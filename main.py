"""
Main orchestrator for Slauson portfolio onboarding automation.
"""
import sys
from typing import Dict, Optional
from config import Config
from notion_integration import NotionIntegration
from canva_integration import CanvaIntegration
from docsend_integration import DocSendIntegration
from image_processor import ImageProcessor
import os
import tempfile


class PortfolioOnboardingAutomation:
    """Main automation orchestrator."""
    
    def __init__(self, require_notion=False):
        """Initialize all integrations."""
        Config.validate(require_notion=require_notion)
        
        # Notion is optional if using Zapier
        self.notion = NotionIntegration() if Config.NOTION_API_KEY else None
        self.canva = CanvaIntegration()
        self.docsend = DocSendIntegration()
        self.image_processor = ImageProcessor()
    
    def process_onboarding(
        self,
        company_data: Dict,
        headshot_path: str,
        logo_path: str
    ) -> Dict:
        """
        Process complete onboarding workflow.
        
        Args:
            company_data: Dictionary with company information
            headshot_path: Path to founder headshot
            logo_path: Path to company logo
            
        Returns:
            Dictionary with results and created resource IDs
        """
        results = {
            "success": False,
            "notion_page_id": None,
            "notion_folder_id": None,
            "canva_slide_path": None,
            "docsend_individual_link": None,
            "docsend_master_link": None,
            "errors": []
        }
        
        try:
            # Step 1: Process images
            print("Processing images...")
            with tempfile.TemporaryDirectory() as temp_dir:
                processed_headshot_path = os.path.join(temp_dir, "headshot_processed.png")
                processed_headshot = self.image_processor.process_headshot(
                    headshot_path,
                    processed_headshot_path
                )
                
                # Step 2: Create Notion database entry (optional - Zapier handles this)
                if self.notion and Config.NOTION_DATABASE_ID and Config.NOTION_DATABASE_ID != "your_portfolio_database_id_here":
                    print("Creating Notion database entry...")
                    try:
                        notion_page_id = self.notion.create_portfolio_company_entry(company_data)
                        results["notion_page_id"] = notion_page_id
                    except Exception as e:
                        print(f"Warning: Notion entry creation failed: {e}")
                        results["errors"].append(f"Notion entry: {str(e)}")
                else:
                    print("Skipping Notion entry (Zapier handles this)")
                
                # Step 3: Create Notion folder (optional)
                if self.notion and Config.NOTION_TEMPLATE_PAGE_ID and Config.NOTION_TEMPLATE_PAGE_ID != "your_company_template_page_id_here":
                    print("Creating Notion company folder...")
                    try:
                        notion_folder_id = self.notion.create_company_folder(
                            company_data.get("name", "New Company")
                        )
                        results["notion_folder_id"] = notion_folder_id
                    except Exception as e:
                        print(f"Warning: Notion folder creation failed: {e}")
                        results["errors"].append(f"Notion folder: {str(e)}")
                else:
                    print("Skipping Notion folder (Zapier handles this)")
                
                # Step 4: Generate Canva slide
                print("Generating Canva slide...")
                slide_pdf_path = os.path.join(temp_dir, "slide.pdf")
                try:
                    with open(logo_path, 'rb') as f:
                        logo_bytes = f.read()
                    
                    # Try Canva API first, fallback to alternative if not available
                    if Config.CANVA_API_KEY and Config.CANVA_TEMPLATE_ID:
                        slide_pdf = self.canva.create_portfolio_slide(
                            company_data,
                            processed_headshot,
                            logo_bytes,
                            slide_pdf_path
                        )
                    else:
                        print("Canva API not configured, using alternative method...")
                        # Save processed headshot temporarily for alternative method
                        temp_headshot_path = os.path.join(temp_dir, "headshot_processed.png")
                        with open(temp_headshot_path, 'wb') as f:
                            f.write(processed_headshot)
                        slide_pdf = self.canva.create_slide_alternative(
                            company_data,
                            temp_headshot_path,
                            logo_path
                        )
                    
                    # Save PDF bytes to file and store in results
                    if isinstance(slide_pdf, bytes):
                        with open(slide_pdf_path, 'wb') as f:
                            f.write(slide_pdf)
                        results["canva_slide_pdf_bytes"] = slide_pdf
                    else:
                        # If it's already saved to path, read it
                        if os.path.exists(slide_pdf_path):
                            with open(slide_pdf_path, 'rb') as f:
                                results["canva_slide_pdf_bytes"] = f.read()
                    
                    results["canva_slide_path"] = slide_pdf_path
                except Exception as e:
                    print(f"Warning: Canva slide generation failed: {e}")
                    results["errors"].append(f"Canva: {str(e)}")
                    # Continue with other steps - slide generation is optional
                
                # Step 5: Upload to DocSend (optional)
                if Config.DOCSEND_API_KEY and Config.DOCSEND_API_KEY != "your_docsend_api_key_here":
                    if "canva_slide_path" in results and results["canva_slide_path"]:
                        print("Uploading to DocSend...")
                        try:
                            with open(slide_pdf_path, 'rb') as f:
                                slide_pdf_bytes = f.read()
                            
                            # Upload individual slide
                            individual_link = self.docsend.upload_individual_slide(
                                slide_pdf_bytes,
                                company_data.get("name", "Company")
                            )
                            results["docsend_individual_link"] = individual_link
                            
                            # Update master presentation (if configured)
                            if Config.DOCSEND_MASTER_DECK_ID and Config.DOCSEND_MASTER_DECK_ID != "your_master_presentation_deck_id_here":
                                # This would require fetching existing master deck,
                                # merging with new slide, and uploading
                                # For now, skip if not fully configured
                                pass
                                
                        except Exception as e:
                            print(f"Warning: DocSend upload failed: {e}")
                            results["errors"].append(f"DocSend: {str(e)}")
                else:
                    print("Skipping DocSend upload (not configured)")
            
            results["success"] = True
            print("Onboarding automation completed successfully!")
            
        except Exception as e:
            print(f"Error in onboarding automation: {e}")
            results["errors"].append(str(e))
            results["success"] = False
        
        return results


def main():
    """Main entry point."""
    print("Slauson Portfolio Onboarding Automation")
    print("=" * 50)
    
    # Example usage - in production, this would be triggered by form submission
    example_company_data = {
        "name": "Example Company",
        "website": "https://example.com",
        "description": "An example portfolio company",
        "address": "123 Main St, San Francisco, CA",
        "birthday": "2024-01-15",
        "investment_date": "2024-12-01",
        "co_investors": ["Investor A", "Investor B"],
        "num_employees": 10,
        "first_time_founder": True,
        "investment_memo_link": "https://drive.google.com/..."
    }
    
    # Example file paths - replace with actual paths
    headshot_path = "path/to/headshot.jpg"
    logo_path = "path/to/logo.png"
    
    # Check if running in interactive mode or with arguments
    if len(sys.argv) > 1:
        # Could accept JSON file or command-line arguments
        pass
    
    automation = PortfolioOnboardingAutomation()
    
    # For testing, you can uncomment and provide actual file paths:
    # results = automation.process_onboarding(
    #     example_company_data,
    #     headshot_path,
    #     logo_path
    # )
    # print("\nResults:", results)
    
    print("\nTo use this automation:")
    print("1. Set up your .env file with API keys")
    print("2. Configure Notion database and template IDs")
    print("3. Call automation.process_onboarding() with company data")


if __name__ == "__main__":
    main()

