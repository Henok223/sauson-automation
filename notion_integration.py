"""
Notion API integration for portfolio company management.
"""
from notion_client import Client
from typing import Dict, List, Optional
from config import Config
import uuid


class NotionIntegration:
    """Handle Notion API operations."""
    
    def __init__(self):
        """Initialize Notion client."""
        if not Config.NOTION_API_KEY:
            raise ValueError("NOTION_API_KEY not configured. Notion integration is optional when using Zapier.")
        self.client = Client(auth=Config.NOTION_API_KEY)
    
    def create_portfolio_company_entry(self, company_data: Dict) -> str:
        """
        Create a new entry in the Portfolio Companies database.
        
        Args:
            company_data: Dictionary containing company information
            
        Returns:
            Page ID of created entry
        """
        if not Config.NOTION_DATABASE_ID:
            raise ValueError("NOTION_DATABASE_ID not configured")
        
        properties = self._format_company_properties(company_data)
        
        response = self.client.pages.create(
            parent={"database_id": Config.NOTION_DATABASE_ID},
            properties=properties
        )
        
        return response["id"]
    
    def _format_company_properties(self, data: Dict) -> Dict:
        """
        Format company data into Notion properties format.
        
        Args:
            data: Raw company data
            
        Returns:
            Formatted properties dictionary
        """
        properties = {}
        
        # Text fields
        if "name" in data:
            properties["Name"] = {"title": [{"text": {"content": data["name"]}}]}
        
        if "website" in data:
            properties["Website"] = {"url": data["website"]}
        
        if "description" in data:
            properties["Description"] = {"rich_text": [{"text": {"content": data["description"]}}]}
        
        if "address" in data:
            properties["Address"] = {"rich_text": [{"text": {"content": data["address"]}}]}
        
        # Date fields
        if "birthday" in data:
            properties["Birthday"] = {"date": {"start": data["birthday"]}}
        
        if "investment_date" in data:
            properties["Investment Date"] = {"date": {"start": data["investment_date"]}}
        
        # Multi-select fields
        if "co_investors" in data:
            if isinstance(data["co_investors"], list):
                properties["Co-Investors"] = {
                    "multi_select": [{"name": investor} for investor in data["co_investors"]]
                }
        
        # Number fields
        if "num_employees" in data:
            properties["Number of Employees"] = {"number": data["num_employees"]}
        
        # Checkbox fields
        if "first_time_founder" in data:
            properties["First Time Founder"] = {"checkbox": data["first_time_founder"]}
        
        # URL fields
        if "investment_memo_link" in data:
            properties["Investment Memo"] = {"url": data["investment_memo_link"]}
        
        return properties
    
    def create_company_folder(self, company_name: str, template_page_id: Optional[str] = None) -> str:
        """
        Create a company subfolder with pre-filled sections.
        
        Args:
            company_name: Name of the company
            template_page_id: Optional template page to duplicate
            
        Returns:
            Page ID of created folder
        """
        if template_page_id or Config.NOTION_TEMPLATE_PAGE_ID:
            # Duplicate template
            template_id = template_page_id or Config.NOTION_TEMPLATE_PAGE_ID
            response = self.client.pages.create(
                parent={"page_id": template_id},
                properties={
                    "title": {"title": [{"text": {"content": company_name}}]}
                }
            )
            return response["id"]
        else:
            # Create new page with basic structure
            parent_id = Config.NOTION_DATABASE_ID
            response = self.client.pages.create(
                parent={"page_id": parent_id},
                properties={
                    "title": {"title": [{"text": {"content": company_name}}]}
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
                        "type": "heading_1",
                        "heading_1": {
                            "rich_text": [{"text": {"content": "Updates"}}]
                        }
                    },
                    {
                        "object": "block",
                        "type": "heading_1",
                        "heading_1": {
                            "rich_text": [{"text": {"content": "Contacts"}}]
                        }
                    }
                ]
            )
            return response["id"]
    
    def add_granola_note(self, company_page_id: str, note_content: str, meeting_title: str) -> str:
        """
        Add a Granola meeting note to a company's Notion page.
        
        Args:
            company_page_id: Notion page ID of the company
            note_content: Content of the meeting note
            meeting_title: Title of the meeting
            
        Returns:
            Block ID of created note
        """
        response = self.client.blocks.children.append(
            block_id=company_page_id,
            children=[
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"text": {"content": meeting_title}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": note_content}}]
                    }
                }
            ]
        )
        return response["results"][0]["id"] if response["results"] else None
    
    def get_company_by_name(self, company_name: str) -> Optional[Dict]:
        """
        Find a company in the database by name.
        
        Args:
            company_name: Name of the company to find
            
        Returns:
            Company page data or None if not found
        """
        if not Config.NOTION_DATABASE_ID:
            return None
        
        response = self.client.databases.query(
            database_id=Config.NOTION_DATABASE_ID,
            filter={
                "property": "Name",
                "title": {
                    "equals": company_name
                }
            }
        )
        
        if response["results"]:
            return response["results"][0]
        return None

