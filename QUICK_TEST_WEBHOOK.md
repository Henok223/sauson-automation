# Quick Test Guide - Webhook Payload

## ✅ Your Payload Format is Supported!

Your Zapier webhook payload format is **perfect** and ready to test:

```json
{
  "company_data__name": "{{Name}}",
  "company_data__description": "{{Description 1}}",
  "company_data__address": "{{Location}}",
  "company_data__investment_date": "{{Investment Date 1}}",
  "company_data__investment_round": "{{Investment Stage}}",
  "company_data__founders": "{{Founders}}",
  "company_data__co_investors": "{{Co-Investors 1}}",
  "company_data__background": "{{Background}}",
  "headshot_url": "{{headshot_url}}",
  "logo_url": "{{logo_url}}",
  "notion_page_id": "{{Notion ID}}",
  "notion_created_time": "{{Created time}}",
  "notion_last_edited": "{{Last edited time}}",
  "status": "{{Status}}"
}
```

## What the Code Does

✅ **Extracts company data** from `company_data__*` fields  
✅ **Handles headshot_url and logo_url** at top level  
✅ **Converts comma-separated founders/co_investors** to lists  
✅ **Stores Notion metadata** for later updates  

## Pre-Test Checklist

Before testing, make sure:

- [ ] **Server is running** (`python webhook_listener.py` or `./start_server.sh`)
- [ ] **ngrok is running** (if testing locally) - exposes your local server
- [ ] **Environment variables are set** (`.env` file with all API keys)
- [ ] **Notion database has**:
  - [ ] `headshot_url` property (File type) with image uploaded
  - [ ] `logo_url` property (File type) with image uploaded
  - [ ] `Google Drive Link` property (URL type)
  - [ ] `DocSend Link` property (URL type)  
  - [ ] `Status` property (Select or Text type)
- [ ] **Google OAuth is set up** (`token.json` exists)
- [ ] **Canva template ID** is in `.env` (or using alternative method)

## Testing Steps

### Option 1: Test with Zapier (Recommended)

1. **Set up Zapier webhook** with the payload format above
2. **Trigger from Notion** (when a new entry is created or updated)
3. **Check server logs** for processing steps
4. **Check Notion database** - should see:
   - Google Drive link populated
   - DocSend link populated (if API key set, or via Google Drive sync)
   - Status set to "completed"

### Option 2: Test Manually with curl

```bash
curl -X POST http://localhost:5000/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data__name": "Test Company",
    "company_data__description": "A test company description",
    "company_data__address": "Los Angeles, CA",
    "company_data__investment_date": "2024-01-15",
    "company_data__investment_round": "PRE-SEED",
    "company_data__founders": "John Doe, Jane Smith",
    "company_data__co_investors": "Investor A, Investor B",
    "company_data__background": "Company background information",
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png",
    "notion_page_id": "test-page-id-123",
    "status": "pending"
  }'
```

## Expected Response

```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": "https://docsend.com/view/..." (if API key set),
  "notion_page_id": "test-page-id-123",
  "errors": []
}
```

## What Happens During Processing

1. ✅ **Receives webhook** with your flat format
2. ✅ **Extracts company data** from `company_data__*` fields
3. ✅ **Downloads headshot and logo** from URLs
4. ✅ **Processes headshots** with Gemini (background removal, greyscale, combine)
5. ✅ **Generates map** with Gemini based on location
6. ✅ **Creates Canva slide** (API or alternative method)
7. ✅ **Uploads PDF to Google Drive** (returns shareable link)
8. ✅ **Uploads to DocSend** (if API key set, or syncs from Google Drive)
9. ✅ **Updates Notion** with links and status
10. ✅ **Returns JSON response** to Zapier

## Troubleshooting

### If you get "Missing company_data" error:
- ✅ **Fixed!** Code now handles flat format automatically

### If founders/co_investors aren't working:
- ✅ **Fixed!** Code automatically converts comma-separated strings to lists

### If images don't download:
- Check that `headshot_url` and `logo_url` are valid URLs
- Check server logs for download errors

### If Notion update fails:
- Check that `notion_page_id` is correct
- Check that property names match exactly:
  - `Google Drive Link` (or `Drive Link`, `PDF Link`, `Slide Link`)
  - `DocSend Link` (or `DocSend`, `Presentation Link`)
  - `Status` (Select or Text type)

## Ready to Test! 🚀

Your payload format is **100% compatible**. Just make sure:
1. Server is running
2. All environment variables are set
3. Notion database has required properties
4. Images are uploaded to Notion

Then trigger from Zapier and watch the magic happen! ✨


