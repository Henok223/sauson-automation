# ✅ Ready to Test - Option A Complete!

## What's Been Configured

### ✅ Canva Integration (Alternative Method)
- **Status**: Using programmatic slide generation (no Canva API needed)
- **Design**: Updated to match your template style:
  - Orange vertical sidebar on left
  - Dark grey background
  - Yellow highlight boxes for sections
  - Proper positioning of headshots, logo, and map
- **Fields Supported**: All your Data Autofill fields:
  - `company_name`
  - `description`
  - `location`
  - `investment_stage` (or separate round/quarter/year)
  - `founders`
  - `co_investors`
  - `background`

### ✅ Google Drive
- Service account configured
- Ready to upload PDFs

### ✅ Notion
- API key configured
- Ready to update records

### ✅ Image Processing
- Gemini headshot processing (background removal, greyscale, combining)
- Gemini map generation (matching your style)

## What's Next

### 1. Add Notion Database Properties ⚠️

You need to add these properties to your Notion database:

- **Google Drive Link** (or `Drive Link` or `PDF Link` or `Slide Link`)
  - Type: **URL**
  
- **DocSend Link** (or `DocSend` or `Presentation Link`)
  - Type: **URL**
  
- **Status** (or `Slide Status` or `Processing Status`)
  - Type: **Select** (with "completed" option) OR **Text**

**Action**: Add these properties to your Notion database, then tell me the exact property names you're using.

### 2. Test the Workflow 🧪

Once Notion properties are added, you can test with a webhook:

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test Company",
      "description": "Test description",
      "location": "Los Angeles",
      "investment_date": "2024-12-01",
      "investment_stage": "PRE-SEED • Q2 2024",
      "founders": ["Founder 1"],
      "co_investors": ["Investor 1"],
      "background": "Test background text"
    },
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png",
    "notion_page_id": "your_page_id"
  }'
```

### 3. Start the Webhook Server

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python webhook_listener.py
```

## What Will Happen

When you send a webhook:

1. ✅ Downloads headshots and logo from URLs
2. ✅ Processes headshots with Gemini (background removal, greyscale, combining)
3. ✅ Generates map with Gemini (matching your style)
4. ✅ Creates slide programmatically (orange sidebar, dark background, yellow highlights)
5. ✅ Exports as PDF
6. ✅ Uploads to Google Drive (returns shareable link)
7. ✅ Uploads to DocSend (returns shareable link)
8. ✅ Updates Notion record (adds links + sets status to "completed")
9. ✅ Returns JSON response with success flag and links

## Summary

**✅ Done:**
- Canva alternative method configured
- Google Drive ready
- Notion API key set
- Code updated for your template style

**⚠️ Still Needed:**
- Notion database properties (Google Drive Link, DocSend Link, Status)

**Next Step:**
1. Add Notion properties
2. Share the exact property names
3. Test the workflow!


