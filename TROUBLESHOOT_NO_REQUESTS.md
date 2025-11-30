# Troubleshooting: No Requests Appearing

Your server is running, but no requests are coming through. Let's check:

## ✅ Server Status: RUNNING
Your server is listening on port 5001 - that's good!

## 🔍 Check These Things

### 1. Is ngrok Running?

**Check if ngrok is running:**
- Open: http://localhost:4040
- If you see the ngrok web interface → ✅ ngrok is running
- If you get "connection refused" → ❌ ngrok is NOT running

**If ngrok is NOT running:**
```bash
ngrok http 5001
```

**Keep ngrok running in a separate terminal!**

### 2. Is Your Zap ON?

1. Go to Zapier
2. Find your Zap
3. Check if the toggle is **ON** (green/blue)
   - If it's gray → Turn it ON
   - If it's ON → Check task history

### 3. Check Zapier Task History

1. In Zapier, click on your Zap
2. Click **"Task History"** tab
3. Look for the most recent task
4. Check:
   - ✅ **Success** → Request was sent (check ngrok)
   - ❌ **Error** → See error message
   - ⚠️ **Skipped** → Filter might be blocking

### 4. Check Your Filter (if using)

If you have a filter step for Status = "Ready":
- Make sure your test entry has **Status = "Ready"**
- If Status is "Draft" or empty → Zap won't trigger

### 5. Verify Webhook URL in Zapier

In your Zap webhook step, make sure the URL is:
```
https://blinkingly-unsuspendible-lacy.ngrok-free.dev/webhook/onboarding
```

**Important:** 
- Must match your current ngrok URL exactly
- If ngrok restarted, the URL might have changed
- Check ngrok terminal for current URL

### 6. Test the Connection Manually

**Test if your server can receive requests:**

In a **new terminal**, run:
```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{"company_data": {"name": "Manual Test"}, "headshot_url": "https://example.com/h.jpg", "logo_url": "https://example.com/l.png"}'
```

**In your server terminal**, you should see:
```
Received webhook request: POST /webhook/onboarding
```

If this works but Zapier doesn't → Issue is with ngrok or Zapier

## 🎯 Most Likely Issues

### Issue 1: ngrok Not Running
**Solution:** Start ngrok in a separate terminal:
```bash
ngrok http 5001
```

### Issue 2: Zap is OFF
**Solution:** Turn the Zap ON in Zapier

### Issue 3: Filter Blocking
**Solution:** Make sure test entry has Status = "Ready"

### Issue 4: Wrong ngrok URL
**Solution:** Check current ngrok URL and update Zapier

## 📋 Quick Checklist

- [ ] Server running (✅ You have this)
- [ ] ngrok running (check http://localhost:4040)
- [ ] Zap is ON in Zapier
- [ ] Test entry has Status = "Ready" (if using filter)
- [ ] Webhook URL in Zapier matches current ngrok URL
- [ ] Check Zapier task history for errors

## 🧪 Test Steps

1. **Make sure ngrok is running**: `ngrok http 5001`
2. **Verify Zap is ON** in Zapier
3. **Create test entry** with Status = "Ready"
4. **Watch server terminal** for incoming request
5. **Check ngrok web interface** (http://localhost:4040) - Requests tab

---

**Most common issue:** ngrok isn't running, so Zapier can't reach your server!

