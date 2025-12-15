# How to Upload Headshots and Logos

## Yes! Upload Through Notion Database ✅

The easiest way is to **upload images directly to your Notion database**, and the webhook will automatically download and process them.

## How It Works

### Step 1: Upload to Notion Database

1. **Open your Notion database**
2. **Create or edit a company entry**
3. **Upload images to Notion properties**:
   - **Headshot**: Upload to a "Headshot" property (File type)
   - **Logo**: Upload to a "Logo" property (File type)

### Step 2: Notion Provides URLs

When you upload files to Notion:
- Notion stores them and provides **shareable URLs**
- These URLs look like: `https://s3.us-west-2.amazonaws.com/notion.so/...`

### Step 3: Zapier Sends URLs to Webhook

When Zapier triggers:
- It reads the Notion file URLs
- Sends them in the webhook payload as:
  ```json
  {
    "headshot_url": "https://notion.so/file/...",
    "logo_url": "https://notion.so/file/..."
  }
  ```

### Step 4: Your Server Downloads & Processes

Your webhook automatically:
- ✅ Downloads images from Notion URLs
- ✅ Processes headshots (Gemini: background removal, greyscale, combining)
- ✅ Uses images in slide generation

## Notion Database Setup

### Add These Properties:

1. **Headshot** (or `Headshot URL`)
   - Type: **File** (for uploading images)
   - OR **URL** (if you want to paste URLs manually)

2. **Logo** (or `Logo URL`)
   - Type: **File** (for uploading images)
   - OR **URL** (if you want to paste URLs manually)

### Multiple Headshots (Optional)

If you have multiple founders, you can:
- **Option A**: Upload multiple images to the Headshot property (Notion supports multiple files)
- **Option B**: Create separate properties: `Headshot 1`, `Headshot 2`, etc.
- **Option C**: Use a "Headshots" property with multiple files

The code will handle multiple headshots and combine them automatically!

## Zapier Field Mapping

In Zapier, map the Notion file fields:

```json
{
  "headshot_url": "{{1.Headshot}}",  // Notion file URL
  "logo_url": "{{1.Logo}}"           // Notion file URL
}
```

**Note**: Zapier automatically converts Notion file properties to URLs when you select them.

## Alternative: Manual URL Entry

If you prefer, you can also:
- Upload images elsewhere (Google Drive, Dropbox, etc.)
- Get the shareable URL
- Paste the URL into a Notion **URL** property
- Zapier sends that URL to the webhook

## Image Requirements

- **Format**: JPG, PNG (any common image format)
- **Size**: No strict limit, but reasonable sizes work best
- **Headshots**: Will be processed (background removed, greyscale, combined if multiple)
- **Logo**: Used as-is (resized to fit slide)

## Complete Flow

```
1. Upload headshot & logo to Notion database
   ↓
2. Zapier triggers when new entry created
   ↓
3. Zapier reads file URLs from Notion
   ↓
4. Zapier sends webhook with URLs:
   {
     "headshot_url": "https://notion.so/file/...",
     "logo_url": "https://notion.so/file/..."
   }
   ↓
5. Your server downloads images from URLs
   ↓
6. Processes headshots with Gemini
   ↓
7. Uses images in slide generation
```

## Summary

✅ **Upload images to Notion database** (easiest method)
✅ **Zapier automatically gets the URLs**
✅ **Your server downloads and processes them**
✅ **No manual URL copying needed!**

Just upload to Notion, and everything else is automatic! 🎉


