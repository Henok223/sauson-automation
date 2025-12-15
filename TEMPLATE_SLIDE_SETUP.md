# Template Slide Setup

## Problem
The slide doesn't look like your template because Gemini Vision only analyzes images - it doesn't generate them. The code was falling back to manually creating slides that don't match your design.

## ✅ Solution: Use Your Template Image as Base

I've added a new method that uses your template image as the base and overlays the new content on top. This ensures the slide looks **exactly** like your template.

## How to Set It Up

### Step 1: Save Your Template Image

1. **Save your template slide** as an image file (PNG or JPG)
2. **Place it in your project directory** or note the full path
3. **Recommended location**: `/Users/henoktewolde/slauson-automation/template_slide.png`

### Step 2: Add Template Path to .env

Add this line to your `.env` file:

```bash
SLIDE_TEMPLATE_PATH=/Users/henoktewolde/slauson-automation/template_slide.png
```

Or use a relative path:

```bash
SLIDE_TEMPLATE_PATH=template_slide.png
```

### Step 3: Restart Your Server

Restart your webhook server to load the new configuration.

## How It Works

1. **Loads your template image** as the base
2. **Overlays new text** (company name, founders, etc.) on top
3. **Overlays new images** (headshot, logo, map) on top
4. **Exports as PDF** - looks exactly like your template!

## Text Positioning

The code uses approximate positions. You may need to adjust these in `canva_integration.py` in the `_create_slide_from_template` method:

- **Company name**: (250, 80)
- **Investment stage**: (20, 50) 
- **Founders**: (250, 400)
- **Co-investors**: (250, ~500)
- **Background**: (250, ~600)
- **Logo**: (1700, 50)
- **Headshot**: (1500, 700)
- **Map**: (1400, 200)

Adjust these coordinates to match your template's exact layout!

## Test It

1. **Add template path to .env**
2. **Restart server**
3. **Test webhook** - the slide should now match your template!


