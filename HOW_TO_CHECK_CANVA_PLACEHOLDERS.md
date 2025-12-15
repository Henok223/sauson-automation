# How to Check Your Canva Template Placeholder Fields

## Option 1: If You're Using Canva Autofill Feature

1. **Open your Canva template** in Canva
2. **Look for the Autofill feature**:
   - Click on any text element in your template
   - Look for an "Autofill" or "Data" option in the properties panel
   - Or go to: **File** > **Autofill** (if available)
3. **Check the field names**:
   - Canva Autofill uses field names like `{{company_name}}` or just `company_name`
   - Look at what field names you've defined in your Autofill setup
4. **Match them to our required fields**:
   - Our code sends: `company_name`, `description`, `location`, `investment_date`, `investment_round`, `quarter`, `year`, `founders`, `co_investors`, `background`
   - Your Canva template should have these same field names

## Option 2: If You're Using Text Placeholders Manually

1. **Open your Canva template**
2. **Look at your text elements** - they might have placeholders like:
   - `{{company_name}}`
   - `{{description}}`
   - `{{location}}`
   - etc.
3. **Note the field names** (the part inside `{{}}`)

## Option 3: If You Haven't Set Up Placeholders Yet

If you haven't set up placeholders, you have two options:

### Option A: Use Canva's Autofill API (Recommended)

1. **In your Canva template**, identify which text elements need to be dynamic
2. **Set up Autofill fields** in Canva:
   - Select a text element
   - Look for "Autofill" or "Data" options
   - Create a field name (e.g., `company_name`)
   - Repeat for all dynamic text elements
3. **For images**, set up image placeholders:
   - Select image placeholders
   - Name them: `headshot`, `logo`, `map`

### Option B: Tell Me Your Current Field Names

If your Canva template already has placeholder names that are different, just tell me:
- What field names you're currently using
- I can update the code to match your existing names

## What to Tell Me

**If you've already set up placeholders:**
- "I've checked my Canva template and the field names are: [list your field names]"
- OR "My Canva template uses these field names: [list them]"

**If you haven't set up placeholders yet:**
- "I haven't set up placeholders yet - I'll use the names you provided"
- OR "I need help setting them up"

**If you're not sure:**
- "I'm not sure how to check - can you help?"
- I can guide you through finding them or help you set them up

## Quick Check List

Our code expects these **exact field names** in your Canva template:

✅ Text Fields:
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

✅ Image Fields:
- `headshot`
- `logo`
- `map` (optional)

**Just confirm:** "My Canva template uses these exact field names" or tell me if yours are different!


