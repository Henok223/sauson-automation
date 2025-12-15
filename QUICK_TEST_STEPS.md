# Quick Test Steps

## Step 1: Complete OAuth Authorization

If you haven't run the OAuth setup script yet:

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python setup_google_oauth.py
```

This will:
- Open a browser
- Ask you to sign in with hmikaeltewolde@gmail.com
- Request Google Drive access
- Save token to `token.json`

**If you already did this, skip to Step 2.**

## Step 2: Start the Webhook Server

Open a terminal and run:

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python webhook_listener.py
```

You should see:
```
 * Running on http://0.0.0.0:5001
```

**Keep this terminal open!** The server needs to stay running.

## Step 3: Send a Test Webhook

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
      "co_investors": ["Investor 1"],
      "background": "This is a test background description for the company."
    },
    "headshot_url": "https://via.placeholder.com/400x400",
    "logo_url": "https://via.placeholder.com/200x200",
    "notion_page_id": "your_notion_page_id_here"
  }'
```

**Replace `your_notion_page_id_here`** with a real Notion page ID from your database.

## Step 4: Watch the Server Output

In the server terminal, you should see:
```
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

✓ Processing complete!
```

## Step 5: Check Results

### Check Google Drive
1. Go to: https://drive.google.com
2. Log in as: hmikaeltewolde@gmail.com
3. Look for: `Test_Company_slide.pdf`
4. ✅ File should be there!

### Check DocSend
1. Go to: https://www.docsend.com
2. Check if file auto-synced (may take a few minutes)
3. ✅ File should appear

### Check Notion
1. Open your database
2. Find the test company record
3. Check:
   - ✅ `Google Drive Link` has the link
   - ✅ `Status` = "completed"

## Step 6: Verify the Slide

Open the PDF from Google Drive and verify:
- ✅ Orange sidebar on left
- ✅ Dark grey background
- ✅ Company name in orange
- ✅ Yellow highlight boxes
- ✅ Images positioned correctly

## Troubleshooting

**"token.json not found"**
- Run: `python setup_google_oauth.py`

**"Google Drive upload failed"**
- Check that token.json exists
- Verify you authorized with hmikaeltewolde@gmail.com

**"Notion update failed"**
- Check property names match exactly
- Verify notion_page_id is correct

## Success!

If everything works:
- ✅ Slide generated
- ✅ Uploaded to Google Drive
- ✅ Notion updated
- ✅ Ready for production!


