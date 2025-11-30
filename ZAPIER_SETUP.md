# Zapier Integration Guide

## DocSend Integration via Zapier

### Recommended Zapier Template/Workflow

Since Zapier doesn't have a direct "DocSend" app, you have a few options:

### Option 1: Webhook → DocSend (Recommended)

**Zap Template Structure:**

1. **Trigger: Notion** (when new database entry is created)
   - App: Notion
   - Event: "New Database Item"
   - Database: Your Portfolio Companies database
   - Filter: Only when certain fields are filled (optional)

2. **Action: Webhook** (send data to your automation)
   - App: Webhooks by Zapier
   - Event: "POST"
   - URL: `https://your-server.com/webhook/onboarding` (or localhost for testing)
   - Method: POST
   - Data: JSON payload with company data

3. **Action: DocSend** (upload the generated slide)
   - App: DocSend (if available) OR use "HTTP Request" action
   - If DocSend app exists: Upload document
   - If not: Use "HTTP Request" to call DocSend API

### Option 2: Form → Automation → DocSend

**Zap Template Structure:**

1. **Trigger: Notion Form** (when form is submitted)
   - App: Notion
   - Event: "New Database Item" (from form submission)

2. **Action: Webhook** (trigger automation)
   - App: Webhooks by Zapier
   - Event: "POST"
   - URL: Your webhook endpoint
   - Payload: Company data + file URLs

3. **Action: DocSend Upload** (after automation completes)
   - Wait for webhook response
   - Upload PDF to DocSend

---

## Step-by-Step Zapier Setup

### Step 1: Create the Zap

1. Go to https://zapier.com
2. Click "Create Zap"
3. Name it: "Slauson Portfolio Onboarding"

### Step 2: Set Up Trigger

**Choose: Notion → New Database Item**

- **Account**: Connect your Notion account
- **Database**: Select "Portfolio Companies" database
- **Filter**: (Optional) Only trigger when "Status" = "Ready" or similar

**Test the trigger:**
- Create a test entry in your Notion database
- Zapier should detect it

### Step 3: Set Up Webhook Action

**Choose: Webhooks by Zapier → POST**

- **URL**: 
  - For local testing: Use ngrok or similar: `https://your-ngrok-url.ngrok.io/webhook/onboarding`
  - For production: Your deployed server URL
- **Method**: POST
- **Data Pass-Through**: No
- **Headers**: 
  ```
  Content-Type: application/json
  ```
- **Data (JSON)**: 
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

**Note**: Adjust field names to match your Notion database properties.

### Step 4: Handle File Uploads

If your Notion database has file fields (headshot, logo), you have two options:

**Option A: Download files in Zapier first**
- Add step: "Code by Zapier" or "Formatter" to download files
- Convert to base64
- Include in webhook payload

**Option B: Send file URLs and download in automation**
- Send Notion file URLs in webhook
- Your automation downloads them
- Process as normal

### Step 5: DocSend Upload (After Automation)

**Option A: If DocSend Zapier App Exists**

Add another step:
- **App**: DocSend
- **Event**: Upload Document
- **File**: Use the PDF URL from webhook response
- **Name**: "{{company_name}} Portfolio Slide"

**Option B: Use HTTP Request to DocSend API**

Add step:
- **App**: Webhooks by Zapier → POST
- **URL**: `https://api.docsend.com/documents`
- **Method**: POST
- **Headers**:
  ```
  Authorization: Bearer YOUR_DOCSEND_API_KEY
  Content-Type: multipart/form-data
  ```
- **Body**: Upload the PDF file from previous step

---

## Complete Zapier Workflow Example

```
┌─────────────────┐
│  Notion Trigger │  New database entry created
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Webhook POST   │  Send to automation server
│  (Trigger Auto)  │  /webhook/onboarding
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Wait for       │  Wait for automation to complete
│  Response       │  (Get PDF URL back)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  DocSend Upload │  Upload PDF to DocSend
│  (HTTP Request) │  Update master deck
└─────────────────┘
```

---

## Webhook Payload Format

Your automation expects this format:

```json
{
  "company_data": {
    "name": "Acme Corp",
    "website": "https://acme.com",
    "description": "A great company",
    "address": "123 Main St, SF, CA",
    "investment_date": "2024-12-01",
    "co_investors": ["Investor A", "Investor B"],
    "num_employees": 25,
    "first_time_founder": false,
    "investment_memo_link": "https://drive.google.com/..."
  },
  "headshot": "base64_encoded_image_or_url",
  "logo": "base64_encoded_image_or_url"
}
```

**Or with URLs:**

```json
{
  "company_data": { ... },
  "headshot_url": "https://notion.so/file/...",
  "logo_url": "https://notion.so/file/..."
}
```

---

## Updated Webhook Handler

I'll update the webhook listener to handle both formats (base64 and URLs).

---

## Testing Your Zap

1. **Test Trigger**: Create a test entry in Notion
2. **Test Webhook**: Check that data reaches your server
3. **Test Automation**: Verify PDF is generated
4. **Test DocSend**: Confirm upload works

---

## Alternative: Zapier → Make.com Hybrid

If Zapier doesn't have DocSend, you can:
1. Use Zapier for Notion → Webhook
2. Use Make.com for Webhook → DocSend
3. Chain them together

---

## DocSend API Integration (If No Zapier App)

If there's no DocSend Zapier app, use the HTTP Request action:

**Endpoint**: `https://api.docsend.com/documents`

**Headers**:
```
Authorization: Bearer YOUR_DOCSEND_API_KEY
Content-Type: multipart/form-data
```

**Body**:
- `file`: The PDF file
- `name`: Document name
- `folder_id`: (Optional) Folder to upload to

**For updating master deck**:
- Use PUT request to: `https://api.docsend.com/documents/{document_id}`
- Include the merged PDF

---

## Recommended Zapier Template

**Template Name**: "Portfolio Company Onboarding"

**Steps**:
1. Trigger: Notion - New Database Item
2. Action: Webhooks - POST (to your automation)
3. Action: Webhooks - POST (to DocSend API) OR DocSend app if available

**Filters** (Optional):
- Only run when "Status" field = "Ready to Process"
- Only run when required fields are filled

---

## Next Steps

1. Set up your webhook server (or use ngrok for testing)
2. Create the Zap in Zapier
3. Test with a sample entry
4. Monitor logs for errors
5. Adjust field mappings as needed

---

## Troubleshooting

### Webhook not receiving data
- Check Zapier webhook URL is correct
- Verify server is running and accessible
- Check Zapier webhook logs

### Files not uploading
- Verify file URLs are accessible
- Check file size limits
- Ensure proper authentication

### DocSend upload fails
- Verify API key is correct
- Check DocSend API documentation
- Test API call outside Zapier first

---

**Need help? Check the webhook logs and Zapier task history for detailed error messages.**

