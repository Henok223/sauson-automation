# DocSend Setup - What You Need

## Required: DocSend API Key

You need to provide your **DocSend API Key** so the code can upload PDFs.

### How to Get It:

1. **Log into DocSend**
2. **Go to Settings** → **API** (or Developer settings)
3. **Generate/Copy your API Key**
4. **Share it with me** or add to `.env`:
   ```
   DOCSEND_API_KEY=your_actual_api_key_here
   ```

## Optional: Deck IDs

The code can work with or without these:

### Individual Deck ID (Optional)
- If you want all slides in one deck
- Currently: Each slide is uploaded as a separate document
- **Not required** - can leave as placeholder

### Master Deck ID (Optional)
- If you want to merge slides into a master presentation
- Currently: Not used in the workflow
- **Not required** - can leave as placeholder

## Current Workflow

The code currently:
1. Uploads each slide as a **separate DocSend document**
2. Returns the shareable link for that document
3. Stores the link in Notion

**You only need the API key for this to work!**

## What to Do

**Required:**
- Get your DocSend API Key
- Share it with me or add to `.env`:
  ```
  DOCSEND_API_KEY=your_api_key_here
  ```

**Optional:**
- Individual Deck ID (if you want all slides in one deck)
- Master Deck ID (if you want to merge into master presentation)

## Summary

**Minimum needed:**
- ✅ DocSend API Key

**Optional:**
- Individual Deck ID (for organizing slides)
- Master Deck ID (for master presentation)

Just get the API key and you're good to go!


