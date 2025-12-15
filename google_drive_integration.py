"""
Google Drive API integration for uploading PDFs and generating shareable links.
"""
import io
from typing import Optional
from config import Config
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError
import os
import json


class GoogleDriveIntegration:
    """Handle Google Drive API operations."""
    
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    
    def __init__(self):
        """Initialize Google Drive client."""
        self.credentials = None
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google Drive API."""
        creds = None
        
        # Check if we have token.json (for OAuth flow) - preferred for personal account
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
            if creds and creds.valid:
                self.credentials = creds
                self.service = build('drive', 'v3', credentials=creds)
                return
        
        # If token.json exists but expired, refresh it
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                self.credentials = creds
                self.service = build('drive', 'v3', credentials=creds)
                return
            except Exception as e:
                print(f"Warning: Could not refresh token: {e}")
        
        # Try OAuth credentials from environment variable
        if Config.GOOGLE_DRIVE_CREDENTIALS_JSON:
            try:
                creds_info = json.loads(Config.GOOGLE_DRIVE_CREDENTIALS_JSON)
                if creds_info.get('type') != 'service_account':
                    # OAuth credentials
                    creds = Credentials.from_authorized_user_info(creds_info, self.SCOPES)
                    if creds and creds.valid:
                        self.credentials = creds
                        self.service = build('drive', 'v3', credentials=creds)
                        return
            except json.JSONDecodeError:
                pass
        
        # Fallback to service account if OAuth not available
        service_account_path = os.getenv('GOOGLE_SERVICE_ACCOUNT_PATH')
        if service_account_path and os.path.exists(service_account_path):
            from google.oauth2 import service_account
            creds = service_account.Credentials.from_service_account_file(
                service_account_path, scopes=self.SCOPES
            )
            self.credentials = creds
            self.service = build('drive', 'v3', credentials=creds)
            print("Warning: Using service account. For personal Google Drive, set up OAuth.")
            return
        
        # If no credentials, raise error with instructions
        raise ValueError(
            "Google Drive credentials not configured. "
            "For personal Google Drive (hmikaeltewolde@gmail.com), you need to set up OAuth. "
            "Run the OAuth setup script or set GOOGLE_DRIVE_CREDENTIALS_JSON"
        )
    
    def upload_pdf(
        self,
        pdf_bytes: bytes,
        filename: str,
        folder_id: Optional[str] = None
    ) -> str:
        """
        Upload PDF to Google Drive and return shareable link.
        
        Args:
            pdf_bytes: PDF file bytes
            filename: Name for the file
            folder_id: Optional Google Drive folder ID to upload to
            
        Returns:
            Shareable link to the uploaded file
        """
        if not self.service:
            raise ValueError("Google Drive service not initialized")
        
        try:
            # Create file metadata
            file_metadata = {
                'name': filename,
            }
            if folder_id:
                file_metadata['parents'] = [folder_id]
            
            # Create media upload
            media = MediaIoBaseUpload(
                io.BytesIO(pdf_bytes),
                mimetype='application/pdf',
                resumable=True
            )
            
            # Upload file
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink, webContentLink'
            ).execute()
            
            file_id = file.get('id')
            
            # Make file shareable (anyone with link can view)
            self.service.permissions().create(
                fileId=file_id,
                body={'role': 'reader', 'type': 'anyone'}
            ).execute()
            
            # Get shareable link
            file = self.service.files().get(
                fileId=file_id,
                fields='webViewLink, webContentLink'
            ).execute()
            
            # Prefer webViewLink (opens in Drive) over webContentLink (direct download)
            shareable_link = file.get('webViewLink') or file.get('webContentLink')
            
            if not shareable_link:
                # Fallback: construct link manually
                shareable_link = f"https://drive.google.com/file/d/{file_id}/view"
            
            return shareable_link
            
        except HttpError as error:
            raise Exception(f"Google Drive upload error: {error}")
    
    def create_folder(self, folder_name: str, parent_folder_id: Optional[str] = None) -> str:
        """
        Create a folder in Google Drive.
        
        Args:
            folder_name: Name of the folder
            parent_folder_id: Optional parent folder ID
            
        Returns:
            Folder ID
        """
        if not self.service:
            raise ValueError("Google Drive service not initialized")
        
        try:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_folder_id:
                file_metadata['parents'] = [parent_folder_id]
            
            folder = self.service.files().create(
                body=file_metadata,
                fields='id'
            ).execute()
            
            return folder.get('id')
        except HttpError as error:
            raise Exception(f"Google Drive folder creation error: {error}")

