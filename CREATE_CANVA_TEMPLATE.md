# How to Create Your Canva Template

Since you don't have a template yet, here's how to create one that matches your slide design and works with our automation.

## Step 1: Create the Template Design

1. **Go to Canva** and create a new design
2. **Set the size**: 1920 x 1080 pixels (or use "Presentation" size)
3. **Design your slide** to match the style you showed:
   - **Left sidebar (Orange)**: Narrow vertical orange bar on the left
     - Top: "PRE-SEED Q2, 2024" (vertical text)
     - Bottom: "SLAUSON&CO." (vertical text)
   - **Main content area (Dark grey)**: Larger area on the right
     - Company name in large orange text (top left)
     - Logo in top right corner
     - Map overlay (upper right portion)
     - Information sections (left-mid):
       - Founders section
       - Co-Investors section
       - Background/description section
     - Founder headshots (bottom right, overlapping style)

## Step 2: Set Up Autofill/Placeholder Fields

### For Text Elements:

1. **Select each text element** that should be dynamic
2. **Set up Autofill fields** (Canva's Autofill feature):
   - Look for "Autofill" or "Data" option in the properties panel
   - OR use Canva's Autofill API setup
   - Create field names exactly as listed below

3. **Required Text Field Names** (use these exact names):
   - `company_name` - For the company name (large orange text)
   - `description` - For company description
   - `location` - For location/address
   - `investment_date` - For investment date
   - `investment_round` - For "PRE-SEED" (or other rounds)
   - `quarter` - For "Q2" (or other quarters)
   - `year` - For "2024" (or other years)
   - `founders` - For founder names (comma-separated)
   - `co_investors` - For co-investor names (comma-separated)
   - `background` - For background/description text

### For Image Elements:

1. **Create image placeholders** where images should go:
   - **Headshot placeholder** (bottom right) - name it: `headshot`
   - **Logo placeholder** (top right) - name it: `logo`
   - **Map placeholder** (upper right, optional) - name it: `map`

2. **Set up image placeholders**:
   - Add a placeholder image or frame
   - Name it with the exact field names above
   - Position them correctly in your design

## Step 3: Using Canva's Autofill Feature

### Method A: Canva Autofill UI (if available)

1. Go to your template in Canva
2. Look for **"Autofill"** or **"Data"** in the menu
3. Set up data fields matching the names above
4. Link each text element to its corresponding field

### Method B: Canva API Autofill (Recommended)

Canva's API uses Autofill with field names. When you create the template:

1. **Design your template** with all the visual elements
2. **Note the element IDs** or use Canva's Autofill feature to name fields
3. **The field names must match** what our code sends:
   - Text fields: `company_name`, `description`, `location`, etc.
   - Image fields: `headshot`, `logo`, `map`

## Step 4: Get Your Template ID

Once your template is created:

1. **Publish or share** your template
2. **Get the Template ID**:
   - The template ID is usually in the URL: `canva.com/design/TEMPLATE_ID/view`
   - OR in Canva's API dashboard
3. **Add it to your `.env` file**:
   ```
   CANVA_TEMPLATE_ID=your_template_id_here
   ```

## Step 5: Test the Template

After creating the template:

1. Make sure all placeholder field names match exactly
2. Test with a sample company data to verify everything populates correctly
3. Verify images (headshot, logo, map) are positioned correctly

## Quick Checklist

- [ ] Template created with correct dimensions (1920x1080)
- [ ] Design matches your slide style (orange sidebar, dark background)
- [ ] All text elements have Autofill field names set up
- [ ] Image placeholders created and named correctly
- [ ] Template ID obtained and added to `.env`
- [ ] Field names match exactly: `company_name`, `description`, `location`, `investment_date`, `investment_round`, `quarter`, `year`, `founders`, `co_investors`, `background`
- [ ] Image placeholders named: `headshot`, `logo`, `map`

## Need Help?

If you need help with:
- **Canva Autofill setup**: Check Canva's documentation or I can help guide you
- **Template design**: I can provide more specific design guidance
- **Field names**: Just confirm you'll use the exact names I provided

Once your template is ready, just tell me:
- "I've created my template with these field names: [confirm they match]"
- "I need help with [specific part]"


