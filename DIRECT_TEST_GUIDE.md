# Direct Webhook Testing Guide

## Test Without Zapier! 🚀

If Zapier isn't triggering, you can test the webhook directly.

---

## Quick Test (Easiest)

### Step 1: Make Sure Server is Running

```bash
# In terminal 1
cd /Users/henoktewolde/slauson-automation
python webhook_listener.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 2: Run Test Script

```bash
# In terminal 2 (new terminal)
cd /Users/henoktewolde/slauson-automation
python test_webhook_direct.py
```

This will:
- ✅ Send a test payload to your webhook
- ✅ Show you the response
- ✅ Test if everything is working

---

## Manual Test with curl

If you prefer curl:

```bash
curl -X POST http://localhost:5000/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data__name": "Test Company",
    "company_data__description": "A test company description",
    "company_data__address": "Los Angeles, CA",
    "company_data__investment_date": "2024-03-15",
    "company_data__investment_round": "PRE-SEED",
    "company_data__founders": "John Doe, Jane Smith",
    "company_data__co_investors": "Investor A, Investor B",
    "company_data__background": "Test background information",
    "headshot_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
    "logo_url": "https://images.unsplash.com/photo-1611262588024-d12430b98920?w=400",
    "notion_page_id": "test-123",
    "status": "pending"
  }'
```

---

## Test with ngrok (If Testing from Another Machine)

If you want to test from another computer or share the URL:

### Step 1: Start Server
```bash
python webhook_listener.py
```

### Step 2: Start ngrok (in new terminal)
```bash
ngrok http 5000
```

### Step 3: Use ngrok URL
```bash
# Copy the ngrok URL (e.g., https://abc123.ngrok.io)
# Then test with:
python test_webhook_direct.py https://abc123.ngrok.io/webhook/onboarding
```

---

## What to Check if Nothing Happens

### 1. Is Server Running?
```bash
# Check if port 5000 is in use
lsof -i :5000
```

### 2. Check Server Logs
Look at the terminal where `webhook_listener.py` is running. You should see:
- `Received webhook request: POST /webhook/onboarding`
- Processing steps
- Any errors

### 3. Check Environment Variables
```bash
# Make sure .env file exists and has all keys
cat .env
```

Required:
- `GEMINI_API_KEY`
- `GOOGLE_DRIVE_CREDENTIALS_JSON` or `GOOGLE_SERVICE_ACCOUNT_PATH`
- `NOTION_API_KEY`
- `CANVA_API_KEY` (optional)
- `CANVA_TEMPLATE_ID` (optional)

### 4. Test Health Endpoint
```bash
curl http://localhost:5000/health
```

Should return: `{"status": "healthy"}`

---

## Expected Response

When test succeeds, you should see:

```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": "https://docsend.com/view/..." (if API key set),
  "notion_page_id": "test-123",
  "errors": []
}
```

---

## Troubleshooting Zapier Issues

If direct test works but Zapier doesn't:

### 1. Check Zapier Webhook URL
- Make sure it's correct: `https://your-ngrok-url.ngrok.io/webhook/onboarding`
- Or production URL if deployed

### 2. Check Zapier Trigger
- Is trigger set to "New Database Item"?
- Did you test the trigger in Zapier?
- Is the Zap turned ON?

### 3. Check Zapier Filter
- If you have a filter, make sure Status = `Ready` (or whatever you set)
- Try removing filter for testing

### 4. Check Notion Connection
- Is Notion database shared with Zapier?
- Go to Notion → Database → "..." → "Connections" → Add Zapier

### 5. Check Zapier Logs
- Go to Zapier → Your Zap → "Task History"
- Look for errors or failed tasks

---

## Quick Debug Checklist

- [ ] Server is running (`python webhook_listener.py`)
- [ ] Can access health endpoint (`curl http://localhost:5000/health`)
- [ ] Direct test works (`python test_webhook_direct.py`)
- [ ] Environment variables are set (`.env` file)
- [ ] Zapier webhook URL is correct
- [ ] Zapier trigger is tested and working
- [ ] Zap is turned ON in Zapier
- [ ] Notion database is shared with Zapier

---

## Next Steps

1. **Test directly first** - Use `test_webhook_direct.py` to verify server works
2. **Check server logs** - See what's happening
3. **Fix any errors** - Based on logs
4. **Then test Zapier** - Once direct test works

---

## Need Help?

If direct test fails:
1. Check server logs for errors
2. Verify all environment variables
3. Make sure images can be downloaded (test URLs work)
4. Check Google OAuth is set up (`token.json` exists)

If direct test works but Zapier doesn't:
1. Verify Zapier webhook URL
2. Check Zapier task history
3. Test Zapier trigger separately
4. Check Notion connection in Zapier


