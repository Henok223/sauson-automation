# Test Complete Flow - Final Steps

## ✅ Zapier is Configured!

Your Zap is ready with:
- **Webhook URL**: `https://blinkingly-unsuspendible-lacy.ngrok-free.dev/webhook/onboarding`
- **Method**: POST
- **Trigger**: Burton test database

## 🚀 Start Your Webhook Server

### Step 1: Start the Server

**Terminal 1** - Start the webhook server:

```bash
cd slauson-automation
source venv/bin/activate
python webhook_listener.py
```

You should see:
```
 * Running on http://0.0.0.0:5001
 * Debug mode: on
```

**Keep this terminal open!**

### Step 2: Verify ngrok is Running

**Terminal 2** - Make sure ngrok is still running:

```bash
ngrok http 5001
```

You should see:
```
Forwarding   https://blinkingly-unsuspendible-lacy.ngrok-free.dev -> http://localhost:5001
```

**Keep this terminal open too!**

## ✅ Test the Complete Flow

### Step 1: Create Test Entry in Notion

1. Open your **"Burton test"** database in Notion
2. Click **"+ New"** to create a new entry
3. Fill in:
   - **Name**: "Test Company"
   - **Status**: "Ready" (if using filter)
   - **Headshot**: Upload a test image
   - **Logo**: Upload a test image
   - Fill in other fields (Website, Description, etc.)
4. **Save** the entry

### Step 2: Watch the Magic Happen

**In your webhook server terminal**, you should see:
```
Received webhook request: POST /webhook/onboarding
Processing onboarding...
Creating Notion database entry...
Creating Notion company folder...
Generating Canva slide...
Processing complete. Success: True
```

**In Zapier**:
- Check the task history
- Should show: ✅ Webhook sent successfully
- Response should show `{"success": true, ...}`

### Step 3: Verify Results

**Check Notion**:
- New database entry created (if automation creates it)
- Company folder/page created
- All data populated

**Check Server Logs**:
- No errors
- All steps completed successfully

## 🐛 Troubleshooting

### Server not receiving requests
- ✅ Check server is running (Terminal 1)
- ✅ Check ngrok is running (Terminal 2)
- ✅ Verify URL in Zapier matches ngrok URL exactly
- ✅ Check ngrok web interface: http://localhost:4040

### "Connection refused" or timeout
- ✅ Make sure both server AND ngrok are running
- ✅ Check port 5001 is correct
- ✅ Try restarting both

### Server errors
- ✅ Check `.env` file has `NOTION_API_KEY`
- ✅ Verify `NOTION_DATABASE_ID` is set
- ✅ Check server logs for specific errors

### Zap not triggering
- ✅ Make sure Zap is **ON** (not just in draft mode)
- ✅ Verify Status = "Ready" if using filter
- ✅ Check Zapier task history for errors

## 📋 Quick Checklist

- [ ] Webhook server running (Terminal 1)
- [ ] ngrok running (Terminal 2)
- [ ] Zapier webhook URL updated
- [ ] Test entry created in Notion
- [ ] Status = "Ready" (if using filter)
- [ ] Headshot and Logo files attached
- [ ] Zap triggered automatically
- [ ] Server logs show processing
- [ ] Results visible in Notion

## 🎯 Expected Payload Structure

Your server will receive:

```json
{
  "company_data": {
    "name": "Test Company",
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

## 🎉 You're Ready!

Once both the server and ngrok are running:
1. Create a test entry in Notion
2. Watch the automation happen!
3. Check results in Notion and server logs

---

**Everything is configured!** Just start the server and test it! 🚀

