# Setting Up Canva Data Autofill

## Step 1: Install/Open Canva Data Autofill

1. **Open your Canva template** (or create it first)
2. **Go to Apps** in the left sidebar (or search for "Data" or "Autofill")
3. **Find "Data Autofill"** or **"Bulk Create"** app
4. **Click to add/install** the app if you haven't already

## Step 2: Create Your Data Source

### Option A: Create a Sample CSV File (Recommended for Setup)

1. **Create a CSV file** with your field names as headers:
   ```csv
   company_name,description,location,investment_date,investment_round,quarter,year,founders,co_investors,background
   Test Company,This is a test description,Los Angeles,2024-12-01,PRE-SEED,Q2,2024,Founder 1,Investor 1,This is the background text
   ```

2. **Save it** as `sample_data.csv`

3. **In Canva Data Autofill:**
   - Click "Connect Data" or "Upload Data"
   - Upload your CSV file
   - OR connect to Google Sheets

### Option B: Use Google Sheets

1. **Create a Google Sheet** with these column headers:
   - `company_name`
   - `description`
   - `location`
   - `investment_date`
   - `investment_round`
   - `quarter`
   - `year`
   - `founders`
   - `co_investors`
   - `background`

2. **Add one sample row** of data

3. **In Canva:**
   - Connect to Google Sheets
   - Select your sheet

## Step 3: Link Text Elements to Data Fields

1. **Select a text element** in your template (e.g., the company name text box)

2. **In the Data Autofill panel:**
   - You should see your data fields listed
   - Click on the field name that matches (e.g., `company_name`)
   - The text element is now linked to that field

3. **Repeat for all text elements:**
   - Company name → Link to `company_name`
   - Description → Link to `description`
   - Location → Link to `location`
   - Investment date → Link to `investment_date`
   - Investment round → Link to `investment_round`
   - Quarter → Link to `quarter`
   - Year → Link to `year`
   - Founders → Link to `founders`
   - Co-investors → Link to `co_investors`
   - Background → Link to `background`

## Step 4: Link Image Elements to Data Fields

For images, you'll need to set up image fields:

1. **Select an image placeholder/frame** (e.g., where headshots should go)

2. **In Data Autofill:**
   - Look for image field options
   - Create or select an image field named: `headshot`
   - Link the image placeholder to `headshot`

3. **Repeat for other images:**
   - Logo placeholder → Link to `logo`
   - Map placeholder → Link to `map` (optional)

**Note:** For images, you might need to:
- Upload sample images to your data source first, OR
- Use image URLs in your CSV/Sheet, OR
- Set up the image fields to accept uploads via API

## Step 5: Verify Field Names Match

**Critical:** Make sure your Canva Data Autofill field names match exactly:

✅ **Text Fields:**
- `company_name`
- `description`
- `location`
- `investment_date`
- `investment_round`
- `quarter`
- `year`
- `founders`
- `co_investors`
- `background`

✅ **Image Fields:**
- `headshot`
- `logo`
- `map` (optional)

## Step 6: Test the Setup

1. **Use your sample data** to generate a test design
2. **Verify** that all fields populate correctly
3. **Check** that images are positioned correctly

## Step 7: Get Your Template ID

Once everything is set up:

1. **Publish or save** your template
2. **Get the Template ID** from:
   - The URL: `canva.com/design/TEMPLATE_ID/view`
   - Or Canva's API dashboard
3. **Share the Template ID with me** so I can add it to your `.env` file

## Important Notes

### Field Name Matching

Our code sends data with these exact field names. Your Canva Data Autofill must use the **same exact names**:

- If your Canva field is named `Company Name` (with space), our code won't match it
- It must be `company_name` (lowercase, underscore)

### Image Handling

For images via API:
- Canva Data Autofill might expect image URLs in your data source
- Our code will upload images to Canva first, then link them
- You may need to set up image fields to accept API uploads

### Alternative: Hybrid Approach

If Canva Data Autofill doesn't work perfectly with images:
- Use Data Autofill for **text fields** (easier)
- Use API image uploads for **image fields** (more reliable)
- Our code can handle both approaches

## Troubleshooting

**Can't find Data Autofill app?**
- Search for "Bulk Create" or "Data Merge"
- Some Canva plans might not have this feature
- Alternative: Use placeholder text `{{field_name}}` instead

**Field names don't match?**
- Check for spaces, capitalization, special characters
- Field names must be exact: `company_name` not `Company Name` or `companyName`

**Images not working?**
- You might need to use the API approach for images
- Or upload images to a folder and reference them by URL

## Next Steps

Once you've set up Data Autofill:

1. ✅ Confirm all field names match exactly
2. ✅ Test with sample data
3. ✅ Get your Template ID
4. ✅ Tell me: "I've set up Data Autofill with these field names: [list them]"
5. ✅ Share your Template ID

I'll then verify the setup and make sure our code matches your Canva configuration!


