# Gemini API Key Setup - REQUIRED

## ✅ Yes, You Need a Gemini API Key!

The slide generation **strictly requires** a Gemini API key. It will **not work without it**.

---

## Step 1: Get Your Gemini API Key

1. **Go to Google AI Studio**:
   - Visit: https://aistudio.google.com/apikey
   - Sign in with your Google account

2. **Create API Key**:
   - Click **"Create API Key"**
   - Select your Google Cloud project (or create a new one)
   - Copy the API key

3. **Free Tier Available**:
   - Gemini API has a generous free tier
   - No credit card required for basic usage

---

## Step 2: Add to Your .env File

Add this line to your `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

**Example:**
```bash
GEMINI_API_KEY=AIzaSyAbCdEfGhIjKlMnOpQrStUvWxYz1234567
```

---

## Step 3: Verify It's Working

Check that the API key is loaded:

```bash
# In Python
python -c "from config import Config; print('Gemini API Key:', 'SET' if Config.GEMINI_API_KEY else 'NOT SET')"
```

---

## What Happens Without API Key?

If `GEMINI_API_KEY` is not set, the code will **raise an error**:

```
ValueError: GEMINI_API_KEY is required for slide generation. 
Please set GEMINI_API_KEY in your .env file.
```

**No fallback** - Gemini is required!

---

## Why Gemini is Required

The slide generation uses **Gemini Vision** to:
1. Analyze the template slide design
2. Understand the layout and styling
3. Generate a new slide with company data
4. Match the exact design from your template

This ensures slides match your design perfectly!

---

## Troubleshooting

### "GEMINI_API_KEY is required"
- ✅ Check `.env` file exists
- ✅ Check `GEMINI_API_KEY=...` is in `.env`
- ✅ No spaces around the `=` sign
- ✅ Restart your server after adding the key

### "google-generativeai not installed"
```bash
pip install google-generativeai
```

### "API key invalid"
- ✅ Check you copied the full key
- ✅ Check for extra spaces or quotes
- ✅ Verify key is active in Google AI Studio

### "Quota exceeded"
- ✅ Check your API usage in Google AI Studio
- ✅ Free tier has limits - may need to wait or upgrade

---

## Quick Checklist

- [ ] Got API key from https://aistudio.google.com/apikey
- [ ] Added `GEMINI_API_KEY=...` to `.env` file
- [ ] Installed `google-generativeai` package
- [ ] Restarted server
- [ ] Verified key is loaded

---

## Need Help?

1. **Get API Key**: https://aistudio.google.com/apikey
2. **Documentation**: https://ai.google.dev/docs
3. **Pricing**: https://ai.google.dev/pricing

**Gemini API Key is REQUIRED - no exceptions!** 🔑


