"""
Image processing utilities for portfolio onboarding.
Handles background removal, grayscale conversion, and image manipulation.
"""
import io
import requests
from PIL import Image, ImageEnhance
from typing import Optional
from config import Config


class ImageProcessor:
    """Process images for portfolio slides."""
    
    @staticmethod
    def remove_background(image_path: str, output_path: Optional[str] = None) -> bytes:
        """
        Remove background from image using Remove.bg API.
        
        Args:
            image_path: Path to input image or image URL
            output_path: Optional path to save output image
            
        Returns:
            Bytes of processed image
        """
        if not Config.REMOVEBG_API_KEY:
            # Fallback: return original image if no API key
            print("Warning: REMOVEBG_API_KEY not set. Skipping background removal.")
            with open(image_path, 'rb') as f:
                return f.read()
        
        # Check if this is a placeholder image (skip background removal)
        if 'placeholder' in image_path.lower():
            print("Skipping background removal for placeholder image")
            with open(image_path, 'rb') as f:
                return f.read()
        
        api_url = "https://api.remove.bg/v1.0/removebg"
        
        try:
            with open(image_path, 'rb') as image_file:
                response = requests.post(
                    api_url,
                    files={'image_file': image_file},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': Config.REMOVEBG_API_KEY},
                )
            
            if response.status_code == 200:
                image_bytes = response.content
                if output_path:
                    with open(output_path, 'wb') as out_file:
                        out_file.write(image_bytes)
                return image_bytes
            else:
                # If Remove.bg fails, return original image
                print(f"Warning: Remove.bg API error: {response.status_code} - {response.text}")
                print("Using original image without background removal")
                with open(image_path, 'rb') as f:
                    return f.read()
        except Exception as e:
            # If any error occurs, return original image
            print(f"Warning: Background removal failed: {e}")
            print("Using original image without background removal")
            with open(image_path, 'rb') as f:
                return f.read()
    
    @staticmethod
    def to_grayscale(image_bytes: bytes) -> bytes:
        """
        Convert image to grayscale.
        
        Args:
            image_bytes: Image bytes
            
        Returns:
            Grayscale image bytes
        """
        image = Image.open(io.BytesIO(image_bytes))
        grayscale_image = image.convert('L')
        
        # Convert back to RGB if needed (for compatibility)
        if grayscale_image.mode != 'RGB':
            grayscale_image = grayscale_image.convert('RGB')
        
        output = io.BytesIO()
        grayscale_image.save(output, format='PNG')
        return output.getvalue()
    
    @staticmethod
    def process_headshot(image_path: str, output_path: str) -> bytes:
        """
        Process headshot: remove background and convert to grayscale.
        
        Args:
            image_path: Path to input headshot
            output_path: Path to save processed headshot
            
        Returns:
            Processed image bytes
        """
        try:
            # Remove background (will skip for placeholders or return original on error)
            no_bg_image = ImageProcessor.remove_background(image_path)
            
            # Convert to grayscale
            grayscale_image = ImageProcessor.to_grayscale(no_bg_image)
            
            # Save if output path provided
            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(grayscale_image)
            
            return grayscale_image
        except Exception as e:
            # If processing fails, try to just convert to grayscale
            print(f"Warning: Headshot processing failed: {e}")
            print("Attempting grayscale conversion only...")
            try:
                with open(image_path, 'rb') as f:
                    image_bytes = f.read()
                grayscale_image = ImageProcessor.to_grayscale(image_bytes)
                if output_path:
                    with open(output_path, 'wb') as f:
                        f.write(grayscale_image)
                return grayscale_image
            except Exception as e2:
                print(f"Error: Could not process headshot: {e2}")
                # Return original as last resort
                with open(image_path, 'rb') as f:
                    return f.read()
    
    @staticmethod
    def resize_image(image_bytes: bytes, max_width: int, max_height: int) -> bytes:
        """
        Resize image while maintaining aspect ratio.
        
        Args:
            image_bytes: Image bytes
            max_width: Maximum width
            max_height: Maximum height
            
        Returns:
            Resized image bytes
        """
        image = Image.open(io.BytesIO(image_bytes))
        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        output = io.BytesIO()
        image.save(output, format='PNG')
        return output.getvalue()

