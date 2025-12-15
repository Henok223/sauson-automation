# Setup Requirements - Exact Information Needed

## 1. Google Drive Credentials Setup

### Option A: Service Account (Recommended for Server/Production)

**What I need from you:**
1. The **full file path** to your service account JSON file (e.g., `/Users/henoktewolde/slauson-automation/google-service-account.json`)

**How to get it:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable **Google Drive API**:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click "Enable"
4. Create Service Account:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Give it a name (e.g., "slauson-automation")
   - Click "Create and Continue"
   - Skip role assignment (or add "Editor" role)
   - Click "Done"
5. Create Key:
   - Click on the service account you just created
   - Go to "Keys" tab
   - Click "Add Key" > "Create new key"
   - Choose "JSON" format
   - Download the JSON file
   - **Save this file in your project directory** (e.g., `google-service-account.json`)

**Once you have the file path, tell me:**
- The full path to the JSON file

**I'll add to `.env`:**
```
GOOGLE_SERVICE_ACCOUNT_PATH=/full/path/to/google-service-account.json
```

### Option B: OAuth Credentials (Alternative)

**What I need from you:**
- The entire contents of your OAuth credentials JSON file (as a string)

**I'll add to `.env`:**
```
GOOGLE_DRIVE_CREDENTIALS_JSON='{"type":"service_account","project_id":"...","private_key":"..."}'
```

### Optional: Google Drive Folder ID

**What I need from you:**
- The Google Drive folder ID where you want PDFs uploaded (optional - if not provided, uploads to root)

**How to get it:**
1. Open Google Drive
2. Navigate to or create the folder where you want PDFs
3. Open the folder
4. Look at the URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
5. Copy the `FOLDER_ID_HERE` part

**Tell me:**
- The folder ID (or say "skip" if you want uploads to root)

---

## 2. Canva Template Placeholder Field Names

Your Canva template needs these **exact placeholder field names** for Autofill:

### Text Fields (in your Canva template):
- `company_name` - Company name
- `description` - Company description  
- `location` - Company location/address
- `investment_date` - Investment date
- `investment_round` - Investment round (e.g., "PRE-SEED")
- `quarter` - Quarter (e.g., "Q2")
- `year` - Year (e.g., "2024")
- `founders` - Founders names (will be comma-separated)
- `co_investors` - Co-investors (will be comma-separated)
- `background` - Background/description text

### Image Fields (in your Canva template):
- `headshot` - Combined processed headshots (background removed, greyscale, combined)
- `logo` - Company logo
- `map` - Generated map image (optional - only if you want map in slide)

**To set up in Canva:**
1. Open your template in Canva
2. For each text element, add a placeholder like: `{{company_name}}` or use Canva's Autofill feature
3. For images, set up image placeholders with these names
4. Make sure your template matches the design you showed (orange sidebar, dark background, etc.)

**Tell me:**
- "I've set up the Canva template with these placeholders" OR
- If you need help with any specific field names

---

## 3. Notion Database Properties

Your Notion database needs these properties. The code will try multiple name variations, but here are the **exact names** that will work:

### Required Properties:

**For Google Drive Link:**
- Property name: `Google Drive Link` (or `Drive Link` or `PDF Link` or `Slide Link`)
- Property type: **URL**

**For DocSend Link:**
- Property name: `DocSend Link` (or `DocSend` or `Presentation Link`)
- Property type: **URL**

**For Status:**
- Property name: `Status` (or `Slide Status` or `Processing Status` or `Completion Status`)
- Property type: **Select** (with option "completed") OR **Text**

### How to Add in Notion:
1. Open your Portfolio Companies database
2. Click the "+" button to add a new property
3. Add each property with the exact names above
4. Set the correct types (URL for links, Select/Text for status)

**Tell me:**
- "I've added these properties to my Notion database" OR
- The exact property names you're using (if different)

---

## 4. Environment Variables Summary

Once you provide the information above, I'll add these to your `.env` file:

```bash
# Google Drive (one of these)
GOOGLE_SERVICE_ACCOUNT_PATH=/path/to/service-account.json
# OR
GOOGLE_DRIVE_CREDENTIALS_JSON='{...}'

# Optional
GOOGLE_DRIVE_FOLDER_ID=your_folder_id_here
```

---

## Quick Checklist

Please provide:

1. ✅ **Google Drive Service Account JSON file path** (or OAuth credentials)
2. ✅ **Google Drive Folder ID** (optional - say "skip" if not needed)
3. ✅ **Canva template confirmation** - "I've set up placeholders" or questions
4. ✅ **Notion database confirmation** - "I've added the properties" or the exact property names you're using

Once you give me this info, I'll:
- Add the environment variables to your `.env` file
- Update the code if your Notion property names are different
- Verify everything is set up correctly


