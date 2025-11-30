"""
Example usage of the Slauson automation suite.
"""
from main import PortfolioOnboardingAutomation
import os


def example_onboarding():
    """Example of how to use the onboarding automation."""
    
    # Example company data (this would come from a form submission)
    company_data = {
        "name": "Acme Corp",
        "website": "https://acme.com",
        "description": "A revolutionary company changing the world",
        "address": "123 Innovation St, San Francisco, CA 94105",
        "birthday": "2024-01-15",  # Founder birthday
        "investment_date": "2024-12-01",
        "co_investors": ["Sequoia Capital", "Andreessen Horowitz"],
        "num_employees": 25,
        "first_time_founder": False,
        "investment_memo_link": "https://drive.google.com/file/d/example",
    }
    
    # Paths to images (replace with actual paths)
    headshot_path = "examples/headshot.jpg"
    logo_path = "examples/logo.png"
    
    # Check if example files exist
    if not os.path.exists(headshot_path):
        print(f"⚠️  Headshot not found at {headshot_path}")
        print("   Please provide a headshot image for testing")
        return
    
    if not os.path.exists(logo_path):
        print(f"⚠️  Logo not found at {logo_path}")
        print("   Please provide a logo image for testing")
        return
    
    # Initialize automation
    print("Initializing automation...")
    automation = PortfolioOnboardingAutomation()
    
    # Process onboarding
    print("Processing onboarding...")
    results = automation.process_onboarding(
        company_data,
        headshot_path,
        logo_path
    )
    
    # Print results
    print("\n" + "=" * 50)
    print("Results:")
    print("=" * 50)
    print(f"Success: {results['success']}")
    print(f"Notion Page ID: {results.get('notion_page_id', 'N/A')}")
    print(f"Notion Folder ID: {results.get('notion_folder_id', 'N/A')}")
    print(f"Canva Slide: {results.get('canva_slide_path', 'N/A')}")
    print(f"DocSend Individual Link: {results.get('docsend_individual_link', 'N/A')}")
    
    if results.get('errors'):
        print("\nErrors:")
        for error in results['errors']:
            print(f"  - {error}")


def example_granola_note():
    """Example of how to process a Granola note."""
    from granola_integration import GranolaIntegration
    
    # This would typically be triggered by a webhook from Granola
    note_id = "example_note_id"
    
    try:
        granola = GranolaIntegration()
        results = granola.process_and_import_note(note_id)
        
        print("Granola note processed:")
        print(f"  Company: {results['company_name']}")
        print(f"  Insights: {results['insights']}")
        
    except Exception as e:
        print(f"Error processing Granola note: {e}")


if __name__ == "__main__":
    print("Slauson Automation - Example Usage")
    print("=" * 50)
    
    # Run example
    example_onboarding()
    
    # Uncomment to test Granola integration:
    # example_granola_note()

