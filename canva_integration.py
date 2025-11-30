"""
Canva API integration for portfolio slide generation.
"""
import requests
from typing import Dict, Optional, BinaryIO
from config import Config
import base64
import io


class CanvaIntegration:
    """Handle Canva API operations for slide generation."""
    
    def __init__(self):
        """Initialize Canva client."""
        self.api_key = Config.CANVA_API_KEY
        self.base_url = "https://api.canva.com/rest/v1"
        self.template_id = Config.CANVA_TEMPLATE_ID
    
    def create_portfolio_slide(
        self,
        company_data: Dict,
        headshot_image: bytes,
        logo_image: bytes,
        output_path: Optional[str] = None
    ) -> bytes:
        """
        Create a portfolio slide using Canva template.
        
        Args:
            company_data: Dictionary with company information
            headshot_image: Processed headshot image bytes
            logo_image: Company logo image bytes
            output_path: Optional path to save the slide
            
        Returns:
            PDF bytes of the generated slide
        """
        if not self.api_key:
            raise ValueError("CANVA_API_KEY not configured. Use create_slide_alternative() for manual processing.")
        
        if not self.template_id:
            raise ValueError("CANVA_TEMPLATE_ID not configured")
        
        try:
            # Upload images to Canva
            headshot_upload_id = self._upload_image(headshot_image, "headshot")
            logo_upload_id = self._upload_image(logo_image, "logo")
            
            # Create design from template
            design_id = self._duplicate_template()
            
            # Replace elements in the design
            self._replace_text_elements(design_id, company_data)
            self._replace_image_elements(design_id, headshot_upload_id, logo_upload_id, company_data)
            
            # Export as PDF
            pdf_bytes = self._export_as_pdf(design_id)
            
            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(pdf_bytes)
            
            return pdf_bytes
        except Exception as e:
            # Fallback to alternative method if Canva API fails
            print(f"Canva API failed: {e}. Using alternative method...")
            import tempfile
            import os
            with tempfile.TemporaryDirectory() as temp_dir:
                headshot_path = os.path.join(temp_dir, "headshot.png")
                logo_path = os.path.join(temp_dir, "logo.png")
                with open(headshot_path, 'wb') as f:
                    f.write(headshot_image)
                with open(logo_path, 'wb') as f:
                    f.write(logo_image)
                return self.create_slide_alternative(company_data, headshot_path, logo_path)
    
    def _upload_image(self, image_bytes: bytes, image_type: str) -> str:
        """
        Upload image to Canva and get upload ID.
        
        Args:
            image_bytes: Image bytes to upload
            image_type: Type of image (headshot, logo)
            
        Returns:
            Upload ID from Canva
        """
        # Note: This is a simplified version. Actual Canva API may differ.
        # You may need to use Canva's upload endpoint or direct file upload
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # For now, return a placeholder. Actual implementation depends on Canva API structure
        # You might need to use Canva's design API or webhook-based approach
        return f"upload_{image_type}_{hash(image_bytes)}"
    
    def _duplicate_template(self) -> str:
        """
        Duplicate the template design.
        
        Returns:
            Design ID of duplicated template
        """
        # Placeholder - actual implementation depends on Canva API
        # Canva API structure may vary, this is a conceptual implementation
        return f"design_{self.template_id}_copy"
    
    def _replace_text_elements(self, design_id: str, company_data: Dict):
        """Replace text elements in the design."""
        # Implementation depends on Canva API structure
        pass
    
    def _replace_image_elements(
        self,
        design_id: str,
        headshot_upload_id: str,
        logo_upload_id: str,
        company_data: Dict
    ):
        """Replace image elements in the design."""
        # Implementation depends on Canva API structure
        pass
    
    def _export_as_pdf(self, design_id: str) -> bytes:
        """
        Export design as PDF.
        
        Args:
            design_id: Canva design ID
            
        Returns:
            PDF bytes
        """
        # Placeholder - actual implementation depends on Canva API
        # This would typically involve calling Canva's export endpoint
        return b"PDF_CONTENT_PLACEHOLDER"
    
    def create_slide_alternative(
        self,
        company_data: Dict,
        headshot_path: str,
        logo_path: str,
        template_path: Optional[str] = None
    ) -> bytes:
        """
        Alternative approach: Use image processing + template manipulation.
        This can be used if Canva API is not available.
        
        Args:
            company_data: Company information
            headshot_path: Path to processed headshot
            logo_path: Path to logo
            template_path: Path to template image/PDF
            
        Returns:
            PDF bytes of generated slide
        """
        # This would use PIL/Pillow or similar to composite images
        # For now, return placeholder
        # In production, you'd:
        # 1. Load template
        # 2. Place headshot at correct position
        # 3. Place logo at correct position
        # 4. Add text elements
        # 5. Export as PDF
        
        from PIL import Image, ImageDraw, ImageFont
        
        # Placeholder implementation
        return b"ALTERNATIVE_SLIDE_PDF"

