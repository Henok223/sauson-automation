# How to Check if Automation Ran

## Quick Checklist

After creating a Notion entry with Status = "Ready", check these places:

---

## 1. ✅ Check Zapier (Easiest - Start Here)

### Step 1: Open Zapier Dashboard
1. Go to: https://zapier.com/app/dashboard
2. Find your Zap (the one with Notion → Webhook → Google Drive)

### Step 2: Check Task History
1. Click on your Zap
2. Click **"Task History"** tab (or "History")
3. Look for recent tasks (should show within 30 seconds)

### What to Look For:
- ✅ **Green checkmarks** = Success
- ❌ **Red X** = Error (click to see details)
- ⏳ **In progress** = Still running

### If You See a Task:
- Click on it to see details
- Check each step:
  - Step 1: Notion trigger ✅
  - Step 2: Filter (if you have one) ✅
  - Step 3: Webhook ✅
  - Step 4: Google Drive ✅

### If No Tasks Appear:
- ⚠️ Zap might be paused - check if it's ON
- ⚠️ Status field might not be "Ready" exactly
- ⚠️ Wait a bit longer (can take up to 1 minute)

---

## 2. ✅ Check Render Logs (See What Server Did)

### Step 1: Open Render Dashboard
1. Go to: https://dashboard.render.com/
2. Click on your service: `sauson-automation-3`

### Step 2: View Logs
1. Click **"Logs"** tab
2. Look for recent activity

### What to Look For:
```
Received webhook request: POST /webhook/onboarding
Company name: TechFlow Solutions
Processing images...
Generating Canva slide...
Processing complete. Success: True
```

### If You See Errors:
- Check the error message
- Common issues:
  - Image download failed
  - Canva API error
  - Missing fields

---

## 3. ✅ Check Google Drive (See the PDF)

### Step 1: Open Google Drive
1. Go to: https://drive.google.com
2. Navigate to the folder where Zapier uploads files

### Step 2: Look for PDF
- File name: `TechFlow_Solutions_slide.pdf` (or similar)
- Should appear within 1-2 minutes

### If PDF is There:
- ✅ **Success!** Everything worked
- Open it to verify it's the correct slide

### If PDF is Missing:
- Check Zapier task history for Google Drive step errors
- Verify Google Drive folder is correct in Zapier

---

## 4. ✅ Check Notion (Verify Entry)

### Step 1: Open Your Database
1. Go to your Portfolio Companies database
2. Find the entry you created

### Step 2: Verify Data
- All fields should be filled
- Status should still be "Ready"
- Images should be attached

---

## 5. ✅ Test Webhook Directly (If Zapier Didn't Trigger)

If Zapier didn't run, test the webhook manually:

```bash
cd ~/slauson-automation
./test_and_download.sh
```

This will:
- Send test data to webhook
- Show you the response
- Download the PDF if successful

---

## Troubleshooting by Issue

### Issue: Zapier Shows No Tasks

**Check:**
1. Is Zap **ON** (not paused)?
2. Is Status field **exactly** "Ready" (case-sensitive)?
3. Did you just create the entry? (Wait 30-60 seconds)
4. Check Zapier's "Catch Up" - sometimes it needs to catch up

**Fix:**
- Turn Zap ON if paused
- Edit entry, change Status to something else, save, then change back to "Ready"
- Or create a new entry

---

### Issue: Zapier Shows Error

**Check:**
1. Click on the failed task
2. Read the error message
3. Common errors:
   - "Webhook returned 500" → Check Render logs
   - "Field not found" → Check field names match
   - "Invalid JSON" → Check webhook payload

**Fix:**
- Check Render logs for detailed error
- Verify field names in Zapier match Notion exactly
- Test webhook directly

---

### Issue: Render Logs Show Error

**Check:**
1. Open Render logs
2. Look for error messages
3. Common errors:
   - "Missing company_data" → Webhook payload issue
   - "Image download failed" → Image URL issue
   - "Canva API error" → Canva not configured (uses fallback)

**Fix:**
- Check the error message
- Verify webhook payload format
- Check if images are accessible

---

### Issue: PDF Not in Google Drive

**Check:**
1. Zapier task history - did Google Drive step succeed?
2. Check Google Drive folder path in Zapier
3. Verify Google Drive connection in Zapier

**Fix:**
- Check Zapier Google Drive step for errors
- Verify folder exists and is accessible
- Re-test the Google Drive step in Zapier

---

## Quick Status Check Commands

### Check Render Service Status
```bash
curl https://sauson-automation-3.onrender.com/health
```
Should return: `{"status":"healthy"}`

### Test Webhook
```bash
cd ~/slauson-automation
curl -X POST https://sauson-automation-3.onrender.com/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d @test_real_payload.json
```

---

## Expected Timeline

After creating Notion entry:

- **0-10 seconds:** Zapier detects new entry
- **10-30 seconds:** Zapier sends webhook
- **30-60 seconds:** Server processes (images, Canva slide)
- **60-90 seconds:** PDF uploaded to Google Drive

**Total:** Usually completes within 1-2 minutes

---

## Still Not Working?

1. **Check Zapier first** - easiest to see what happened
2. **Check Render logs** - see server-side errors
3. **Test webhook directly** - verify server is working
4. **Check Google Drive** - verify upload step worked

**Most common issue:** Status field not exactly "Ready" or Zap is paused!

---

**Start with Zapier Task History - that's the easiest way to see what happened!** 🚀

