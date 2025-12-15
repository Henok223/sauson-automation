# Canva Image Auto-Upload - How It Works

## Yes! The Code Automatically Uploads and Attaches Images

You just need to create **image placeholders** in your Canva template with the correct names. The code handles everything else!

## How It Works

### Step 1: You Create Image Placeholders in Canva

In your Canva template, just create **image frames/placeholders** and name them:
- `headshot` - For headshots (bottom right)
- `logo` - For logo (top right)  
- `map` - For map (optional, upper right)

**That's it!** You don't need to upload any images manually.

### Step 2: The Code Does Everything Automatically

When the webhook receives `headshot_url` and `logo_url`:

1. **Downloads images** from the URLs
2. **Processes headshots** with Gemini (background removal, greyscale, combining)
3. **Generates map** automatically from company location
4. **Uploads images to Canva** via API (`_upload_image()` method)
5. **Gets upload IDs** from Canva
6. **Links images to your placeholders** via Autofill API using the field names

### Step 3: Images Appear in Your Template

The Autofill API links the uploaded images to your placeholders by matching the field names:
- Uploaded headshot → Linked to `headshot` placeholder
- Uploaded logo → Linked to `logo` placeholder
- Uploaded map → Linked to `map` placeholder (if you have one)

## What You Need to Do

### In Canva Template:

1. **Create image placeholders/frames** where images should go
2. **Name them exactly:**
   - `headshot`
   - `logo`
   - `map` (optional)

### In Canva Data Autofill:

When setting up Data Autofill:
- Link your image placeholders to image fields with these exact names:
  - Image placeholder → `headshot`
  - Image placeholder → `logo`
  - Image placeholder → `map`

## Code Flow

```python
# 1. Download images from URLs
headshot_path = download_from_url(headshot_url)
logo_path = download_from_url(logo_url)

# 2. Process headshots
combined_headshot_bytes = process_with_gemini(headshot_paths)

# 3. Generate map
map_bytes = generate_map_with_gemini(location)

# 4. Upload to Canva
headshot_upload_id = canva._upload_image(combined_headshot_bytes, "headshot")
logo_upload_id = canva._upload_image(logo_bytes, "logo")
map_upload_id = canva._upload_image(map_bytes, "map")

# 5. Link via Autofill
autofill_data = {
    "images": {
        "headshot": headshot_upload_id,  # Links to your 'headshot' placeholder
        "logo": logo_upload_id,          # Links to your 'logo' placeholder
        "map": map_upload_id              # Links to your 'map' placeholder
    }
}
canva._autofill_design(design_id, company_data, headshot_upload_id, logo_upload_id, map_upload_id)
```

## Important Notes

✅ **You don't need to upload images manually** - The code does it automatically
✅ **Just create empty image placeholders** - Name them correctly
✅ **Field names must match exactly** - `headshot`, `logo`, `map` (lowercase)
✅ **Images are processed automatically** - Headshots are combined, backgrounds removed, etc.

## What Happens If Images Are Missing?

- If `headshot_url` is missing → Creates a placeholder gray image
- If `logo_url` is missing → Creates a placeholder gray image
- Map is always generated automatically from company location

## Summary

**You:** Create image placeholders in Canva, name them `headshot`, `logo`, `map`
**Code:** Downloads, processes, uploads, and links images automatically
**Result:** Images appear in your template automatically!

No manual image upload needed! 🎉


