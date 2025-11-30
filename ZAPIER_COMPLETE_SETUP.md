# Complete Zapier Setup Guide

## Step-by-Step Configuration

### Step 1: Notion Trigger Setup

1. **App**: Notion
2. **Event**: "New Database Item"
3. **Account**: Connect your Notion account
4. **Database**: Select "Portfolio Companies" database
   - If you don't see it: Go to Notion → Open database → "..." → "Connections" → Add Zapier integration

### Step 2: Optional Filter (Recommended)

**Add a Filter step** to only trigger when Status = "Ready":

1. **App**: Filter by Zapier
2. **Condition**: 
   - Field: `{{1.Status}}`
   - Condition: "Text is exactly"
   - Value: `Ready`
3. **Only continue if**: Condition matches

**OR** use Zapier's built-in filter in the Notion trigger:
- In Notion trigger settings, add filter:
  - Property: "Status"
  - Condition: "is"
  - Value: "Ready"

### Step 3: Webhook Action Configuration

**App**: Webhooks by Zapier  
**Event**: POST

#### URL Configuration
```
https://your-server.com/webhook/onboarding
```
- Replace `your-server.com` with:
  - Local testing: Your ngrok URL (e.g., `https://abc123.ngrok.io`)
  - Production: Your deployed server URL

#### Method
- **POST**

#### Headers
Add a header:
- **Key**: `Content-Type`
- **Value**: `application/json`

#### Data (JSON Payload)

Copy this exact JSON into the "Data" field:

```json
{
  "company_data": {
    "name": "{{1.Name}}",
    "website": "{{1.Website}}",
    "description": "{{1.Description}}",
    "address": "{{1.Address}}",
    "investment_date": "{{1.Investment Date}}",
    "co_investors": "{{1.Co-Investors}}",
    "num_employees": "{{1.Number of Employees}}",
    "first_time_founder": "{{1.First Time Founder}}",
    "investment_memo_link": "{{1.Investment Memo}}"
  },
  "headshot_url": "{{1.Headshot}}",
  "logo_url": "{{1.Logo}}"
}
```

#### Important Notes:

1. **Field Names**: The `{{1.Field Name}}` syntax pulls data from Step 1 (Notion trigger)
2. **Exact Match**: Property names must match your Notion database exactly:
   - "Name" (not "Company Name")
   - "Investment Date" (with space)
   - "Number of Employees" (with spaces)
   - etc.

3. **Using Zapier Field Picker**: 
   - Click the "+" icon next to each field
   - Select from dropdown to ensure correct field names
   - This prevents typos

4. **File Fields**: 
   - `{{1.Headshot}}` and `{{1.Logo}}` should be file URLs from Notion
   - The webhook automatically downloads these files

### Step 4: Test the Webhook

1. Click "Test" in Zapier
2. Create a test entry in your Notion database with:
   - All required fields filled
   - Status = "Ready" (if using filter)
   - Headshot and Logo files attached
3. Check webhook response:
   - Should return JSON with `success: true`
   - Check your server logs for any errors

---

## Complete Zap Structure

```
┌─────────────────────────┐
│  Step 1: Notion         │  Trigger: New Database Item
│  Database: Portfolio    │  Filter: Status = "Ready" (optional)
│  Companies              │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Step 2: Filter         │  Only if Status = "Ready"
│  (Optional)             │  Skip if not needed
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Step 3: Webhook POST   │  Send to automation server
│  URL: /webhook/         │  Payload: Company data
│  onboarding             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Step 4: DocSend        │  Upload PDF (if configured)
│  (Optional)             │
└─────────────────────────┘
```

---

## Field Mapping Reference

### Notion Database Properties → Zapier Fields

