# Setting Up Your Own Portfolio Companies Database

Since you don't have access to Slauson & Co.'s database yet, let's create your own test database first.

## Step 1: Create Database in Notion

### Option A: Use the Setup Script (Recommended)

1. Make sure you have your Notion API key in `.env`:
   ```env
   NOTION_API_KEY=secret_your_token_here
   ```

2. Run the setup script:
   ```bash
   python setup_notion.py
   ```

3. When prompted, enter a parent page ID where you want the database created
   - Create a new page in Notion first
   - Get the page ID from the URL (the long string after the last `/`)

4. The script will create:
   - "Portfolio Companies" database
   - Company template page

### Option B: Create Manually in Notion

1. **Create a new page** in Notion (name it "Portfolio" or similar)

2. **Add a database** to the page:
   - Type `/database` and select "Table - Inline"
   - Or click "+" → "Table"

3. **Name the database**: "Portfolio Companies"

4. **Add these properties** (click "+" to add columns):

| Property Name | Type | Required | Notes |
|--------------|------|----------|-------|
| Name | Title | ✅ Yes | Main company name |
| Website | URL | No | Company website |
| Description | Text | No | One-line description |
| Address | Text | No | Mailing address |
| Investment Date | Date | No | When you invested |
| Co-Investors | Multi-select | No | Other investors |
| Number of Employees | Number | No | Employee count |
| First Time Founder | Checkbox | No | True/false |
| Investment Memo | URL | No | Link to memo doc |
| Headshot | Files | ✅ Yes | Founder photo |
| Logo | Files | ✅ Yes | Company logo |
| Status | Select | No | Ready/Draft/Pending |
| DocSend Link | URL | No | Auto-filled after processing |

5. **Set up Status property**:
   - Type: Select
   - Options: "Ready", "Draft", "Pending", "Processed"
   - Default: "Draft"

## Step 2: Create Company Template (Optional but Recommended)

1. **Create a new page** in the same parent as your database
2. **Name it**: "Company Template"
3. **Add these sections**:
   - Heading 1: "Notes"
   - Heading 1: "Updates"
   - Heading 1: "Contacts"
   - Heading 1: "Onboarding Call"

4. **Get the template page ID**:
   - Copy the URL
   - Extract the ID (long string after the last `/`)

## Step 3: Share Database with Integration

1. **Open your Portfolio Companies database**
2. Click **"..."** (three dots) → **"Connections"**
3. **Add your Notion integration**:
   - If you created one: Select it from the list
   - If not: Create one at https://www.notion.so/my-integrations
4. **Do the same for the template page** (if created)

## Step 4: Get Database ID

1. **Open your Portfolio Companies database**
2. **Copy the URL** from your browser
3. **Extract the database ID**:
   - URL format: `https://www.notion.so/Your-Page-Name-abc123def456...`
   - The ID is the part after the last `/` (e.g., `abc123def456...`)
   - Remove any query parameters (everything after `?`)

4. **Add to your `.env` file**:
   ```env
   NOTION_DATABASE_ID=abc123def456...
   NOTION_TEMPLATE_PAGE_ID=xyz789... (if you created template)
   ```

## Step 5: Test Your Database

1. **Create a test entry**:
   - Click "+ New" in your database
   - Fill in:
     - Name: "Test Company"
     - Status: "Ready"
     - Upload a test headshot image
     - Upload a test logo image
     - Fill other fields as needed

2. **Verify it works**:
   ```bash
   python test_integration.py
   ```

## Step 6: Configure Zapier

Now that your database is set up:

1. **Go to Zapier** and create a new Zap
2. **Trigger**: Notion → "New Database Item"
3. **Select your database**: "Portfolio Companies"
4. **Test the trigger**: Create a test entry and verify Zapier sees it

## Database Structure Summary

Your database should look like this:

```
Portfolio Companies Database
├── Name (Title) ✅
├── Website (URL)
├── Description (Text)
├── Address (Text)
├── Investment Date (Date)
├── Co-Investors (Multi-select)
├── Number of Employees (Number)
├── First Time Founder (Checkbox)
├── Investment Memo (URL)
├── Headshot (Files) ✅
├── Logo (Files) ✅
├── Status (Select: Ready/Draft/Pending)
└── DocSend Link (URL) - Auto-filled
```

## Quick Reference: Property Types in Notion

- **Title**: Use for "Name" (first column, automatically created)
- **URL**: For websites and links
- **Text**: For descriptions and addresses
- **Date**: For investment dates
- **Multi-select**: For co-investors (create tags)
- **Number**: For employee count
- **Checkbox**: For true/false (First Time Founder)
- **Files**: For headshots and logos
- **Select**: For Status dropdown

## Troubleshooting

### "Database not showing in Zapier"
- Make sure database is shared with Zapier integration
- Refresh Zapier database list
- Check integration has access

### "Properties not matching"
- Property names must match exactly (case-sensitive)
- Use Zapier's field picker to select fields
- Don't type field names manually

### "Files not uploading"
- Ensure Headshot and Logo are "Files" type properties
- Attach actual files (not just URLs)
- Check file size limits

## Next Steps

Once your database is set up:

1. ✅ Test with sample data
2. ✅ Configure Zapier webhook (see `ZAPIER_COMPLETE_SETUP.md`)
3. ✅ Test end-to-end automation
4. ✅ When you get Slauson's database access, just update the database ID in Zapier

---

**Pro Tip**: Keep your test database structure identical to what Slauson will use, so migration is just a database ID change!

