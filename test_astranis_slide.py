#!/usr/bin/env python3
"""
Test script to generate a slide for Astranis using the Canva integration.
"""
import os
import sys
from pathlib import Path

# Try to load dotenv if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Note: python-dotenv not installed, using environment variables directly")

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canva_integration import CanvaIntegration
from image_processor import ImageProcessor

def test_astranis_slide():
    """Test slide generation with Astranis company data."""
    
    print("🚀 Testing slide generation for Astranis...")
    print("=" * 60)
    
    # Astranis company data
    company_data = {
        "name": "Astranis",
        "description": "Astranis is building small, low-cost telecommunications satellites to connect the four billion people who currently lack internet access.",
        "address": "San Francisco, CA",
        "location": "San Francisco, CA",
        "investment_date": "2021-03-15",
        "investment_round": "SERIES B",
        "quarter": "Q1",
        "year": "2021",
        "investment_stage": "SERIES B • Q1 2021",
        "founders": "John Gedmark\nRyan McLinko",
        "co_investors": "Andreessen Horowitz\nVenrock\nTribe Capital",
        "background": "Astranis is revolutionizing satellite internet by building smaller, more cost-effective satellites. The company's innovative approach enables faster deployment and lower costs, making internet access more accessible globally. Founded in 2015, Astranis has raised over $350M to date."
    }
    
    # Check for template path
    template_path = os.getenv('SLIDE_TEMPLATE_PATH')
    if not template_path or not os.path.exists(template_path):
        print("❌ Error: SLIDE_TEMPLATE_PATH not set or file doesn't exist")
        print(f"   Expected: {template_path}")
        print("   Please set SLIDE_TEMPLATE_PATH in your .env file")
        return False
    
    print(f"✓ Template found: {template_path}")
    
    # Create placeholder images (or use existing ones if available)
    temp_dir = Path("temp_test")
    temp_dir.mkdir(exist_ok=True)
    
    # Create placeholder headshot (you can replace with real image)
    headshot_path = temp_dir / "headshot_placeholder.png"
    logo_path = temp_dir / "logo_placeholder.png"
    map_path = temp_dir / "map_placeholder.png"
    
    # Check if we have real images, otherwise create placeholders
    from PIL import Image, ImageDraw, ImageFont
    
    if not headshot_path.exists():
        print("Creating placeholder headshot...")
        img = Image.new('RGB', (400, 400), color='lightgray')
        draw = ImageDraw.Draw(img)
        draw.ellipse([50, 50, 350, 350], fill='gray', outline='black', width=3)
        draw.text((150, 180), "Headshot", fill='black', anchor='mm')
        img.save(headshot_path)
    
    if not logo_path.exists():
        print("Creating placeholder logo...")
        img = Image.new('RGB', (200, 200), color='white')
        draw = ImageDraw.Draw(img)
        draw.rectangle([20, 20, 180, 180], fill='blue', outline='black', width=2)
        draw.text((100, 100), "LOGO", fill='white', anchor='mm')
        img.save(logo_path)
    
    # Generate map using Gemini if available
    if os.getenv('GEMINI_API_KEY'):
        print("Generating map with Gemini...")
        try:
            map_bytes = ImageProcessor.generate_map_with_gemini("San Francisco, CA")
            with open(map_path, 'wb') as f:
                f.write(map_bytes)
            print(f"✓ Map generated: {map_path}")
        except Exception as e:
            print(f"⚠ Could not generate map: {e}")
            # Create placeholder map
            img = Image.new('RGB', (600, 400), color='#2a2a2a')
            draw = ImageDraw.Draw(img)
            draw.text((300, 200), "Map Placeholder", fill='white', anchor='mm')
            img.save(map_path)
    else:
        print("⚠ GEMINI_API_KEY not set, using placeholder map")
        img = Image.new('RGB', (600, 400), color='#2a2a2a')
        draw = ImageDraw.Draw(img)
        draw.text((300, 200), "Map Placeholder", fill='white', anchor='mm')
        img.save(map_path)
    
    print(f"✓ Headshot: {headshot_path}")
    print(f"✓ Logo: {logo_path}")
    print(f"✓ Map: {map_path}")
    print()
    
    # Initialize Canva integration
    try:
        canva = CanvaIntegration()
        print("✓ CanvaIntegration initialized")
    except Exception as e:
        print(f"❌ Error initializing CanvaIntegration: {e}")
        return False
    
    # Generate slide
    output_path = temp_dir / "astranis_slide.pdf"
    print(f"\n📄 Generating slide...")
    print(f"   Output: {output_path}")
    print()
    
    try:
        # Use create_slide_alternative which accepts template_slide_path
        pdf_bytes = canva.create_slide_alternative(
            company_data=company_data,
            headshot_path=str(headshot_path),
            logo_path=str(logo_path),
            template_path=template_path,
            map_path=str(map_path) if map_path.exists() else None
        )
        
        # Write PDF bytes to file
        with open(output_path, 'wb') as f:
            f.write(pdf_bytes)
        
        print()
        print("=" * 60)
        print("✅ SUCCESS! Slide generated successfully!")
        print(f"   📄 PDF saved to: {output_path}")
        print(f"   📊 Size: {len(pdf_bytes) / 1024:.1f} KB")
        print()
        print("   You can now open the PDF to view the generated slide.")
        print("=" * 60)
        
        # Open the PDF automatically
        import subprocess
        subprocess.run(['open', str(output_path)], check=False)
        print(f"   📂 Opened PDF in default viewer")
        
        return True
        
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ ERROR generating slide:")
        print(f"   {str(e)}")
        print()
        import traceback
        print("Full traceback:")
        traceback.print_exc()
        print("=" * 60)
        return False

if __name__ == "__main__":
    success = test_astranis_slide()
    sys.exit(0 if success else 1)

