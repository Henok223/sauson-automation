# Google Drive & DocSend Links - Explanation

## Two Different Things

### 1. Where to Upload (Configuration) 📁

This is where you tell the code **WHERE** to upload the PDFs.

**For Google Drive:**
- You can specify a folder ID in `.env` as `GOOGLE_DRIVE_FOLDER_ID`
- If not specified, uploads go to the **root** of Google Drive
- You already said "upload to root", so we left this empty ✅

**For DocSend:**
- No folder concept - you just upload documents
- Each upload creates its own document/link

### 2. Where to Store Links (Notion Properties) 🔗

This is where the code **STORES** the shareable links after uploading.

**The Notion properties are OUTPUT fields:**
- `Google Drive Link` - Stores the link to the uploaded PDF
- `DocSend Link` - Stores the link to the uploaded PDF

**These are NOT for specifying where to upload!**

## How It Works

### Step 1: Upload (Configuration)
```
Code uploads PDF → Google Drive root (or specified folder)
Code uploads PDF → DocSend
```

### Step 2: Get Links
```
Code gets shareable link from Google Drive
Code gets shareable link from DocSend
```

### Step 3: Store Links (Notion Properties)
```
Code updates Notion record:
  - Google Drive Link property = "https://drive.google.com/file/d/..."
  - DocSend Link property = "https://docsend.com/view/..."
```

## What You Need to Do

### For Upload Location (Already Done ✅)
- Google Drive: Uploading to root (no folder ID needed)
- DocSend: No folder needed

### For Notion Properties (Need to Add)
Add these properties to **STORE** the links:
- `Google Drive Link` (URL type) - Will contain the link after upload
- `DocSend Link` (URL type) - Will contain the link after upload

## Example Flow

1. **Webhook receives company data**
2. **Code generates slide PDF**
3. **Code uploads to Google Drive root** → Gets link: `https://drive.google.com/file/d/abc123`
4. **Code uploads to DocSend** → Gets link: `https://docsend.com/view/xyz789`
5. **Code updates Notion:**
   - `Google Drive Link` = `https://drive.google.com/file/d/abc123`
   - `DocSend Link` = `https://docsend.com/view/xyz789`
   - `Status` = `completed`

## Summary

**Notion Properties are for STORING links (output), not specifying upload location!**

- ✅ Upload location: Already configured (root for Google Drive)
- ⚠️ Notion properties: Need to add to store the resulting links

You don't need to send any folder links - just add the 3 properties to Notion to store the results!


