# How to View Your Canva Slide

## ✅ Fixed! PDF Now Available in Response

I've fixed the issue - the PDF is now included in the webhook response as base64-encoded data.

---

## Quick Test (Wait ~30 seconds for Render to redeploy)

After Render redeploys (takes ~30-60 seconds), run:

```bash
cd ~/slauson-automation
./test_and_download.sh
```

This will:
1. ✅ Test the webhook
2. ✅ Automatically extract the PDF
3. ✅ Save it as `TechFlow_Solutions_slide.pdf` (or similar)

---

## Manual Method

### Step 1: Test Webhook

```bash
curl -X POST https://sauson-automation-3.onrender.com/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d @test_real_payload.json \
  -o response.json
```

### Step 2: Extract PDF

```bash
python3 download_slide.py response.json
```

The PDF will be saved in the current directory!

---

## What Changed

- ✅ PDF bytes are now read **before** the temp directory is cleaned up
- ✅ PDF is included in webhook response as `pdf_base64`
- ✅ Filename is included as `pdf_filename`
- ✅ File size is included as `pdf_size_bytes`

---

## Response Format

```json
{
  "success": true,
  "pdf_base64": "JVBERi0xLjQK...",  // ← PDF as base64
  "pdf_filename": "TechFlow_Solutions_slide.pdf",  // ← Filename
  "pdf_size_bytes": 12345,  // ← File size
  ...
}
```

---

## From Zapier

When Zapier triggers the webhook, the response will include the PDF. You can:

1. **Use "Code by Zapier"** to extract and save the PDF
2. **Upload to Google Drive** using the base64 data
3. **Email the PDF** as an attachment

---

**Wait ~30 seconds for Render to redeploy, then test!** 🚀

