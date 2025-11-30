# Quick Test Guide - Zapier Webhook

Since your Zapier → Notion connection is already working, here's the quickest way to test:

## 🚀 Quick Start (3 Steps)

### Step 1: Start Webhook Server

**Terminal 1** - Start the server:
```bash
cd slauson-automation
python webhook_listener.py
```

You should see: `Running on http://0.0.0.0:5000`

### Step 2: Start ngrok (for public URL)

**Terminal 2** - Start ngrok:
```bash
ngrok http 5000
```

Copy the **Forwarding URL** (e.g., `https://abc123.ngrok.io`)

**Don't have ngrok?** Download: https://ngrok.com/download

### Step 3: Update Zapier Webhook URL

1. In your Zap, go to the **Webhook step**
2. Update URL to: `https://YOUR-NGROK-URL.ngrok.io/webhook/onboarding`
   - Example: `https://abc123.ngrok.io/webhook/onboarding`
3. Click **"Test"** - should see success response

## ✅ Test the Full Flow

1. **Create test entry** in "Burton test" database:
   - Name: "Test Company"
   - Status: "Ready" (if using filter)
   - Upload headshot image
   - Upload logo image
   - Fill other fields

2. **Zap should trigger automatically**

3. **Check results**:
   - Server logs show processing
   - Notion database gets new entry
   - Company folder created

## 🔍 Verify It's Working

**Check server logs** - you should see:
```
Processing onboarding...
Creating Notion database entry...
Creating Notion company folder...
Generating Canva slide...
```

**Check Zapier task history** - should show:
- ✅ Notion trigger fired
- ✅ Webhook sent successfully
- ✅ Response received

**Check Notion** - should see:
- ✅ New database entry created
- ✅ Company folder/page created

## 🐛 Troubleshooting

### Webhook not receiving requests
- Check server is running (Terminal 1)
- Check ngrok is running (Terminal 2)
- Verify URL in Zapier matches ngrok URL exactly
- Check ngrok shows requests in web interface

### "Connection refused"
- Make sure both server AND ngrok are running
- Check port 5000 isn't blocked
- Try restarting both

### Server errors
- Check `.env` file exists and has `NOTION_API_KEY`
- Verify `NOTION_DATABASE_ID` is set
- Check server logs for specific errors

### Zap not triggering
- Make sure Zap is **ON** (not just in draft mode)
- Verify Status = "Ready" if using filter
- Check Zapier task history for errors

## 📝 Quick Checklist

- [ ] Webhook server running (Terminal 1)
- [ ] ngrok running (Terminal 2)
- [ ] Zapier webhook URL updated
- [ ] Webhook test successful in Zapier
- [ ] Test entry created in Notion
- [ ] Zap triggered and processed
- [ ] Results visible in Notion

---

**That's it!** Once the webhook URL is updated in Zapier, create a test entry and watch it work! 🎉

