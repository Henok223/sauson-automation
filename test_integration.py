"""
Test script to verify integrations are working.
"""
from config import Config
from notion_integration import NotionIntegration
from image_processor import ImageProcessor
import os


def test_notion():
    """Test Notion integration."""
    print("Testing Notion integration...")
    try:
        Config.validate()
        notion = NotionIntegration()
        print("✅ Notion client initialized")
        
        # Try to query database
        if Config.NOTION_DATABASE_ID:
            try:
                # This will fail if database doesn't exist or isn't accessible
                response = notion.client.databases.retrieve(Config.NOTION_DATABASE_ID)
                print(f"✅ Notion database accessible: {response.get('title', [{}])[0].get('plain_text', 'Unknown')}")
            except Exception as e:
                print(f"⚠️  Could not access database: {e}")
                print("   Make sure NOTION_DATABASE_ID is correct and the integration has access")
        else:
            print("⚠️  NOTION_DATABASE_ID not set")
            
    except Exception as e:
        print(f"❌ Notion integration failed: {e}")


def test_image_processing():
    """Test image processing."""
    print("\nTesting image processing...")
    try:
        processor = ImageProcessor()
        print("✅ Image processor initialized")
        
        if Config.REMOVEBG_API_KEY:
            print("✅ Remove.bg API key configured")
        else:
            print("⚠️  REMOVEBG_API_KEY not set - background removal will be skipped")
            
    except Exception as e:
        print(f"❌ Image processing setup failed: {e}")


def test_config():
    """Test configuration."""
    print("Testing configuration...")
    try:
        required = [
            ("NOTION_API_KEY", Config.NOTION_API_KEY),
        ]
        
        optional = [
            ("NOTION_DATABASE_ID", Config.NOTION_DATABASE_ID),
            ("NOTION_TEMPLATE_PAGE_ID", Config.NOTION_TEMPLATE_PAGE_ID),
            ("CANVA_API_KEY", Config.CANVA_API_KEY),
            ("DOCSEND_API_KEY", Config.DOCSEND_API_KEY),
            ("REMOVEBG_API_KEY", Config.REMOVEBG_API_KEY),
            ("OPENAI_API_KEY", Config.OPENAI_API_KEY),
        ]
        
        print("\nRequired configuration:")
        all_required = True
        for name, value in required:
            status = "✅" if value else "❌"
            print(f"  {status} {name}")
            if not value:
                all_required = False
        
        print("\nOptional configuration:")
        for name, value in optional:
            status = "✅" if value else "⚠️ "
            print(f"  {status} {name}")
        
        if all_required:
            print("\n✅ All required configuration present")
        else:
            print("\n❌ Missing required configuration")
            
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")


def main():
    """Run all tests."""
    print("Slauson Automation Integration Tests")
    print("=" * 50)
    
    # Check if .env exists
    if not os.path.exists(".env"):
        print("⚠️  .env file not found")
        print("   Copy .env.example to .env and fill in your API keys")
        return
    
    test_config()
    test_notion()
    test_image_processing()
    
    print("\n" + "=" * 50)
    print("Test complete!")


if __name__ == "__main__":
    main()

