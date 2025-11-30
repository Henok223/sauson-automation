"""
Setup script to create Notion database structure for portfolio companies.
Run this once to set up your Notion workspace.
"""
from notion_client import Client
from config import Config
import json


def create_portfolio_database(parent_page_id: str) -> str:
    """
    Create the Portfolio Companies database in Notion.
    
    Args:
        parent_page_id: ID of the parent page where database should be created
        
    Returns:
        Database ID
    """
    client = Client(auth=Config.NOTION_API_KEY)
    
    database_properties = {
        "Name": {"title": {}},
        "Website": {"url": {}},
        "Description": {"rich_text": {}},
        "Address": {"rich_text": {}},
        "Birthday": {"date": {}},
        "Investment Date": {"date": {}},
        "Co-Investors": {
            "multi_select": {
                "options": []
            }
        },
        "Number of Employees": {"number": {}},
        "First Time Founder": {"checkbox": {}},
        "Investment Memo": {"url": {}},
        "Headshot": {"files": {}},
        "Logo": {"files": {}},
        "Founders": {"rich_text": {}},
        "Location": {"rich_text": {}},
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
    
    response = client.databases.create(
        parent={"page_id": parent_page_id},
        title=[{"text": {"content": "Portfolio Companies"}}],
        properties=database_properties
    )
    
    print(f"✅ Created Portfolio Companies database: {response['id']}")
    print(f"   Add this to your .env file: NOTION_DATABASE_ID={response['id']}")
    
    return response["id"]


def create_company_template(parent_page_id: str) -> str:
    """
    Create a template page for company folders.
    
    Args:
        parent_page_id: ID of the parent page
        
    Returns:
        Template page ID
    """
    client = Client(auth=Config.NOTION_API_KEY)
    
    # Create template page with pre-filled sections
    response = client.pages.create(
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
    
    print(f"✅ Created company template: {response['id']}")
    print(f"   Add this to your .env file: NOTION_TEMPLATE_PAGE_ID={response['id']}")
    
    return response["id"]


def main():
    """Main setup function."""
    print("Notion Setup for Slauson Automation")
    print("=" * 50)
    
    if not Config.NOTION_API_KEY:
        print("❌ Error: NOTION_API_KEY not set in .env file")
        return
    
    print("\nTo set up your Notion workspace:")
    print("1. Create a new page in Notion (or use an existing one)")
    print("2. Get the page ID from the URL (the long string after the last /)")
    print("3. Enter it below when prompted")
    
    parent_page_id = input("\nEnter your Notion parent page ID: ").strip()
    
    if not parent_page_id:
        print("❌ No page ID provided")
        return
    
    print("\nCreating Portfolio Companies database...")
    database_id = create_portfolio_database(parent_page_id)
    
    print("\nCreating company template...")
    template_id = create_company_template(parent_page_id)
    
    print("\n" + "=" * 50)
    print("✅ Setup complete!")
    print("\nAdd these to your .env file:")
    print(f"NOTION_DATABASE_ID={database_id}")
    print(f"NOTION_TEMPLATE_PAGE_ID={template_id}")


if __name__ == "__main__":
    main()