| Notion Property Name | Zapier Field Syntax | Data Type | Notes |
|---------------------|---------------------|-----------|-------|
| Name | `{{1.Name}}` | Text | Required |
| Website | `{{1.Website}}` | URL | Optional |
| Description | `{{1.Description}}` | Text | Optional |
| Address | `{{1.Address}}` | Text | Optional |
| Investment Date | `{{1.Investment Date}}` | Date | Format: YYYY-MM-DD |
| Co-Investors | `{{1.Co-Investors}}` | Multi-select | Array of strings |
| Number of Employees | `{{1.Number of Employees}}` | Number | Integer |
| First Time Founder | `{{1.First Time Founder}}` | Checkbox | Boolean (true/false) |
| Investment Memo | `{{1.Investment Memo}}` | URL | Link to memo |
| Headshot | `{{1.Headshot}}` | Files | File URL |
| Logo | `{{1.Logo}}` | Files | File URL |
| Status | `{{1.Status}}` | Select | For filtering |

### Expected Webhook Response

```json
{
  "success": true,
  "notion_page_id": "abc123...",
  "notion_folder_id": "def456...",
  "canva_slide_path": "/tmp/slide.pdf",
  "docsend_individual_link": "https://docsend.com/view/...",
  "errors": []
}
```

---

## Troubleshooting

### Issue: Database not showing in Zapier

**Solution:**
1. Open your Portfolio Companies database in Notion
2. Click "..." (three dots) → "Connections"
3. Add "Zapier" integration
4. Refresh Zapier database selection

### Issue: Field names not matching

**Solution:**
1. In Zapier, use the field picker (click "+" icon)
2. Select fields from dropdown instead of typing
3. Verify property names in Notion match exactly (case-sensitive)

### Issue: Files not uploading

**Solution:**
1. Ensure Headshot and Logo are file properties in Notion
2. Files must be attached (not just URLs)
3. Check webhook logs for download errors

### Issue: Date format errors

**Solution:**
- Zapier automatically formats dates
- If issues occur, use "Formatter" step to convert date format
- Expected format: `YYYY-MM-DD`

### Issue: Co-Investors as array

**Solution:**
- If Co-Investors is multi-select, Zapier sends as comma-separated string
- Webhook handles both formats
- If needed, use "Code by Zapier" to convert to array

---

## Advanced: Conditional Logic

### Only Process When All Required Fields Present

Add a "Filter" step before webhook:

**Condition**: 
- `{{1.Name}}` is not empty
- AND `{{1.Headshot}}` is not empty
- AND `{{1.Logo}}` is not empty

### Different Actions Based on Status

Use "Paths" in Zapier:
- Path A: Status = "Ready" → Run automation
- Path B: Status = "Draft" → Skip or send notification

---

## Testing Checklist

Before going live:

- [ ] Notion database shared with Zapier integration
- [ ] All field names match exactly
- [ ] Webhook URL is correct and accessible
- [ ] Test entry created with all fields
- [ ] Webhook receives data (check logs)
- [ ] Automation processes successfully
- [ ] PDF generated correctly
- [ ] DocSend upload works (if configured)
- [ ] Error handling works (test with missing fields)

---

## Quick Copy-Paste Configuration

### For Zapier Webhook "Data" Field:

```json
{
  "company_data": {
    "name": "{{1.Name}}",
    "website": "{{1.Website}}",
    "description": "{{1.Description}}",
    "address": "{{1.Address}}",
    "investment_date": "{{1.Investment Date}}",
    "co_investors": "{{1.Co-Investors}}",
    "num_employees": "{{1.Number of Employees}}",
    "first_time_founder": "{{1.First Time Founder}}",
    "investment_memo_link": "{{1.Investment Memo}}"
  },
  "headshot_url": "{{1.Headshot}}",
  "logo_url": "{{1.Logo}}"
}
```

### Filter Condition (if using):

```
{{1.Status}} is exactly "Ready"
```

---

## Next Steps After Setup

1. **Test with sample data** in Notion
2. **Monitor webhook logs** for first few runs
3. **Verify PDF generation** works correctly
4. **Set up error notifications** in Zapier (optional)
5. **Document any customizations** for your team

---

**Ready to configure?** Copy the JSON payload above into your Zapier webhook action, and use the field picker to ensure all field names match your Notion database exactly!

