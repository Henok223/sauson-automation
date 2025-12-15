# Notion Database Properties - What You Need

## What You Already Have ✅

Your Notion database **already has** properties for company data:
- Company Name
- Description
- Location
- Investment Date
- Investment Stage
- Founders
- Co-Investors
- Background
- etc.

**These are fine!** The webhook receives this data from Notion (or Zapier), so you don't need to change these.

## What You Need to ADD ⚠️

You need to add **3 NEW properties** to store the **results** of the slide generation:

### 1. Google Drive Link Property
- **Purpose**: Store the shareable Google Drive link to the generated PDF
- **Type**: **URL**
- **Name Options** (code tries these in order):
  - `Google Drive Link` (preferred)
  - `Drive Link`
  - `PDF Link`
  - `Slide Link`

### 2. DocSend Link Property
- **Purpose**: Store the shareable DocSend link to the generated PDF
- **Type**: **URL**
- **Name Options** (code tries these in order):
  - `DocSend Link` (preferred)
  - `DocSend`
  - `Presentation Link`

### 3. Status Property
- **Purpose**: Track whether slide generation is complete
- **Type**: **Select** (with "completed" option) OR **Text**
- **Name Options** (code tries these in order):
  - `Status` (preferred)
  - `Slide Status`
  - `Processing Status`
  - `Completion Status`

## How It Works

### The Flow:

1. **Notion/Zapier triggers webhook** with company data:
   ```json
   {
     "company_data": {
       "name": "Company Name",
       "description": "...",
       ...
     },
     "notion_page_id": "page_id_here"
   }
   ```

2. **Code processes** and generates slide

3. **Code uploads** to Google Drive and DocSend

4. **Code updates the Notion record** with:
   - Google Drive link → stored in `Google Drive Link` property
   - DocSend link → stored in `DocSend Link` property
   - Status → set to "completed" in `Status` property

## What to Do

### Step 1: Add the 3 New Properties

In your Notion database, add:

1. **Property Name**: `Google Drive Link`
   - **Type**: URL
   
2. **Property Name**: `DocSend Link`
   - **Type**: URL
   
3. **Property Name**: `Status`
   - **Type**: Select (add option "completed") OR Text

### Step 2: Tell Me the Exact Names

Once you've added them, tell me:
- "I've added: Google Drive Link (URL), DocSend Link (URL), Status (Select with 'completed')"

OR if you used different names:
- "I've added: [your exact property names]"

I'll verify they match what the code expects, or update the code if needed.

## Summary

**✅ Keep existing properties** (company name, description, etc.) - those are fine!

**➕ Add 3 new properties** for storing the results:
- Google Drive Link (URL)
- DocSend Link (URL)  
- Status (Select or Text)

These are just for storing the **output** (links and status), not the input data.


