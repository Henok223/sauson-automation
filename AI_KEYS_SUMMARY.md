# AI Keys Usage Summary

## Quick Answer: **Gemini is OPTIONAL (with fallbacks)**

The code uses AI keys, but **they're not strictly required** - the system has fallbacks.

---

## AI Keys Used

### 1. **Google Gemini API Key** (OPTIONAL - Has Fallbacks)
**Used for:**
- Map generation (creates stylized map images with location pins)
- Headshot processing (background removal + grayscale via Gemini Vision)

**What happens WITHOUT it:**
- ✅ Map generation: Creates a simple placeholder map (gray box with orange border)
- ✅ Headshot processing: Falls back to local `rembg` ML model + manual processing
- ✅ **System still works fully** - just uses fallbacks

**Get it:**
- Free tier available: https://aistudio.google.com/apikey
- No credit card needed

**Environment Variable:**
```bash
GEMINI_API_KEY=AIzaSy...
```

---

### 2. **OpenAI API Key** (OPTIONAL - Backup Only)
**Used for:**
- Background removal (backup method if remove.bg fails)
- Granola meeting insights (if using Granola integration)

**What happens WITHOUT it:**
- ✅ Background removal: Falls back to `rembg` or `remove.bg`
- ✅ Granola insights: Skipped (if not using Granola)
- ✅ **Not critical** - multiple fallbacks exist

**Get it:**
- Paid service: https://platform.openai.com/api-keys
- Requires billing setup

**Environment Variable:**
```bash
OPENAI_API_KEY=sk-proj-...
```

---

### 3. **Remove.bg API Key** (OPTIONAL - Has Fallbacks)
**Used for:**
- Professional background removal for headshots

**What happens WITHOUT it:**
- ✅ Falls back to local `rembg` ML model (free, works well)
- ✅ **System still works** - just uses local ML instead

**Get it:**
- Free tier: 50 images/month: https://www.remove.bg/api
- No credit card needed for free tier

**Environment Variable:**
```bash
REMOVEBG_API_KEY=your_key
```

---

## Local ML (No API Key Needed)

### **rembg** (Built-in, No Key Required)
- Local machine learning model for background removal
- Installed via `requirements.txt`
- Works offline, no API calls
- Free and unlimited
- **This is the default fallback** if APIs aren't available

---

## Summary Table

| AI Service | Required? | What It Does | Fallback If Missing |
|------------|-----------|--------------|---------------------|
| **Gemini API** | ❌ Optional | Map generation, headshot processing | Placeholder map + local rembg |
| **OpenAI API** | ❌ Optional | Background removal backup | rembg or remove.bg |
| **Remove.bg API** | ❌ Optional | Professional background removal | Local rembg ML model |
| **rembg (local)** | ✅ Built-in | Background removal ML model | None (this IS the fallback) |

---

## Minimum Setup (No AI Keys Needed)

**You can run the system with ZERO AI keys:**
- ✅ Uses local `rembg` for background removal
- ✅ Creates placeholder maps
- ✅ Fully functional slide generation
- ✅ All features work

**Recommended Setup (Better Quality):**
- ✅ Add Gemini API key (free) → Better maps + headshot processing
- ✅ Add Remove.bg key (free tier) → Better background removal

**Full Setup (Best Quality):**
- ✅ Gemini API key
- ✅ Remove.bg API key
- ✅ OpenAI API key (backup)

---

## Code Evidence

Looking at `webhook_listener.py`:

```python
# Gemini map generation - has fallback
try:
    map_bytes = ImageProcessor.generate_map_with_gemini(location, map_path)
except Exception as e:
    print(f"Warning: Gemini map generation failed: {e}")
    # Creates placeholder map instead
    img = Image.new('RGB', (800, 600), color=(40, 40, 40))
    # ... creates simple placeholder

# Gemini headshot processing - has fallback
try:
    combined_headshot_bytes = ImageProcessor.process_headshots_with_gemini(...)
except Exception as e:
    print(f"Warning: Gemini headshot processing failed: {e}")
    # Falls back to raw headshot - HTML generator will process it
    combined_headshot_path = headshot_paths[0]
```

**Conclusion:** All AI features have fallbacks. The system works without any AI keys!

---

## Recommendation for New Company

**Start with:**
1. ✅ No AI keys (system works with fallbacks)
2. ✅ Add Gemini API key (free, improves quality)
3. ✅ Add Remove.bg key (free tier, better backgrounds)

**Skip:**
- OpenAI API key (not critical, multiple fallbacks exist)

---

## Cost

- **Gemini API**: Free tier available (generous)
- **Remove.bg**: Free tier (50 images/month)
- **OpenAI**: Paid (not recommended unless needed)
- **rembg (local)**: Free, unlimited, built-in

**Total cost for recommended setup: $0/month** (all free tiers)

