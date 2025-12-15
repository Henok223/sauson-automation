# Testing Guide - Complete Workflow

## Prerequisites Checklist

Before testing, make sure you have:

- [ ] ✅ OAuth setup complete (`token.json` exists)
- [ ] ✅ Notion properties added (Google Drive Link, DocSend Link, Status)
- [ ] ✅ Notion API key configured
- [ ] ✅ Gemini API key configured (for headshot/map processing)
- [ ] ✅ Webhook server ready to start

## Step 1: Start the Webhook Server

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python webhook_listener.py
```

You should see:
```
 * Running on http://0.0.0.0:5001
```

**Keep this terminal open** - the server needs to be running to receive webhooks.

## Step 2: Test with a Sample Webhook

### Option A: Using curl (Terminal)

Open a **new terminal window** and run:

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test Company",
      "description": "This is a test company description",
      "location": "Los Angeles",
      "address": "Los Angeles, CA",
      "investment_date": "2024-12-01",
      "investment_stage": "PRE-SEED • Q2 2024",
      "founders": ["Founder 1", "Founder 2"],
      "co_investors": ["Investor 1", "Investor 2"],
      "background": "This is a test background description for the company."
    },
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png",
    "notion_page_id": "your_notion_page_id_here"
  }'
```

### Option B: Using a Test File

Create a file `test_payload.json`:

```json
{
  "company_data": {
    "name": "Test Company",
    "description": "This is a test company description",
    "location": "Los Angeles",
    "address": "Los Angeles, CA",
    "investment_date": "2024-12-01",
    "investment_stage": "PRE-SEED • Q2 2024",
    "founders": ["Founder 1", "Founder 2"],
    "co_investors": ["Investor 1", "Investor 2"],
    "background": "This is a test background description for the company."
  },
  "headshot_url": "https://example.com/headshot.jpg",
  "logo_url": "https://example.com/logo.png",
  "notion_page_id": "your_notion_page_id_here"
}
```

Then run:
```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d @test_payload.json
```

## Step 3: What to Watch For

### In the Server Terminal

You should see output like:
```
============================================================
Received webhook request: POST /webhook/onboarding
Company name: Test Company
============================================================

Processing headshots with Gemini...
✓ Headshots processed and combined

Generating map with Gemini...
✓ Map generated for Los Angeles

Creating Canva slide...
Canva API not configured, using alternative method...
✓ Slide created

Uploading PDF to Google Drive...
✓ Uploaded to Google Drive: https://drive.google.com/file/d/...

DocSend integration via Google Drive...
✓ DocSend will auto-sync from Google Drive

Updating Notion record...
✓ Notion record updated

============================================================
Processing complete. Success: True
============================================================
```

### Expected Response

You should get a JSON response like:
```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": null,
  "notion_page_id": "your_page_id",
  "errors": []
}
```

## Step 4: Verify Results

### 1. Check Google Drive
- Go to: https://drive.google.com
- Log in as: hmikaeltewolde@gmail.com
- Look for: `Test_Company_slide.pdf`
- ✅ File should be there with shareable link

### 2. Check DocSend
- Go to: https://www.docsend.com
- Check if the file auto-synced from Google Drive
- ✅ File should appear (may take a few moments)
- Copy the DocSend link

### 3. Check Notion
- Open your Notion database
- Find the test company record
- Check properties:
  - ✅ `Google Drive Link` should have the link
  - ⚠️ `DocSend Link` will be empty (add manually if needed)
  - ✅ `Status` should be "completed"

### 4. Check the Generated Slide
- Open the PDF from Google Drive
- Verify:
  - ✅ Orange sidebar on left
  - ✅ Dark grey background
  - ✅ Company name in orange
  - ✅ Yellow highlight boxes (Founders, Co-Investors, Background)
  - ✅ Headshot in bottom right
  - ✅ Logo in top right
  - ✅ Map in middle right (if generated)

## Step 5: Test with Real Data

Once basic test works, test with:
- Real headshot URLs (from Notion)
- Real logo URLs
- Real Notion page ID
- Real company data

## Troubleshooting

### "Google Drive upload failed"
- Check that `token.json` exists and is valid
- Re-run OAuth setup if needed
- Verify you're logged in as hmikaeltewolde@gmail.com

### "Gemini processing failed"
- Check `GEMINI_API_KEY` in `.env`
- Verify API key is valid and has quota

### "Notion update failed"
- Check `NOTION_API_KEY` in `.env`
- Verify property names match exactly
- Check that `notion_page_id` is correct

### "Slide generation failed"
- Check error message in server logs
- Verify image URLs are accessible
- Check that all required fields are provided

### DocSend link is null
- This is expected - DocSend syncs automatically
- Check DocSend manually after a few minutes
- Add the link to Notion manually if needed

## Quick Test Command

Here's a minimal test (replace with real values):

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test Co",
      "location": "LA",
      "investment_stage": "PRE-SEED • Q2 2024"
    },
    "notion_page_id": "your_page_id"
  }'
```

## Success Criteria

✅ Webhook receives request
✅ Headshots processed (or placeholder created)
✅ Map generated (or placeholder created)
✅ Slide created (PDF generated)
✅ Uploaded to Google Drive
✅ Link returned in response
✅ Notion updated with link and status

## Next Steps After Testing

Once testing works:
1. ✅ Connect to Zapier
2. ✅ Set up webhook URL in Zapier
3. ✅ Test end-to-end from Notion → Zapier → Your Server
4. ✅ Verify complete workflow

Ready to test! Start the server and send a test webhook.


