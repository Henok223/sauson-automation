# Debug: Test Entry Not Appearing

## Quick Checks

### 1. Check Server Logs

**Look at your server terminal** where `webhook_listener.py` is running.

**Did you see:**
```
Received webhook request: POST /webhook/onboarding
```

**If YES:**
- Request reached your server
- Check for error messages below
- Look for "Processing complete" or error details

**If NO:**
- Request didn't reach your server
- Check Zapier/Zap status (see below)

### 2. Check Zapier Task History

1. Go to your Zap in Zapier
2. Click **"Task History"** tab
3. Look for the most recent task
4. Check:
   - ✅ **Success** → Request was sent (check server logs)
   - ❌ **Error** → See error message
   - ⚠️ **Skipped** → Filter might be blocking

### 3. Check Zap Status

1. In Zapier, make sure your Zap is **ON** (not just in draft)
2. The toggle should be green/blue

### 4. Check Status Field

If you have a filter for Status = "Ready":
- Make sure your test entry has **Status = "Ready"**
- If Status is "Draft" or empty → Zap won't trigger

### 5. Check ngrok

1. Open: http://localhost:4040
2. Click **"Requests"** tab
3. Do you see any requests?
   - If YES → Request reached ngrok (check server)
   - If NO → Request didn't reach ngrok (check Zapier)

## Common Issues

### Issue 1: Zap Not Triggering
**Symptoms:**
- No request in server logs
- No request in ngrok
- Zapier task history shows nothing or "Skipped"

**Solutions:**
- Make sure Zap is **ON**
- Check Status = "Ready" (if using filter)
- Verify database is shared with Zapier integration

### Issue 2: Request Reached Server But Failed
**Symptoms:**
- Request appears in server logs
- Error message in logs
- 400 or 500 error

**Solutions:**
- Check error message in server logs
- Verify all required fields are filled
- Check if Headshot/Logo files are attached

### Issue 3: Request Never Reached Server
**Symptoms:**
- No request in server logs
- Request appears in ngrok but not server

**Solutions:**
- Check server is running
- Verify ngrok is forwarding to correct port (5001)
- Check firewall/network settings

## What to Share

To help debug, share:
1. **Server logs** - What do you see in the terminal?
2. **Zapier task history** - What does it show?
3. **ngrok requests** - Any requests in http://localhost:4040?
4. **Entry details** - What Status did you set?

---

**Most likely:** Check your server terminal logs first - that will tell us exactly what happened!

