# Notion Database Property Names for Zapier

## Required Property Names

Your Notion database properties must match these **exact names** (case-sensitive) for Zapier to work correctly:

### ✅ Required Properties

| Property Name in Notion | Type | Required | Zapier Field |
|------------------------|------|----------|--------------|
| **Name** | Title | ✅ Yes | `{{1.Name}}` |
| **Website** | URL | No | `{{1.Website}}` |
| **Description** | Text | No | `{{1.Description}}` |
| **Address** | Text | No | `{{1.Address}}` |
| **Investment Date** | Date | No | `{{1.Investment Date}}` |
| **Co-Investors** | Multi-select | No | `{{1.Co-Investors}}` |
| **Number of Employees** | Number | No | `{{1.Number of Employees}}` |
| **First Time Founder** | Checkbox | No | `{{1.First Time Founder}}` |
| **Investment Memo** | URL | No | `{{1.Investment Memo}}` |
| **Headshot** | Files | ✅ Yes | `{{1.Headshot}}` |
| **Logo** | Files | ✅ Yes | `{{1.Logo}}` |
| **Status** | Select | No | `{{1.Status}}` |

## Important Notes

### 1. "Name" Property
- **Must be the Title property** (first column in database)
- This is automatically created when you create a database
- **Don't rename it** - it should be called "Name"

### 2. File Properties
- **Headshot** and **Logo** must be **Files** type properties
- Zapier will send the file URLs automatically
- Make sure files are actually attached (not just URLs)

### 3. Exact Match Required
- Property names must match **exactly** (case-sensitive)
- "Name" not "name" or "Company Name"
- "Investment Date" not "InvestmentDate" or "Date"
- "Number of Employees" not "Employees" or "Num Employees"

### 4. Status Property (for Filter)
- If using a filter, create a **Select** property called "Status"
- Options: "Ready", "Draft", "Pending", "Processed"
- Default: "Draft"

## How to Check Your Property Names

1. **Open your Notion database**
2. **Look at the column headers** - these are your property names
3. **Verify they match** the names in the table above
4. **If they don't match**, either:
   - Rename them in Notion to match, OR
   - Update the Zapier webhook payload to use your actual property names

## Example Database Structure

Your database should look like this:

```
┌──────────┬──────────┬──────────────┬──────────┬──────────────┐
│ Name     │ Website  │ Description  │ Address  │ Status       │
├──────────┼──────────┼──────────────┼──────────┼──────────────┤
│ Company  │ https:// │ Description  │ Address  │ Ready        │
│ A        │ ...      │              │          │              │
└──────────┴──────────┴──────────────┴──────────┴──────────────┘
```

## Quick Checklist

- [ ] "Name" property exists (Title type)
- [ ] "Headshot" property exists (Files type)
- [ ] "Logo" property exists (Files type)
- [ ] Property names match exactly (case-sensitive)
- [ ] Status property exists if using filter (Select type)

## If Your Properties Have Different Names

If your Notion properties have different names, you need to update the Zapier webhook payload to match.

**Example:** If your property is called "Company Name" instead of "Name":
- In Zapier, use: `{{1.Company Name}}` instead of `{{1.Name}}`

---

**The most important property is "Name" - it must be the Title property in your database!**

