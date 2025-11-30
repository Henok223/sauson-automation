# Testing Your Webhook with Zapier

Since Zapier already handles Notion authentication, you just need to set up and test the webhook server.

## Step 1: Start Your Webhook Server

### Option A: Local Testing with ngrok (Recommended for Testing)

1. **Start the webhook server**:
   ```bash
   cd slauson-automation
   python webhook_listener.py
   ```
   You should see: `Running on http://0.0.0.0:5000`

2. **In a new terminal, start ngrok**:
   ```bash
   ngrok http 5000
   ```
   (If you don't have ngrok: https://ngrok.com/download)

3. **Copy the ngrok URL**:
   - You'll see something like: `https://abc123.ngrok.io`
   - Your webhook URL will be: `https://abc123.ngrok.io/webhook/onboarding`

### Option B: Deploy to Production

Deploy `webhook_listener.py` to:
- Heroku
- Railway
- Render
- AWS Lambda
- Any Python hosting service

Then use your production URL.

## Step 2: Update Zapier Webhook URL

1. **In your Zap**, go to the **Webhook step**
2. **Update the URL**:
   - Replace `https://your-server.com/webhook/onboarding`
   - With your actual URL (ngrok or production)
   - Example: `https://abc123.ngrok.io/webhook/onboarding`

3. **Save the step**

## Step 3: Test the Webhook

1. **In Zapier**, click **"Test"** on the webhook step
2. **Check your server logs** - you should see the request
3. **Check the response** - should return JSON with `success: true`

## Step 4: Test Full Flow

1. **Create a test entry** in your "Burton test" database:
   - Name: "Test Company"
   - Status: "Ready" (if using filter)
   - Upload a test headshot image
   - Upload a test logo image
   - Fill in other fields

2. **The Zap should trigger automatically**
3. **Check your server logs** for processing
4. **Verify results** in Notion (new page created, folder created)

## Troubleshooting

### Webhook not receiving requests
- ✅ Check server is running
- ✅ Verify ngrok is running (if using)
- ✅ Check URL in Zapier matches exactly
- ✅ Check firewall/network settings

### "Connection refused" error
- ✅ Make sure webhook server is running
- ✅ Verify port 5000 is not blocked
- ✅ Check ngrok is forwarding correctly

### Server errors
- ✅ Check `.env` file has required keys
- ✅ Verify Notion database ID is set
- ✅ Check server logs for detailed errors

### Test entry not triggering
- ✅ Make sure Status = "Ready" (if using filter)
- ✅ Verify Zap is turned ON (not just in draft)
- ✅ Check Zapier task history for errors

## Quick Test Command

Test the webhook manually:

```bash
curl -X POST http://localhost:5000/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test Company",
      "website": "https://test.com"
    },
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png"
  }'
```

## Expected Response

Your webhook should return:

```json
{
  "success": true,
  "notion_page_id": "abc123...",
  "notion_folder_id": "def456...",
  "canva_slide_path": "/tmp/slide.pdf",
  "errors": []
}
```

---

**Ready to test?** Start your server, update the Zapier webhook URL, and create a test entry!

