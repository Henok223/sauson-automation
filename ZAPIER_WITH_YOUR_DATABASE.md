# Configuring Zapier with Your Own Database

Now that you've created your own Portfolio Companies database, here's how to configure Zapier.

## Step 1: Share Database with Zapier Integration

1. **Open your Portfolio Companies database** in Notion
2. Click **"..."** (three dots) in the top right
3. Select **"Connections"**
4. Click **"Add connections"**
5. **Select "Zapier"** (or your integration name)
   - If you don't see Zapier, create a connection at https://zapier.com/apps/notion/integrations

## Step 2: Create Zap in Zapier

1. Go to https://zapier.com
2. Click **"Create Zap"**
3. Name it: **"Portfolio Onboarding - Test"**

## Step 3: Configure Notion Trigger

1. **Trigger App**: Select **"Notion"**
2. **Trigger Event**: Select **"New Database Item"**
3. **Account**: Connect your Notion account (if not already connected)
4. **Database**: 
   - Click the dropdown
   - **Select "Portfolio Companies"** (your database)
   - If you don't see it:
     - Make sure database is shared with Zapier (Step 1)
     - Refresh the dropdown
     - Check you're using the right Notion account

5. **Test the trigger**:
   - Click "Test trigger"
   - Create a test entry in your database
   - Zapier should find it

## Step 4: Add Filter (Optional but Recommended)

Add a **Filter by Zapier** step:

1. **App**: Filter by Zapier
2. **Event**: Only continue if...
3. **Condition**:
   - **Field**: `{{1.Status}}`
   - **Condition**: "Text is exactly"
   - **Value**: `Ready`

This ensures automation only runs when Status = "Ready"

## Step 5: Configure Webhook Action

1. **Action App**: Select **"Webhooks by Zapier"**
2. **Action Event**: Select **"POST"**
3. **URL**: 
   - For local testing: Use ngrok URL (e.g., `https://abc123.ngrok.io/webhook/onboarding`)
   - For production: Your deployed server URL
4. **Method**: POST
5. **Headers**: 
   - Add header:
     - **Key**: `Content-Type`
     - **Value**: `application/json`
6. **Data (JSON)**: Copy this exact JSON:

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

**Important**: Use Zapier's field picker (click "+" icon) to select fields from your database. This ensures exact field name matching.

## Step 6: Test Your Zap

1. **Create a test entry** in your Portfolio Companies database:
   - Name: "Test Company"
   - Status: "Ready"
   - Upload a test headshot image
   - Upload a test logo image
   - Fill in other fields

2. **Run the Zap**:
   - In Zapier, click "Test" on each step
   - Check webhook receives data
   - Verify automation processes successfully

## Field Mapping Reference

Make sure these Notion properties exist in your database:

| Zapier Field | Notion Property | Type | Required |
|-------------|----------------|------|----------|
| `{{1.Name}}` | Name | Title | ✅ Yes |
| `{{1.Website}}` | Website | URL | No |
| `{{1.Description}}` | Description | Text | No |
| `{{1.Address}}` | Address | Text | No |
| `{{1.Investment Date}}` | Investment Date | Date | No |
| `{{1.Co-Investors}}` | Co-Investors | Multi-select | No |
| `{{1.Number of Employees}}` | Number of Employees | Number | No |
| `{{1.First Time Founder}}` | First Time Founder | Checkbox | No |
| `{{1.Investment Memo}}` | Investment Memo | URL | No |
| `{{1.Headshot}}` | Headshot | Files | ✅ Yes |
| `{{1.Logo}}` | Logo | Files | ✅ Yes |
| `{{1.Status}}` | Status | Select | No (for filter) |

## Troubleshooting

### Database not showing in Zapier
- ✅ Make sure database is shared with Zapier integration
- ✅ Refresh Zapier database dropdown
- ✅ Check you're using correct Notion account

### Field names not matching
- ✅ Use Zapier's field picker (don't type manually)
- ✅ Verify property names match exactly (case-sensitive)
- ✅ Check your database has all required properties

### Files not working
- ✅ Ensure Headshot and Logo are "Files" type properties
- ✅ Attach actual files (not just URLs)
- ✅ Test with small image files first

## Next Steps

Once your test database works:

1. ✅ Test with multiple entries
2. ✅ Verify all fields map correctly
3. ✅ Test the filter (Status = "Ready")
4. ✅ When you get Slauson's database access:
   - Just change the database selection in Zapier
   - All field mappings should stay the same
   - Test with their database

## Quick Checklist

- [ ] Database created in Notion
- [ ] Database shared with Zapier integration
- [ ] Zap created in Zapier
- [ ] Notion trigger configured (database selected)
- [ ] Filter added (Status = "Ready")
- [ ] Webhook configured with correct URL
- [ ] JSON payload added with field mappings
- [ ] Test entry created in database
- [ ] Zap tested successfully

---

**You're all set!** Your Zapier integration is now configured with your own database. When you get access to Slauson's database, just update the database selection in the Zapier trigger step.

