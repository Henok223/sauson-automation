# Notion Image Upload Guide

## Yes! Upload Actual Photos (Files) ✅

You should upload the **actual image files** to Notion, not URLs. Here's how:

## Step 1: Add Properties to Notion Database

Add these properties with these **exact names**:

1. **Property Name**: `headshot_url`
   - **Type**: **File** (not URL!)
   - **Purpose**: Upload headshot image files here

2. **Property Name**: `logo_url`
   - **Type**: **File** (not URL!)
   - **Purpose**: Upload logo image files here

**Note**: Even though the property is named `_url`, you're uploading **files**. Notion will automatically provide URLs when Zapier reads them.

## Step 2: Upload Images in Notion

1. **Open a company entry** in your Notion database
2. **Click on `headshot_url` property**
3. **Upload the headshot image file** (drag & drop or click to upload)
4. **Click on `logo_url` property**
5. **Upload the logo image file**

## Step 3: How It Works

### In Notion:
- You upload **actual image files** (JPG, PNG, etc.)
- Notion stores them and provides **shareable URLs** automatically

### In Zapier:
- When Zapier reads the Notion file property, it **automatically converts it to a URL**
- So `{{1.headshot_url}}` becomes: `https://notion.so/file/...`
- And `{{1.logo_url}}` becomes: `https://notion.so/file/...`

### In Your Webhook:
- Receives: `"headshot_url": "https://notion.so/file/..."`
- Downloads the image from that URL
- Processes it (Gemini: background removal, greyscale, combining)
- Uses it in slide generation

## Zapier Field Mapping

In Zapier webhook, use:

```json
{
  "headshot_url": "{{1.headshot_url}}",
  "logo_url": "{{1.logo_url}}"
}
```

Zapier will automatically convert the Notion file properties to URLs!

## Multiple Headshots

If you have multiple founders:

**Option 1**: Upload multiple files to `headshot_url` property
- Notion supports multiple files in one property
- Zapier will send all URLs
- Code will process and combine them

**Option 2**: Create separate properties
- `headshot_url_1`, `headshot_url_2`, etc.
- Upload one file to each
- Code can handle multiple headshot URLs

## Summary

✅ **Property Names**: `headshot_url` and `logo_url`
✅ **Property Type**: **File** (not URL type!)
✅ **What to Upload**: Actual image files (photos)
✅ **Zapier**: Automatically converts files to URLs
✅ **Your Server**: Downloads from URLs and processes

## Quick Checklist

- [ ] Add `headshot_url` property (File type) to Notion database
- [ ] Add `logo_url` property (File type) to Notion database
- [ ] Upload actual image files to these properties
- [ ] In Zapier, map: `{{1.headshot_url}}` and `{{1.logo_url}}`
- [ ] Done! Everything else is automatic

You upload the **files**, and everything else (URLs, downloading, processing) happens automatically! 🎉


