"""
Google Slides API integration for portfolio slide generation.
Uses Google Slides API to create slides from templates.
"""
import os
import io
from typing import Dict, Optional
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload, MediaIoBaseUpload
from googleapiclient.errors import HttpError
from config import Config
import base64
import requests


class GoogleSlidesIntegration:
    """Handle Google Slides API operations for slide generation."""
    
    def __init__(self):
        """Initialize Google Slides client."""
        self.service = None
        self.drive_service = None
        self.template_id = Config.CANVA_TEMPLATE_ID  # Reuse template ID config, but it's now a Google Slides template ID
        self._initialize_service()
    
    def _initialize_service(self):
        """Initialize Google Slides and Drive services."""
        try:
            # Try service account first
            if Config.GOOGLE_SERVICE_ACCOUNT_PATH and os.path.exists(Config.GOOGLE_SERVICE_ACCOUNT_PATH):
                credentials = service_account.Credentials.from_service_account_file(
                    Config.GOOGLE_SERVICE_ACCOUNT_PATH,
                    scopes=[
                        'https://www.googleapis.com/auth/presentations',
                        'https://www.googleapis.com/auth/drive',
                        'https://www.googleapis.com/auth/drive.file'
                    ]
                )
            # Try OAuth credentials
            elif Config.GOOGLE_DRIVE_CREDENTIALS_JSON:
                import json
                creds_dict = json.loads(Config.GOOGLE_DRIVE_CREDENTIALS_JSON)
                credentials = Credentials.from_authorized_user_info(creds_dict)
            # Try token.json file
            elif os.path.exists('token.json'):
                credentials = Credentials.from_authorized_user_file(
                    'token.json',
                    scopes=[
                        'https://www.googleapis.com/auth/presentations',
                        'https://www.googleapis.com/auth/drive',
                        'https://www.googleapis.com/auth/drive.file'
                    ]
                )
            else:
                raise ValueError(
                    "Google credentials not found. Please set up OAuth or service account.\n"
                    "Run: python setup_google_oauth.py"
                )
            
            self.service = build('slides', 'v1', credentials=credentials)
            self.drive_service = build('drive', 'v3', credentials=credentials)
            print("✓ Google Slides API initialized")
        except Exception as e:
            print(f"⚠️  Google Slides initialization failed: {e}")
            raise
    
    def create_portfolio_slide(
        self,
        company_data: Dict,
        headshot_image: bytes,
        logo_image: bytes,
        map_image: Optional[bytes] = None,
        output_path: Optional[str] = None
    ) -> bytes:
        """
        Create a portfolio slide using Google Slides template.
        
        Args:
            company_data: Dictionary with company information
            headshot_image: Processed headshot image bytes
            logo_image: Company logo image bytes
            map_image: Optional map image bytes
            output_path: Optional path to save the slide
            
        Returns:
            PDF bytes of the generated slide
        """
        if not self.template_id:
            raise ValueError("GOOGLE_SLIDES_TEMPLATE_ID or CANVA_TEMPLATE_ID not configured")
        
        try:
            # Step 1: Copy the template presentation
            print("   Copying Google Slides template...")
            presentation_id = self._copy_template()
            
            # Step 2: Upload images to Drive and get URLs
            print("   Uploading images to Google Drive...")
            headshot_url = self._upload_image_to_drive(headshot_image, "headshot.png")
            logo_url = self._upload_image_to_drive(logo_image, "logo.png")
            map_url = None
            if map_image:
                map_url = self._upload_image_to_drive(map_image, "map.png")
            
            # Step 3: Populate the slide with data
            print("   Populating slide with company data...")
            self._populate_slide(presentation_id, company_data, headshot_url, logo_url, map_url)
            
            # Step 4: Export as PDF
            print("   Exporting slide as PDF...")
            pdf_bytes = self._export_as_pdf(presentation_id)
            
            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(pdf_bytes)
            
            # Clean up: Delete the temporary presentation
            try:
                self.drive_service.files().delete(fileId=presentation_id).execute()
            except:
                pass  # Ignore cleanup errors
            
            return pdf_bytes
            
        except Exception as e:
            error_str = str(e).lower()
            if any(keyword in error_str for keyword in ["401", "403", "invalid", "unauthorized", "permission"]):
                print(f"❌ Google Slides API authentication failed: {e}")
                print("   💡 Run: python setup_google_oauth.py to set up OAuth")
            
            raise Exception(f"Google Slides API failed: {e}")
    
    def _copy_template(self) -> str:
        """Copy the template presentation and return the new presentation ID."""
        try:
            # Copy the template
            copy_metadata = {
                'name': f"Portfolio Slide - {self.template_id[:10]}"
            }
            copied_file = self.drive_service.files().copy(
                fileId=self.template_id,
                body=copy_metadata
            ).execute()
            
            presentation_id = copied_file.get('id')
            print(f"   ✓ Copied template: {presentation_id}")
            return presentation_id
            
        except HttpError as e:
            raise Exception(f"Failed to copy template: {e}")
    
    def _upload_image_to_drive(self, image_bytes: bytes, filename: str) -> str:
        """Upload image to Google Drive and return the file ID."""
        try:
            file_metadata = {
                'name': filename,
                'parents': [Config.GOOGLE_DRIVE_FOLDER_ID] if Config.GOOGLE_DRIVE_FOLDER_ID else []
            }
            
            media = MediaIoBaseUpload(
                io.BytesIO(image_bytes),
                mimetype='image/png',
                resumable=True
            )
            
            file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            file_id = file.get('id')
            
            # Make the file publicly accessible (for embedding in slides)
            self.drive_service.permissions().create(
                fileId=file_id,
                body={'role': 'reader', 'type': 'anyone'}
            ).execute()
            
            # Return the image URL
            return f"https://drive.google.com/uc?export=view&id={file_id}"
            
        except HttpError as e:
            raise Exception(f"Failed to upload image to Drive: {e}")
    
    def _populate_slide(
        self,
        presentation_id: str,
        company_data: Dict,
        headshot_url: str,
        logo_url: str,
        map_url: Optional[str] = None
    ):
        """Populate the slide with company data and images."""
        try:
            # Get the presentation to find placeholders
            presentation = self.service.presentations().get(
                presentationId=presentation_id
            ).execute()
            
            slides = presentation.get('slides', [])
            if not slides:
                raise Exception("No slides found in template")
            
            # Get the first slide (assuming template has one slide)
            slide_id = slides[0].get('objectId')
            page_elements = slides[0].get('pageElements', [])
            
            # Prepare requests for batch update
            requests = []
            
            # Find and replace text placeholders
            text_replacements = {
                '{{company_name}}': company_data.get('name', ''),
                '{{description}}': company_data.get('description', ''),
                '{{location}}': company_data.get('address', company_data.get('location', '')),
                '{{investment_date}}': company_data.get('investment_date', ''),
                '{{investment_round}}': company_data.get('investment_round', ''),
                '{{founders}}': ', '.join(company_data.get('founders', [])) if isinstance(company_data.get('founders'), list) else company_data.get('founders', ''),
                '{{co_investors}}': ', '.join(company_data.get('co_investors', [])) if isinstance(company_data.get('co_investors'), list) else company_data.get('co_investors', ''),
                '{{background}}': company_data.get('background', company_data.get('description', '')),
            }
            
            # Build investment stage if needed
            investment_stage = company_data.get('investment_stage')
            if not investment_stage:
                round_val = company_data.get('investment_round', 'PRE-SEED')
                quarter_val = company_data.get('quarter', 'Q2')
                year_val = company_data.get('year', '2024')
                investment_stage = f"{round_val} • {quarter_val} {year_val}"
            text_replacements['{{investment_stage}}'] = investment_stage
            
            # Replace text in all text elements
            for element in page_elements:
                if 'shape' in element and 'text' in element['shape']:
                    text_content = element['shape']['text'].get('textElements', [])
                    for text_elem in text_content:
                        if 'textRun' in text_elem:
                            original_text = text_elem['textRun'].get('content', '')
                            for placeholder, value in text_replacements.items():
                                if placeholder in original_text:
                                    requests.append({
                                        'replaceAllText': {
                                            'containsText': {
                                                'text': placeholder,
                                                'matchCase': False
                                            },
                                            'replaceText': value
                                        }
                                    })
            
            # Replace images
            # Find image placeholders by position or name
            # Assuming images are in specific positions (you may need to adjust)
            image_replacements = []
            if headshot_url:
                image_replacements.append(('headshot', headshot_url, 'BOTTOM_RIGHT'))
            if logo_url:
                image_replacements.append(('logo', logo_url, 'TOP_RIGHT'))
            if map_url:
                image_replacements.append(('map', map_url, 'MIDDLE_RIGHT'))
            
            # Replace images by finding elements and updating them
            for element in page_elements:
                if 'image' in element:
                    # Try to identify image by position or other means
                    # For now, we'll replace all images in order
                    pass  # Image replacement logic would go here
            
            # Execute batch update
            if requests:
                body = {'requests': requests}
                self.service.presentations().batchUpdate(
                    presentationId=presentation_id,
                    body=body
                ).execute()
                print("   ✓ Populated slide with company data")
            
        except HttpError as e:
            raise Exception(f"Failed to populate slide: {e}")
    
    def _export_as_pdf(self, presentation_id: str) -> bytes:
        """Export the presentation as PDF."""
        try:
            request = self.drive_service.files().export_media(
                fileId=presentation_id,
                mimeType='application/pdf'
            )
            
            pdf_bytes = io.BytesIO()
            downloader = MediaIoBaseDownload(pdf_bytes, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            pdf_bytes.seek(0)
            return pdf_bytes.read()
            
        except HttpError as e:
            raise Exception(f"Failed to export PDF: {e}")

