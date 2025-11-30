# Final Property Mapping - Verified ✅

## Your Notion Database Properties

These match perfectly with the Zapier webhook configuration:

| Notion Property | Type | Zapier Field | Status |
|----------------|------|--------------|--------|
| **Name** | Title | `{{1.Name}}` | ✅ Required |
| **Status** | Select | `{{1.Status}}` | ✅ For filter |
| **Website** | URL | `{{1.Website}}` | Optional |
| **Description** | Text | `{{1.Description}}` | Optional |
| **Address** | Text | `{{1.Address}}` | Optional |
| **Investment Date** | Date | `{{1.Investment Date}}` | Optional |
| **Co-Investors** | Text/Multi-select | `{{1.Co-Investors}}` | Optional |
| **Number of Employees** | Number | `{{1.Number of Employees}}` | Optional |
| **First Time Founder** | Checkbox | `{{1.First Time Founder}}` | Optional |
| **Investment Memo** | URL | `{{1.Investment Memo}}` | Optional |
| **Headshot** | Files | `{{1.Headshot}}` | ✅ Required |
| **Logo** | Files | `{{1.Logo}}` | ✅ Required |

## Status Options

Your Status property should have these options:
- "Ready" (for triggering automation)
- "Draft"
- "Processing"
- "Complete"

## Zapier Webhook Payload (Already Configured)

Your Zapier webhook is already set up with these exact field names:

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

## ✅ Everything Matches!

Your property names match the Zapier configuration perfectly. You're all set!

## Testing Checklist

When creating a test entry:

- [ ] **Name**: Enter company name (required)
- [ ] **Status**: Set to "Ready" (if using filter)
- [ ] **Headshot**: Upload an image file (required)
- [ ] **Logo**: Upload an image file (required)
- [ ] Fill in other fields as needed

## Important Notes

1. **Name** must be the Title property (first column)
2. **Headshot** and **Logo** must be Files type (not URLs)
3. **Status** should be "Ready" to trigger the Zap (if using filter)
4. All property names match exactly - no changes needed!

---

**You're ready to test!** Create an entry with these properties and it should work! 🎉

