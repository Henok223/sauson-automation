"""
Script to create a test Portfolio Companies database in your Notion workspace.
This creates the database structure you need for testing.
"""
from notion_client import Client
from config import Config
import sys


def create_test_database(parent_page_id: str) -> dict:
    """
    Create a test Portfolio Companies database.
    
    Args:
        parent_page_id: ID of the parent page where database should be created
        
    Returns:
        Dictionary with database ID and template ID
    """
    if not Config.NOTION_API_KEY:
        print("❌ Error: NOTION_API_KEY not set in .env file")
        sys.exit(1)
    
    client = Client(auth=Config.NOTION_API_KEY)
    
    print("Creating Portfolio Companies database...")
    
    # Define database properties matching Slauson's structure
    database_properties = {
        "Name": {"title": {}},  # Title is always first
        "Website": {"url": {}},
        "Description": {"rich_text": {}},
        "Address": {"rich_text": {}},
        "Investment Date": {"date": {}},
        "Co-Investors": {
            "multi_select": {
                "options": []  # You can add options later
            }
        },
        "Number of Employees": {"number": {}},
        "First Time Founder": {"checkbox": {}},
        "Investment Memo": {"url": {}},
        "Headshot": {"files": {}},
        "Logo": {"files": {}},
        "Status": {
            "select": {
                "options": [
                    {"name": "Draft", "color": "gray"},
                    {"name": "Ready", "color": "green"},
                    {"name": "Pending", "color": "yellow"},
                    {"name": "Processed", "color": "blue"}
                ]
            }
        },
        "DocSend Link": {"url": {}},
    }
    
    try:
        # Create database
        response = client.databases.create(
            parent={"page_id": parent_page_id},
            title=[{"text": {"content": "Portfolio Companies"}}],
            properties=database_properties
        )
        
        database_id = response["id"]
        print(f"✅ Created database: {database_id}")
        
        # Create template page
        print("\nCreating company template page...")
        template_response = client.pages.create(
            parent={"page_id": parent_page_id},
            properties={
                "title": {"title": [{"text": {"content": "Company Template"}}]}
            },
            children=[
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"text": {"content": "Notes"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": "Meeting notes and updates will appear here."}}]
                    }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"text": {"content": "Updates"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": "Company updates and milestones."}}]
                    }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"text": {"content": "Contacts"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": "Key contacts and team members."}}]
                    }
                },
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"text": {"content": "Onboarding Call"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": "Slauson syllabus and onboarding materials."}}]
                    }
                }
            ]
        )
        
        template_id = template_response["id"]
        print(f"✅ Created template: {template_id}")
        
        return {
            "database_id": database_id,
            "template_id": template_id,
            "database_url": response.get("url", ""),
            "template_url": template_response.get("url", "")
        }
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        raise


def main():
    """Main function to create test database."""
    print("=" * 60)
    print("Create Test Portfolio Companies Database")
    print("=" * 60)
    print()
    
    if not Config.NOTION_API_KEY:
        print("❌ Error: NOTION_API_KEY not set")
        print("\nPlease:")
        print("1. Create a .env file")
        print("2. Add: NOTION_API_KEY=secret_your_token_here")
        print("3. Get token from: https://www.notion.so/my-integrations")
        return
    
    print("To create the database, you need a parent page ID.")
    print("\nSteps:")
    print("1. Create a new page in Notion (or use existing)")
    print("2. Copy the page ID from the URL")
    print("   URL format: https://www.notion.so/Page-Name-abc123def456...")
    print("   The ID is: abc123def456... (the part after the last /)")
    print()
    
    parent_page_id = input("Enter your Notion parent page ID: ").strip()
    
    if not parent_page_id:
        print("❌ No page ID provided")
        return
    
    # Remove any query parameters
    parent_page_id = parent_page_id.split('?')[0]
    
    print()
    print("Creating database and template...")
    print()
    
    try:
        result = create_test_database(parent_page_id)
        
        print()
        print("=" * 60)
        print("✅ Setup Complete!")
        print("=" * 60)
        print()
        print("Add these to your .env file:")
        print()
        print(f"NOTION_DATABASE_ID={result['database_id']}")
        print(f"NOTION_TEMPLATE_PAGE_ID={result['template_id']}")
        print()
        print("Database URL:")
        print(result['database_url'])
        print()
        print("Template URL:")
        print(result['template_url'])
        print()
        print("Next steps:")
        print("1. Open the database in Notion")
        print("2. Share it with your Zapier integration:")
        print("   - Click '...' → 'Connections' → Add your integration")
        print("3. Create a test entry with Status = 'Ready'")
        print("4. Configure Zapier to use this database")
        print()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("- Make sure the parent page ID is correct")
        print("- Verify your Notion API key is valid")
        print("- Check that your integration has access to the parent page")


if __name__ == "__main__":
    main()

