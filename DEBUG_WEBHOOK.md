# Debug: Did the Webhook Work?

## Quick Checks

### 1. Check if ngrok is Running

**In a terminal, run:**
```bash
ngrok http 5001
```

**Or check if it's already running:**
- Open: http://localhost:4040
- If you see the ngrok web interface, it's running
- Check the "Requests" tab to see if any requests came through

### 2. Check Server Logs

**Look at the terminal where `webhook_listener.py` is running**

You should see:
```
Received webhook request: POST /webhook/onboarding
Processing onboarding...
```

**If you see nothing:**
- The request didn't reach your server
- Likely ngrok isn't running or Zapier didn't trigger

### 3. Check Zapier Task History

1. Go to your Zap in Zapier
2. Click on the **"Task History"** tab
3. Look for the most recent task
4. Check if it shows:
   - ✅ **Success** - Request was sent
   - ❌ **Error** - Something went wrong

### 4. Verify Zap is ON

1. In Zapier, make sure your Zap is **turned ON** (not just in draft)
2. The toggle should be green/blue, not gray

### 5. Check Filter (if using)

If you have a filter step for Status = "Ready":
- Make sure your new entry has Status = "Ready"
- If Status is "Draft" or empty, the Zap won't trigger

## Common Issues

### ❌ "No requests in server logs"
**Possible causes:**
- ngrok isn't running → Start it: `ngrok http 5001`
- Zap is OFF → Turn it ON in Zapier
- Filter blocking → Check Status field
- Wrong webhook URL → Verify URL in Zapier matches ngrok URL

### ❌ "Request received but error in processing"
**Check:**
- Server logs for error messages
- `.env` file has `NOTION_API_KEY` set
- `NOTION_DATABASE_ID` is configured
- All required fields are present

### ❌ "Zapier shows error"
**Check:**
- Webhook URL is correct
- Server is running
- ngrok is running
- Network/firewall isn't blocking

## Quick Test

**Test the webhook manually:**

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test",
      "website": "https://test.com"
    },
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png"
  }'
```

If this works, the server is fine - the issue is with Zapier → ngrok → server connection.

## Next Steps

1. **Make sure ngrok is running**: `ngrok http 5001`
2. **Check Zapier task history** for errors
3. **Verify Zap is ON**
4. **Check server logs** for incoming requests
5. **Try creating another entry** with Status = "Ready"

---

**Most likely issue**: ngrok isn't running, so Zapier can't reach your server!

