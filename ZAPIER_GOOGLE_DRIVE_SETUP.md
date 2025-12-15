# Zapier Google Drive Upload Setup

## Current Flow

```
1. Notion Entry (Status = "Ready")
   ↓
2. Zapier Trigger: New Notion Database Entry
   ↓
3. Zapier Action: Webhook (POST to your server)
   ├─ Sends company data
   ├─ Sends image URLs
   └─ Receives response with PDF (base64)
   ↓
4. Zapier Action: Google Drive Upload ⬅️ YOU NEED THIS STEP
   └─ Uploads PDF to Google Drive
```

---

## ✅ What Your Server Does

Your server receives the webhook and returns:
```json
{
  "success": true,
  "pdf_base64": "JVBERi0xLjQK...",  // PDF as base64
  "pdf_filename": "TechFlow_Solutions_slide.pdf",
  "pdf_size_bytes": 12345
}
```

---

## ⚠️ What You Need to Add in Zapier

You need to add a **Google Drive** action step in Zapier to upload the PDF.

---

## Step-by-Step: Add Google Drive Upload to Zapier

### Step 1: Add Google Drive Action

1. **In your Zap:**
   - After the Webhook step
   - Click **"+ Add Step"**
   - Search for **"Google Drive"**
   - Select **"Upload File"**

### Step 2: Connect Google Drive

1. **Connect your Google account** (if not already connected)
2. **Authorize Zapier** to access Google Drive

### Step 3: Configure Upload

**File:**
- **Source:** "Use data from previous step"
- **Field:** Select the `pdf_base64` field from webhook response
- **Note:** You may need to decode base64 first (see below)

**File Name:**
- Use: `pdf_filename` from webhook response
- Or: `{{company_data.name}}_slide.pdf`

**Folder:**
- Choose your Google Drive folder (e.g., "Portfolio Slides")
- Or use a dynamic folder based on company name

---

## ⚠️ Important: Base64 Decoding

Google Drive needs the **actual file**, not base64. You have two options:

### Option 1: Use "Code by Zapier" to Decode

1. **Add step:** "Code by Zapier" (between Webhook and Google Drive)
2. **Code:**
   ```javascript
   // Decode base64 to file
   const base64Data = inputData.pdf_base64;
   const filename = inputData.pdf_filename;
   
   // Convert base64 to binary
   const binaryData = Buffer.from(base64Data, 'base64');
   
   return {
     file_data: binaryData,
     filename: filename
   };
   ```
3. **Then use** `file_data` in Google Drive step

### Option 2: Use Zapier's Built-in Decoder

Some Zapier actions can handle base64 automatically. Check if Google Drive "Upload File" accepts base64 directly.

### Option 3: Return File URL Instead (Better for Zapier)

I can modify the webhook to:
1. Upload PDF to a temporary storage (S3, etc.)
2. Return a **download URL** instead of base64
3. Zapier can download from URL and upload to Google Drive

**Would you like me to implement Option 3?** It's cleaner for Zapier.

---

## Alternative: Use Zapier's "Create File from URL"

If we return a download URL, you can use:
- **Action:** "Google Drive - Create File from URL"
- **URL:** The PDF download URL from webhook response

---

## Quick Test

1. **Test your Zap:**
   - Add a test entry to Notion
   - Watch Zapier execute
   - Check if PDF appears in Google Drive

2. **Check Zapier logs:**
   - Look for errors in the Google Drive step
   - Verify file was uploaded

---

## Current Status

✅ **Webhook returns PDF** (as base64)  
⏳ **Need to add:** Google Drive upload step in Zapier  
⏳ **May need:** Base64 decoding step  

---

## Recommendation

**Option A: Add Google Drive step in Zapier** (you do this)
- Add "Google Drive - Upload File" action
- Use "Code by Zapier" to decode base64 if needed

**Option B: I modify webhook to return download URL** (I do this)
- Upload PDF to temporary storage
- Return URL instead of base64
- Easier for Zapier to handle

**Which do you prefer?** 🤔

