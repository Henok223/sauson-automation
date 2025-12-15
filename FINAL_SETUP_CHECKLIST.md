# Final Setup Checklist - What's Next

## ✅ What's Already Done

1. **Google Drive Integration**
   - ✅ Service account path configured
   - ✅ Code ready to upload PDFs

2. **Canva Template**
   - ✅ Template ID added: `DAG7c2W8dpY`
   - ✅ Data Autofill fields set up
   - ✅ Code updated to support `investment_stage` field
   - ✅ Position-based image replacement ready

3. **Code Implementation**
   - ✅ Gemini headshot processing
   - ✅ Gemini map generation (matching your style)
   - ✅ Canva API integration
   - ✅ Google Drive upload
   - ✅ DocSend upload
   - ✅ Notion update functionality

## 🔧 What's Still Needed

### 1. Canva API Key ⚠️

**Status:** Still shows placeholder in `.env`

**What you need:**
- Get your Canva API key from Canva's developer dashboard
- Once you have it, I can add it to `.env`

**How to get it:**
1. Go to [Canva Developers](https://www.canva.com/developers/)
2. Create an app or use existing one
3. Get your API key
4. Share it with me or add to `.env`:
   ```
   CANVA_API_KEY=your_actual_api_key_here
   ```

### 2. Notion Database Properties ⚠️

**Status:** Need to confirm you've added these properties

**Required properties in your Notion database:**
- `Google Drive Link` (or `Drive Link` or `PDF Link` or `Slide Link`) - Type: URL
- `DocSend Link` (or `DocSend` or `Presentation Link`) - Type: URL  
- `Status` (or `Slide Status` or `Processing Status`) - Type: Select (with "completed" option) or Text

**Action needed:**
- Confirm you've added these properties, OR
- Tell me the exact property names you're using (I can update the code)

### 3. Test the Workflow 🧪

Once Canva API key is added, you can test with a webhook.

## 📋 Quick Action Items

**Priority 1: Canva API Key**
- [ ] Get Canva API key
- [ ] Add to `.env` (I can do this if you share it)

**Priority 2: Notion Properties**
- [ ] Add Google Drive Link property (URL type)
- [ ] Add DocSend Link property (URL type)
- [ ] Add Status property (Select or Text type)
- [ ] Confirm property names match code expectations

**Priority 3: Test**
- [ ] Send test webhook
- [ ] Verify slide generation
- [ ] Check Google Drive upload
- [ ] Check DocSend upload
- [ ] Verify Notion update

## 🚀 Once Everything is Configured

The workflow will:
1. ✅ Receive webhook with company data
2. ✅ Download & process headshots (Gemini: background removal, greyscale, combine)
3. ✅ Generate map (Gemini: stylized map with location pin)
4. ✅ Create Canva slide (populate via Data Autofill API)
5. ✅ Export as PDF
6. ✅ Upload to Google Drive (return shareable link)
7. ✅ Upload to DocSend (return shareable link)
8. ✅ Update Notion record (add links + set status to "completed")
9. ✅ Return JSON response to Zapier (success + links)

## 🎯 Next Steps Right Now

**Tell me:**
1. Do you have your Canva API key? (If yes, share it and I'll add it)
2. Have you added the Notion properties? (If yes, confirm the exact names)

Once those are done, we're ready to test!


