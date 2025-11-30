# Connect Zapier to Your Automation Server

Your Zapier webhook is tested and working! Now let's connect it to your real automation server.

## ✅ Current Status

- ✅ Zapier → Notion connection working
- ✅ Webhook payload properly formatted
- ✅ Test server (httpbin.org) receiving data successfully

## 🚀 Connect to Your Server

### Step 1: Start Your Webhook Server

**Terminal 1** - Start the server:
```bash
cd slauson-automation
python webhook_listener.py
```

You should see: `Running on http://0.0.0.0:5000`

### Step 2: Get Public URL (for testing)

**Terminal 2** - Start ngrok:
```bash
ngrok http 5000
```

Copy the **Forwarding URL** (e.g., `https://abc123.ngrok.io`)

**For production**, deploy to:
- Heroku
- Railway  
- Render
- AWS Lambda
- Any Python hosting service

### Step 3: Update Zapier Webhook URL

1. **In your Zap**, go to the **Webhook step**
2. **Update the URL**:
   - **From**: `https://httpbin.org/post` (test URL)
   - **To**: `https://YOUR-NGROK-URL.ngrok.io/webhook/onboarding`
   - Example: `https://abc123.ngrok.io/webhook/onboarding`

3. **Save the step**

### Step 4: Test the Connection

1. **In Zapier**, click **"Test"** on the webhook step
2. **Check your server logs** - you should see:
   ```
   Received webhook request: POST /webhook/onboarding
   Processing onboarding...
   Creating Notion database entry...
   ```
3. **Check the response** - should return JSON with `success: true`

## ✅ Test with Real Entry

1. **Create a new entry** in your "Burton test" database:
   - Name: "Real Test Company"
   - Status: "Ready" (if using filter)
   - Upload actual headshot image
   - Upload actual logo image
   - Fill in all fields:
     - Website
     - Description
     - Address
     - Investment Date
     - Co-Investors
     - Number of Employees
     - First Time Founder
     - Investment Memo

2. **The Zap should trigger automatically**

3. **Check results**:
   - ✅ Server logs show processing
   - ✅ New Notion page created (if configured)
   - ✅ Company folder created (if configured)
   - ✅ PDF generated (if Canva configured)
   - ✅ DocSend upload (if configured)

## 📋 Expected Payload Structure

Your webhook receives this structure from Zapier:

```json
{
  "company_data": {
    "name": "Burton Test Entry",
    "website": "https://example.com",
    "description": "[Notion page content]",
    "address": "Test Address",
    "investment_date": "[Notion timestamp]",
    "co_investors": "Test Investors",
    "num_employees": "10",
    "first_time_founder": "false",
    "investment_memo_link": "https://example.com/memo"
  },
  "headshot_url": "https://notion.so/file/...",
  "logo_url": "https://notion.so/file/...",
  "notion_page_id": "[actual page ID]",
  "notion_created_time": "[timestamp]",
  "notion_last_edited": "[timestamp]"
}
```

The webhook automatically:
- ✅ Handles Notion file URLs (downloads files)
- ✅ Processes images (background removal, grayscale)
- ✅ Creates Notion entries
- ✅ Generates slides
- ✅ Uploads to DocSend (if configured)

## 🔍 Verify It's Working

### Check Server Logs

You should see:
```
Received webhook request: POST /webhook/onboarding
Processing images...
Creating Notion database entry...
Creating Notion company folder...
Generating Canva slide...
Processing complete. Success: True
```

### Check Zapier Task History

- ✅ Notion trigger fired
- ✅ Webhook sent successfully
- ✅ Response received with `success: true`

### Check Notion

- ✅ New database entry created (if automation creates it)
- ✅ Company folder/page created
- ✅ All data populated correctly

## 🐛 Troubleshooting

### Server not receiving requests
- ✅ Check server is running (Terminal 1)
- ✅ Check ngrok is running (Terminal 2)
- ✅ Verify URL in Zapier matches ngrok URL exactly
- ✅ Check ngrok web interface shows requests

### "Connection refused" or timeout
- ✅ Make sure both server AND ngrok are running
- ✅ Check port 5000 isn't blocked
- ✅ Try restarting both
- ✅ Check firewall settings

### Server errors
- ✅ Check `.env` file has `NOTION_API_KEY`
- ✅ Verify `NOTION_DATABASE_ID` is set
- ✅ Check server logs for specific errors
- ✅ Verify file downloads work (headshot/logo URLs)

### Automation not completing
- ✅ Check all required fields are provided
- ✅ Verify images are accessible (Notion file URLs)
- ✅ Check API keys are valid
- ✅ Review error messages in response

## 📝 Quick Checklist

- [ ] Webhook server running (Terminal 1)
- [ ] ngrok running (Terminal 2)
- [ ] Zapier webhook URL updated (from httpbin to your server)
- [ ] Webhook test successful in Zapier
- [ ] Real entry created in Notion database
- [ ] Status = "Ready" (if using filter)
- [ ] Headshot and Logo files attached
- [ ] Zap triggered and processed
- [ ] Results visible in server logs
- [ ] Results visible in Notion (if creating entries)

## 🎯 Next Steps

Once everything is working:

1. **Deploy to production** (replace ngrok with real server)
2. **Update Zapier URL** to production endpoint
3. **Set up monitoring** for webhook failures
4. **Add error notifications** in Zapier (optional)
5. **Test with multiple entries** to ensure reliability

---

**You're almost there!** Just update the webhook URL in Zapier and test with a real entry! 🚀

