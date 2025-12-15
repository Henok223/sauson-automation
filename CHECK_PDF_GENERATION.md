# Check PDF Generation - Debugging Guide

## If PDF Still Shows File Path

The PDF might still be using the old PIL method. Here's how to check:

### Step 1: Check Render Logs

After creating a new Notion entry, check Render logs for:

**Good signs:**
```
Successfully converted slide to PDF using img2pdf, size: XXXXX bytes
```

**Bad signs:**
```
Warning: img2pdf not available, using PIL PDF (may have issues)
Error converting to PDF: ...
```

### Step 2: Verify img2pdf is Installed

The dependency is in `requirements.txt`, but Render needs to:
1. **Redeploy** (automatic after git push)
2. **Install dependencies** (takes 1-2 minutes)

### Step 3: Check What's Happening

Look for these messages in Render logs:

1. **"Successfully converted slide to PDF using img2pdf"** ✅
   - This means it worked!

2. **"Warning: img2pdf not available"** ⚠️
   - img2pdf not installed yet (wait for redeploy)
   - Or installation failed

3. **"Error converting to PDF"** ❌
   - Check the error message
   - May need to fix the conversion code

### Step 4: Test Directly

You can test the PDF generation locally:

```bash
cd ~/slauson-automation
source venv/bin/activate
pip install img2pdf reportlab
python -c "from canva_integration import CanvaIntegration; c = CanvaIntegration(); print('Can import')"
```

---

## Alternative: Use Reportlab

I've also added `reportlab` as a fallback. It's more reliable than PIL's PDF export.

**If img2pdf fails, reportlab will try:**
- Creates PDF canvas
- Draws the image on it
- Saves as proper PDF

---

## What to Do Now

1. **Wait for Render to redeploy** (~1-2 minutes after git push)
2. **Create a new Notion entry** with Status = "Ready"
3. **Check Render logs** for PDF conversion messages
4. **Check Google Drive** for the PDF

**If it still shows file path:**
- Check Render logs for error messages
- Share the error message and I'll fix it

---

## Expected Log Messages

**Success:**
```
Successfully converted slide to PDF using img2pdf, size: 123456 bytes
```

**Or:**
```
Successfully converted slide to PDF using reportlab
```

**If you see these, the PDF should be correct!** ✅

