# Google Gemini Integration for Slide Generation

## ✅ Added Gemini AI Support!

I've integrated Google Gemini to enhance slide generation with AI-powered design!

---

## Setup

### Step 1: Get Gemini API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

### Step 2: Add to Environment Variables

**In Render:**
1. Go to your service → "Environment" tab
2. Add variable:
   - Key: `GEMINI_API_KEY`
   - Value: `your_gemini_api_key_here`
3. Click "Save Changes"
4. Service will auto-redeploy

**Or locally in `.env`:**
```
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## How It Works

### With Gemini (when API key is set):

1. **Gemini analyzes** the company data
2. **Provides design guidance** (colors, layout, spacing)
3. **Enhanced slide generation** with better design
4. **Professional output** with AI-optimized layout

### Without Gemini (fallback):

- Uses standard PIL/Pillow method
- Still works, but less AI-enhanced

---

## What Gemini Enhances

✅ **Better color schemes** - AI-suggested professional colors  
✅ **Improved layout** - Optimized spacing and positioning  
✅ **Enhanced typography** - Better font choices and sizes  
✅ **Professional design** - AI-optimized slide appearance  

---

## Features

- **Automatic fallback** - If Gemini fails, uses standard method
- **No breaking changes** - Works without Gemini API key
- **Enhanced design** - Better slides when Gemini is available

---

## Test It

1. **Add Gemini API key** to Render environment variables
2. **Wait for redeploy** (~1-2 minutes)
3. **Create a new Notion entry** with Status = "Ready"
4. **Check the slide** - Should have enhanced design!

---

## Dependencies Added

- `google-generativeai>=0.3.0` - Google's Gemini API client

**Automatically installed when Render redeploys!**

---

## Notes

- Gemini API is **free tier available** for testing
- Falls back gracefully if API key not set
- Works with existing slide generation code

**Gemini integration is ready!** 🚀

