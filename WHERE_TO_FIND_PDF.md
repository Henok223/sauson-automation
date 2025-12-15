# Where to Find the Uploaded PDF

## 📁 Google Drive Location

The PDF will appear in the **Google Drive folder you configured in Zapier**.

---

## How to Find It

### Step 1: Check Your Zapier Google Drive Step

1. Go to: https://zapier.com/app/dashboard
2. Click your Zap
3. Find the **"Google Drive"** step (should be after the Webhook step)
4. Click on it to see the configuration
5. Look for **"Folder"** setting - that's where the file will be!

### Common Locations:

- **"My Drive"** (root folder)
- **"Portfolio Slides"** (if you created a specific folder)
- **"Slauson Portfolio"** (if you named it that)
- **Any folder you selected** in the Zapier Google Drive step

---

## If You Didn't Set a Folder

If you didn't specify a folder in Zapier, the file will be in:

**"My Drive"** (the root of your Google Drive)

---

## How to Find It

### Method 1: Search Google Drive

1. Go to: https://drive.google.com
2. Click the **search bar** at the top
3. Type: `TechFlow_Solutions_slide.pdf` (or your company name)
4. Press Enter
5. The file should appear!

### Method 2: Check Recent Files

1. Go to: https://drive.google.com
2. Click **"Recent"** in the left sidebar
3. Look for the PDF file (should be at the top if just uploaded)

### Method 3: Check Specific Folder

1. Go to: https://drive.google.com
2. Navigate to the folder you set in Zapier
3. Look for the PDF file

---

## File Name Format

The PDF will be named:
- `TechFlow_Solutions_slide.pdf` (if company name is "TechFlow Solutions")
- `[Company_Name]_slide.pdf` (format: company name + "_slide.pdf")

---

## If You Can't Find It

### Check Zapier Task History

1. Go to Zapier → Your Zap → Task History
2. Click on the most recent task
3. Click on the **Google Drive step**
4. Check if it shows:
   - ✅ **Success** - File was uploaded
   - ❌ **Error** - Something went wrong

### If There's an Error:

Common issues:
- **"Folder not found"** - Folder path is wrong
- **"Permission denied"** - Google Drive connection issue
- **"Invalid file"** - Base64 decoding issue

**Fix:**
- Re-check Google Drive folder path in Zapier
- Re-connect Google Drive account in Zapier
- Check if base64 decoding is needed (see ZAPIER_GOOGLE_DRIVE_SETUP.md)

---

## Verify Upload Location in Zapier

### To Check/Change the Folder:

1. **Edit your Zap:**
   - Go to Zapier → Your Zap
   - Click **"Edit"**

2. **Find Google Drive Step:**
   - Click on the Google Drive action step

3. **Check "Folder" Field:**
   - See what folder is selected
   - Change it if needed
   - Click **"Continue"** and **"Save"**

---

## Quick Test

After creating a Notion entry:

1. **Wait 1-2 minutes**
2. **Go to Google Drive:** https://drive.google.com
3. **Search for:** `slide.pdf` or your company name
4. **Check Recent files** if not found

---

## Expected Result

You should see:
- ✅ **File name:** `[Company_Name]_slide.pdf`
- ✅ **Location:** The folder you set in Zapier (or "My Drive")
- ✅ **File type:** PDF
- ✅ **Upload time:** Within 1-2 minutes of creating Notion entry

---

## Still Can't Find It?

1. **Check Zapier Task History** - See if Google Drive step succeeded
2. **Check the folder** you configured in Zapier
3. **Search Google Drive** for the file name
4. **Check "Recent"** files in Google Drive

**The file will be in whatever folder you configured in the Zapier Google Drive step!** 📁

