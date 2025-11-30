# Quick Start Guide

## 1. Install Dependencies

```bash
cd slauson-automation
pip install -r requirements.txt
```

## 2. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

### Required:
- `NOTION_API_KEY` - Get from https://www.notion.so/my-integrations
- `NOTION_DATABASE_ID` - Run `python setup_notion.py` to create this

### Optional (for full functionality):
- `CANVA_API_KEY` - Canva API key (may require enterprise plan)
- `DOCSEND_API_KEY` - DocSend API key
- `REMOVEBG_API_KEY` - Get from https://www.remove.bg/api
- `OPENAI_API_KEY` - For Granola insights generation

## 3. Set Up Notion Workspace

1. Create a Notion integration:
   - Go to https://www.notion.so/my-integrations
   - Click "New integration"
   - Give it a name (e.g., "Slauson Automation")
   - Copy the "Internal Integration Token" to your `.env` file

2. Create a page in Notion where you want the database

3. Run the setup script:
```bash
python setup_notion.py
```

This will:
- Create the "Portfolio Companies" database
- Create a company template page
- Give you the IDs to add to your `.env` file

4. Share the database with your integration:
   - Open the Portfolio Companies database
   - Click "..." → "Connections" → Add your integration

## 4. Test Your Setup

```bash
python test_integration.py
```

This will verify:
- Configuration is correct
- Notion integration works
- Image processing is set up

## 5. Run the Automation

### Option A: Direct Python Script

```python
from main import PortfolioOnboardingAutomation

company_data = {
    "name": "Example Company",
    "website": "https://example.com",
    "description": "A great company",
    "address": "123 Main St, SF, CA",
    "investment_date": "2024-12-01",
    "co_investors": ["Investor A"],
    "num_employees": 10,
    "first_time_founder": True,
}

automation = PortfolioOnboardingAutomation()
results = automation.process_onboarding(
    company_data,
    "path/to/headshot.jpg",
    "path/to/logo.png"
)
```

### Option B: Webhook Server

Start the webhook server:
```bash
python webhook_listener.py
```

Then send POST requests to `http://localhost:5000/webhook/onboarding` with JSON payload.

## 6. Canva Integration Notes

The Canva API integration is complex and may require:
- Enterprise Canva account
- Specific API access

**Alternative approach:**
If Canva API is not available, you can:
1. Use the image processing to prepare images
2. Manually create slides in Canva using the processed images
3. Or use an alternative slide generation method (PIL/Pillow)

The code includes placeholder methods that you can implement based on your Canva API access level.

## 7. Next Steps

- Set up Zapier/Make.com webhook to trigger automation from Notion forms
- Configure DocSend API keys for automatic deck updates
- Set up Granola integration for meeting notes (see `granola_integration.py`)

## Troubleshooting

### Notion API Errors
- Make sure your integration is shared with the database
- Verify the database ID is correct
- Check that your integration token is valid

### Image Processing Errors
- Remove.bg API key is optional - images will be used as-is if not set
- Make sure image files exist and are readable

### Canva Errors
- Canva API may not be available - this is expected
- Use alternative slide generation or manual process for now

