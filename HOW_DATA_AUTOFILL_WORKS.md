# How Data Autofill Works - CSV vs API

## Two Ways to Use Canva Data Autofill

### Method 1: CSV Upload in Canva UI (What You Did)
- You upload a CSV file in Canva's Data Autofill interface
- Canva reads the CSV and creates designs for each row
- You manually trigger the generation in Canva

### Method 2: API Autofill (What Our Code Does)
- Our code sends data **programmatically** via Canva's API
- Uses the **same field names** you set up in Data Autofill
- Automatically generates designs without manual steps

## How They Work Together

When you set up Data Autofill with a CSV in Canva, you're doing two things:

1. **Defining field names** - The column headers in your CSV become the field names
   - Example: CSV column `company_name` → Canva field `company_name`

2. **Linking elements** - You link text/image elements in your template to those fields

**Our code uses the same field names** to send data via API!

## How Our Code Sends Data

Here's what happens when a webhook comes in:

### Step 1: Receive Webhook Data
```json
{
  "company_data": {
    "name": "Test Company",
    "description": "Test description",
    "location": "Los Angeles",
    ...
  }
}
```

### Step 2: Prepare Data for Canva
Our code formats it to match your Data Autofill field names:

```python
autofill_data = {
    "data": {
        "company_name": "Test Company",      # Matches your CSV column
        "description": "Test description",     # Matches your CSV column
        "location": "Los Angeles",            # Matches your CSV column
        "investment_date": "2024-12-01",
        "investment_stage": "PRE-SEED • Q2 2024",
        "founders": "Founder 1",
        "co_investors": "Investor 1",
        "background": "Background text"
    },
    "images": {
        "headshot": "upload_id_123",
        "logo": "upload_id_456"
    }
}
```

### Step 3: Send to Canva API
```python
POST https://api.canva.com/rest/v1/designs/{design_id}/autofill
{
    "data": { ... },
    "images": { ... }
}
```

### Step 4: Canva Populates Template
Canva receives the data and:
- Matches field names to your Data Autofill fields
- Populates text elements linked to those fields
- Replaces image placeholders with uploaded images

## The Connection

**Your CSV setup defines the field structure**
- CSV columns = Field names
- You linked elements to these fields in Canva

**Our API code uses those same field names**
- Code sends data with matching field names
- Canva recognizes them because you set them up in Data Autofill
- Elements get populated automatically

## Important: Field Names Must Match

Your CSV column headers must match what our code sends:

✅ **What Our Code Sends:**
- `company_name`
- `description`
- `location`
- `investment_date`
- `investment_stage`
- `founders`
- `co_investors`
- `background`

✅ **Your CSV Should Have:**
- Same column names (exact match)
- Same field names in Canva Data Autofill

## Example Flow

1. **You set up in Canva:**
   - CSV with columns: `company_name`, `description`, `location`, etc.
   - Link text elements to these fields

2. **Webhook comes in:**
   - Our code receives company data

3. **Code sends to Canva:**
   - Formats data with same field names: `company_name`, `description`, etc.
   - Calls Canva Autofill API

4. **Canva populates:**
   - Recognizes field names (from your Data Autofill setup)
   - Fills in linked elements
   - Generates the design

## Why This Works

Canva's Data Autofill and API Autofill use the **same underlying system**:
- Both use the field names you define
- Both populate the same linked elements
- API just does it programmatically instead of from CSV

## Summary

- **Your CSV setup** = Defines field names and links elements
- **Our API code** = Sends data with matching field names
- **Canva** = Recognizes the fields and populates the template

They work together! Your Data Autofill setup tells Canva what fields exist and which elements to populate. Our code sends data to those same fields.


