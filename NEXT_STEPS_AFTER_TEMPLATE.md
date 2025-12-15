# Next Steps After Creating Your Canva Template

## ✅ What You've Done

1. Created your Canva template
2. Set up Data Autofill with these fields:
   - `company_name`
   - `description`
   - `location`
   - `investment_date`
   - `investment_stage` (combined: "PRE-SEED • Q2 2024")
   - `founders`
   - `co_investors`
   - `background`
3. Added image placeholders (for headshot, logo, map)

## 🔧 What You Need to Do Now

### Step 1: Get Your Template ID

1. **Open your template** in Canva
2. **Look at the URL** - it should look like:
   ```
   canva.com/design/TEMPLATE_ID_HERE/view
   ```
3. **Copy the Template ID** (the long string of characters)

**OR**

1. Go to Canva's API dashboard
2. Find your template
3. Copy the Template ID

### Step 2: Add Template ID to `.env` File

Once you have your Template ID, tell me:
- "My Template ID is: [your_template_id]"

I'll add it to your `.env` file:
```
CANVA_TEMPLATE_ID=your_template_id_here
```

### Step 3: Verify Your Field Names Match

Your Canva Data Autofill fields should be:
- ✅ `company_name`
- ✅ `description`
- ✅ `location`
- ✅ `investment_date`
- ✅ `investment_stage` (combined format)
- ✅ `founders`
- ✅ `co_investors`
- ✅ `background`

**The code has been updated to support `investment_stage`!** It will:
- Use `investment_stage` if provided in webhook data
- OR combine `investment_round`, `quarter`, `year` into `investment_stage` format: "PRE-SEED • Q2 2024"

### Step 4: Image Placeholders

Make sure you have image placeholders positioned:
- **Top right** → Will be replaced with logo
- **Middle right** (optional) → Will be replaced with map
- **Bottom right** → Will be replaced with headshot

The code will automatically replace them by position (no naming needed).

### Step 5: Test the Setup

Once everything is configured, you can test by sending a webhook with:
```json
{
  "company_data": {
    "name": "Test Company",
    "description": "Test description",
    "location": "Los Angeles",
    "investment_date": "2024-12-01",
    "investment_stage": "PRE-SEED • Q2 2024",
    "founders": ["Founder 1"],
    "co_investors": ["Investor 1"],
    "background": "Test background text"
  },
  "headshot_url": "https://...",
  "logo_url": "https://...",
  "notion_page_id": "..."
}
```

## 📋 Checklist

- [ ] Got Template ID from Canva
- [ ] Template ID added to `.env` file (I'll do this once you give me the ID)
- [ ] Verified all Data Autofill field names match
- [ ] Image placeholders are in correct positions
- [ ] Ready to test!

## 🚀 What Happens Next

Once you provide your Template ID:
1. I'll add it to your `.env` file
2. The code will be ready to use
3. When webhooks come in, it will:
   - Download and process images
   - Generate map
   - Upload to Canva
   - Populate your template with data
   - Export as PDF
   - Upload to Google Drive and DocSend
   - Update Notion

## ❓ Questions?

If you need help with:
- Finding your Template ID
- Verifying field names
- Testing the setup

Just let me know!


