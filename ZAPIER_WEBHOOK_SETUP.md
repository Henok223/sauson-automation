# Zapier Webhook Setup - Quick Guide

## Yes! It Works with Zapier ✅

Your webhook endpoint is already set up to receive requests from Zapier. Here's how to connect them:

## Step 1: Expose Your Server (Choose One)

### Option A: Use ngrok (For Local Testing)

1. **Install ngrok** (if not already):
   ```bash
   brew install ngrok
   # OR download from https://ngrok.com/
   ```

2. **Start your webhook server**:
   ```bash
   python webhook_listener.py
   ```

3. **In a new terminal, start ngrok**:
   ```bash
   ngrok http 5001
   ```

4. **Copy the ngrok URL** (looks like: `https://abc123.ngrok.io`)

### Option B: Deploy to Production (Recommended for Production)

Deploy your server to:
- Railway
- Render
- Heroku
- AWS
- Or any hosting service

Then use your production URL.

## Step 2: Set Up Zapier Webhook

### In Zapier:

1. **Create a new Zap**
2. **Trigger**: Choose your trigger (e.g., "Notion - New Database Item")
3. **Action**: Choose "Webhooks by Zapier" → "POST"

### Webhook Configuration:

- **URL**: 
  - For ngrok: `https://your-ngrok-url.ngrok.io/webhook/onboarding`
  - For production: `https://your-server.com/webhook/onboarding`
  
- **Method**: `POST`

- **Headers**:
  ```
  Content-Type: application/json
  ```

- **Data (JSON)**:
  ```json
  {
    "company_data": {
      "name": "{{1.Name}}",
      "description": "{{1.Description}}",
      "location": "{{1.Address}}",
      "address": "{{1.Address}}",
      "investment_date": "{{1.Investment Date}}",
      "investment_stage": "{{1.Investment Stage}}",
      "founders": "{{1.Founders}}",
      "co_investors": "{{1.Co-Investors}}",
      "background": "{{1.Background}}"
    },
    "headshot_url": "{{1.Headshot}}",
    "logo_url": "{{1.Logo}}",
    "notion_page_id": "{{1.ID}}"
  }
  ```

**Note**: Replace `{{1.FieldName}}` with your actual Notion field names from Zapier.

## Step 3: Field Mapping

Map your Notion fields to the webhook payload:

- `{{1.Name}}` → Company name
- `{{1.Description}}` → Description
- `{{1.Address}}` or `{{1.Location}}` → Location
- `{{1.Investment Stage}}` → Investment stage
- `{{1.Founders}}` → Founders
- `{{1.Co-Investors}}` → Co-investors
- `{{1.Background}}` → Background
- `{{1.Headshot}}` → Headshot URL
- `{{1.Logo}}` → Logo URL
- `{{1.ID}}` → Notion page ID (for updating the record)

## Step 4: Test the Zap

1. **Test Trigger**: Create a test entry in Notion
2. **Test Webhook**: Zapier sends data to your server
3. **Check Server Logs**: Should see processing steps
4. **Verify Results**: Check Google Drive, DocSend, Notion

## What Happens

1. **Zapier triggers** when new Notion entry is created
2. **Zapier sends webhook** to your server with company data
3. **Your server processes**:
   - Downloads & processes images
   - Generates map
   - Creates slide
   - Uploads to Google Drive
   - Updates Notion
4. **Returns response** to Zapier with success + links

## Webhook Response

Your server returns:
```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": null,
  "notion_page_id": "...",
  "errors": []
}
```

Zapier can use this response in subsequent steps if needed.

## Quick Setup Summary

1. **Start server**: `python webhook_listener.py`
2. **Start ngrok**: `ngrok http 5001` (for local testing)
3. **Get ngrok URL**: Copy the HTTPS URL
4. **In Zapier**: Set webhook URL to `https://your-ngrok-url.ngrok.io/webhook/onboarding`
5. **Map Notion fields** to webhook payload
6. **Test!**

## Production Deployment

For production, deploy your server and use the production URL instead of ngrok.

The webhook endpoint is: `/webhook/onboarding` (POST method)

Ready to connect Zapier! 🚀


