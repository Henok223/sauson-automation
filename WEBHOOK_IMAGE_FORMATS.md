# Webhook Image Format - What You'll Receive

## Yes, you'll receive `headshot_url` and `logo_url`!

The webhook accepts images in **multiple formats** for flexibility:

## Accepted Formats

### For Headshots:

✅ **`headshot_url`** - URL to headshot image (e.g., from Notion)
✅ **`headshot`** - Base64 encoded image OR URL
✅ **`headshots`** - Array of headshot URLs/images (for multiple founders)
✅ Can also be inside `company_data.headshot_url` or `company_data.headshot`

### For Logos:

✅ **`logo_url`** - URL to logo image (e.g., from Notion)
✅ **`logo`** - Base64 encoded image OR URL
✅ Can also be inside `company_data.logo_url` or `company_data.logo`

## Example Webhook Payload

```json
{
  "company_data": {
    "name": "Company Name",
    "description": "...",
    ...
  },
  "headshot_url": "https://notion.so/file/headshot.jpg",
  "logo_url": "https://notion.so/file/logo.png",
  "notion_page_id": "..."
}
```

OR with multiple headshots:

```json
{
  "company_data": {
    "name": "Company Name",
    "headshots": [
      "https://notion.so/file/founder1.jpg",
      "https://notion.so/file/founder2.jpg"
    ]
  },
  "headshot_url": "https://notion.so/file/headshot.jpg",  // Also accepted
  "logo_url": "https://notion.so/file/logo.png"
}
```

## What Happens to the Images

1. **Headshots**:
   - Downloaded from URL (if provided)
   - Processed with Gemini: background removal, greyscale, combined
   - Uploaded to Canva as `headshot` image field

2. **Logo**:
   - Downloaded from URL (if provided)
   - Uploaded to Canva as `logo` image field

3. **Map**:
   - Generated automatically by Gemini based on `company_data.address` or `company_data.location`
   - Uploaded to Canva as `map` image field (if you include it in your template)

## For Your Canva Template

Since you'll receive **URLs**, the code will:
1. Download the images from the URLs
2. Process headshots (if multiple, combine them)
3. Upload processed images to Canva
4. Link them to your template's image fields:
   - `headshot` - Combined processed headshots
   - `logo` - Company logo
   - `map` - Generated map (optional)

## Important Notes

- **URLs are preferred** - The code handles downloading from URLs automatically
- **Multiple headshots supported** - If you send multiple founders, they'll be combined
- **Notion file URLs work** - The code can download from Notion file URLs
- **Base64 also works** - If you send base64 encoded images, that's fine too

## What You Need in Your Canva Template

Make sure your Canva template has these **image placeholders**:
- `headshot` - For the combined processed headshots (bottom right)
- `logo` - For the company logo (top right)
- `map` - For the generated map (optional, upper right)

The code will automatically upload and link these images to your template!


