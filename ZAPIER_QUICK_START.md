# Zapier Quick Start for DocSend Integration

## 🎯 Recommended Zapier Template

**Use this 3-step workflow:**

### Step 1: Trigger - Notion
- **App**: Notion
- **Event**: "New Database Item"
- **Database**: Your Portfolio Companies database

### Step 2: Action - Webhook (Trigger Automation)
- **App**: Webhooks by Zapier
- **Event**: "POST"
- **URL**: Your webhook endpoint (see below)
- **Payload**: Company data from Notion

### Step 3: Action - DocSend Upload
- **Option A**: If DocSend Zapier app exists → Use "Upload Document"
- **Option B**: Use "Webhooks by Zapier" → POST to DocSend API

---

## 📋 Exact Zapier Setup

### Step 1: Notion Trigger

1. In Zapier, choose **Notion** as trigger app
2. Select **"New Database Item"** event
3. Connect your Notion account
4. Select **"Portfolio Companies"** database
5. Test: Create a test entry in Notion

### Step 2: Webhook to Your Automation

1. Add action: **Webhooks by Zapier**
2. Choose **"POST"** event
3. **URL**: 
   - Local: `http://localhost:5000/webhook/onboarding` (use ngrok for testing)
   - Production: `https://your-domain.com/webhook/onboarding`
4. **Method**: POST
5. **Data (JSON)**:
   ```json
   {
     "company_data": {
       "name": "{{1.Name}}",
       "website": "{{1.Website}}",
       "description": "{{1.Description}}",
       "address": "{{1.Address}}",
       "investment_date": "{{1.Investment Date}}",
       "co_investors": "{{1.Co-Investors}}",
       "num_employees": {{1.Number of Employees}},
       "first_time_founder": {{1.First Time Founder}},
       "investment_memo_link": "{{1.Investment Memo}}"
     },
     "headshot_url": "{{1.Headshot}}",
     "logo_url": "{{1.Logo}}"
   }
   ```
6. **Note**: Field names (like `{{1.Name}}`) must match your Notion database property names exactly

### Step 3: DocSend Upload

**If DocSend Zapier App Exists:**
1. Add action: **DocSend**
2. Choose **"Upload Document"**
3. **File**: Use the PDF from step 2 response
4. **Name**: `{{1.Name}} Portfolio Slide`

**If No DocSend App (Use HTTP Request):**
1. Add action: **Webhooks by Zapier** → **"POST"**
2. **URL**: `https://api.docsend.com/documents`
3. **Method**: POST
4. **Headers**:
   ```
   Authorization: Bearer YOUR_DOCSEND_API_KEY
   ```
5. **Body Type**: Form Data
6. **Data**:
   - `file`: PDF file from step 2
   - `name`: `{{1.Name}} Portfolio Slide`

---

## 🔧 Testing Locally

### Option 1: Use ngrok (Recommended)

1. Install ngrok: https://ngrok.com/download
2. Start your webhook server:
   ```bash
   python webhook_listener.py
   ```
3. In another terminal, start ngrok:
   ```bash
   ngrok http 5000
   ```
4. Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)
5. Use this URL in Zapier webhook: `https://abc123.ngrok.io/webhook/onboarding`

### Option 2: Deploy to Server

Deploy `webhook_listener.py` to:
- Heroku
- Railway
- Render
- AWS Lambda
- Any Python hosting service

---

## 📝 Field Mapping Reference

Your Notion database should have these properties (adjust in Zapier if different):

| Notion Property | Zapier Field | Example |
|----------------|--------------|---------|
| Name | `{{1.Name}}` | "Acme Corp" |
| Website | `{{1.Website}}` | "https://acme.com" |
| Description | `{{1.Description}}` | "A great company" |
| Address | `{{1.Address}}` | "123 Main St" |
| Investment Date | `{{1.Investment Date}}` | "2024-12-01" |
| Co-Investors | `{{1.Co-Investors}}` | ["Investor A"] |
| Number of Employees | `{{1.Number of Employees}}` | 25 |
| First Time Founder | `{{1.First Time Founder}}` | true |
| Investment Memo | `{{1.Investment Memo}}` | "https://..." |
| Headshot | `{{1.Headshot}}` | File URL |
| Logo | `{{1.Logo}}` | File URL |

**Important**: Check your actual Notion property names and use those exact names in Zapier!

---

## ✅ Testing Checklist

- [ ] Notion trigger fires when new entry created
- [ ] Webhook receives data (check webhook logs)
- [ ] Automation processes successfully
- [ ] PDF is generated
- [ ] DocSend upload works
- [ ] Notion entry updated (if step 4 added)

---

## 🐛 Common Issues

### "Field not found" in Zapier
- Check property names match exactly (case-sensitive)
- Use Zapier's field picker to select fields

### Webhook returns error
- Check server is running
- Verify URL is correct
- Check webhook logs for details

### Files not uploading
- Notion file URLs work automatically
- If using base64, ensure proper encoding
- Check file size limits

### DocSend upload fails
- Verify API key is correct
- Check DocSend API documentation
- Ensure file format is PDF

---

## 🚀 Production Setup

1. **Deploy webhook server** to production
2. **Update Zapier webhook URL** to production URL
3. **Add error handling** in Zapier (use "Filter" or "Code" steps)
4. **Set up monitoring** for webhook failures
5. **Test with real data** before going live

---

## 📚 Additional Resources

- Zapier Webhooks: https://zapier.com/apps/webhook/help
- DocSend API: Check DocSend documentation
- Notion API: https://developers.notion.com

---

**Quick Answer**: Use **"Webhooks by Zapier"** → **"POST"** action to send data to your automation, then another **"POST"** action to upload to DocSend API.

