# Complete Requirements Checklist

## ✅ What You Need to Provide

### 1. API Keys & Credentials

#### **Required (Minimum to Test)**
- [ ] **Notion API Key**
  - Go to: https://www.notion.so/my-integrations
  - Click "New integration"
  - Name it (e.g., "Slauson Automation")
  - Copy the "Internal Integration Token"
  - Add to `.env` as `NOTION_API_KEY=secret_...`

#### **Optional (For Full Functionality)**

- [ ] **Remove.bg API Key** (for background removal)
  - Go to: https://www.remove.bg/api
  - Sign up for free account (50 free images/month)
  - Copy API key
  - Add to `.env` as `REMOVEBG_API_KEY=...`

- [ ] **OpenAI API Key** (for Granola insights)
  - Go to: https://platform.openai.com/api-keys
  - Create API key
  - Add to `.env` as `OPENAI_API_KEY=sk-...`

- [ ] **Canva API Key** (if available)
  - Contact Canva for API access (may require enterprise)
  - Add to `.env` as `CANVA_API_KEY=...`
  - Also need `CANVA_TEMPLATE_ID=...` (ID of your portfolio slide template)

- [ ] **DocSend API Key** (for automatic deck updates)
  - Check DocSend API documentation
  - Add to `.env` as `DOCSEND_API_KEY=...`
  - Also need:
    - `DOCSEND_INDIVIDUAL_DECK_ID=...` (where individual slides go)
    - `DOCSEND_MASTER_DECK_ID=...` (master presentation)

- [ ] **Granola API Key** (for meeting notes)
  - Check Granola API documentation
  - Add to `.env` as `GRANOLA_API_KEY=...`

---

### 2. Notion Setup

#### **Step 1: Create Integration**
- [ ] Created Notion integration (see API Keys above)
- [ ] Copied integration token to `.env`

#### **Step 2: Create Parent Page**
- [ ] Create a new page in Notion (or use existing)
- [ ] Get the page ID from URL:
  - URL looks like: `https://www.notion.so/Your-Page-Name-abc123def456...`
  - The ID is the part after the last `/` (e.g., `abc123def456...`)

#### **Step 3: Run Setup Script**
```bash
python setup_notion.py
```
- [ ] Enter your parent page ID when prompted
- [ ] Script creates:
  - Portfolio Companies database
  - Company template page
- [ ] Copy the IDs it gives you to `.env`:
  - `NOTION_DATABASE_ID=...`
  - `NOTION_TEMPLATE_PAGE_ID=...`

#### **Step 4: Share Database with Integration**
- [ ] Open the Portfolio Companies database
- [ ] Click "..." (three dots) → "Connections"
- [ ] Add your integration (the one you created in Step 1)
- [ ] Do the same for the template page

---

### 3. Environment File Setup

#### **Create `.env` file:**
```bash
cp .env.example .env
```

#### **Fill in your values:**
```env
# Required
NOTION_API_KEY=secret_your_token_here
NOTION_DATABASE_ID=your_database_id_here
NOTION_TEMPLATE_PAGE_ID=your_template_id_here

# Optional - Image Processing
REMOVEBG_API_KEY=your_removebg_key_here

# Optional - Canva
CANVA_API_KEY=your_canva_key_here
CANVA_TEMPLATE_ID=your_template_id_here

# Optional - DocSend
DOCSEND_API_KEY=your_docsend_key_here
DOCSEND_INDIVIDUAL_DECK_ID=your_individual_deck_id
DOCSEND_MASTER_DECK_ID=your_master_deck_id

# Optional - LLM for Insights
OPENAI_API_KEY=sk-your_openai_key_here

# Optional - Granola
GRANOLA_API_KEY=your_granola_key_here
```

---

### 4. Python Environment

#### **Install Python (if not already)**
- [ ] Python 3.8+ installed
- [ ] Verify: `python3 --version`

#### **Install Dependencies**
```bash
cd slauson-automation
pip install -r requirements.txt
```

- [ ] All packages installed successfully

---

### 5. Test Data (For Testing)

#### **To test the automation, you need:**
- [ ] **Headshot image** (JPG or PNG)
  - Example: `examples/headshot.jpg`
  - Will be processed (background removed, grayscale)

- [ ] **Company logo** (PNG preferred)
  - Example: `examples/logo.png`
  - Will be placed on slide

#### **Sample company data:**
You can use the example in `example_usage.py` or provide:
- Company name
- Website URL
- Description
- Address
- Investment date
- Co-investors (list)
- Number of employees
- First-time founder (true/false)

---

### 6. Canva Template (If Using Canva API)

#### **If you have Canva API access:**
- [ ] Create portfolio slide template in Canva
- [ ] Note the template ID
- [ ] Identify element positions:
  - Where headshot goes
  - Where logo goes
  - Text fields (company name, date, etc.)
- [ ] Add template ID to `.env`

#### **If you DON'T have Canva API:**
- [ ] The system will use alternative image processing
- [ ] You may need to manually create slides or use PIL-based generation
- [ ] This is fine - Notion integration will still work

---

### 7. DocSend Setup (If Using)

#### **If you want automatic DocSend updates:**
- [ ] DocSend account with API access
- [ ] Know where individual slides should be uploaded
- [ ] Know the master presentation document ID
- [ ] Add IDs to `.env`

#### **If you DON'T have DocSend API:**
- [ ] Notion integration still works
- [ ] Can manually upload slides later
- [ ] This is optional

---

## 🚀 Quick Start Path (Minimum Viable)

**To get it working with just Notion (minimum):**

1. ✅ Get Notion API key
2. ✅ Create parent page in Notion
3. ✅ Run `python setup_notion.py`
4. ✅ Add IDs to `.env`
5. ✅ Share database with integration
6. ✅ Test with `python test_integration.py`

**This gives you:**
- ✅ Automatic Notion database entries
- ✅ Automatic company folder creation
- ✅ All Notion automation working

**To add image processing:**
- ✅ Get Remove.bg API key (free tier available)
- ✅ Add to `.env`

**To add Canva slides:**
- ✅ Get Canva API access (may require enterprise)
- ✅ Create template
- ✅ Add to `.env`

**To add DocSend:**
- ✅ Get DocSend API access
- ✅ Add deck IDs to `.env`

**To add Granola:**
- ✅ Get Granola API access
- ✅ Add to `.env`

---

## 📋 Verification Checklist

Run this to verify everything is set up:

```bash
python test_integration.py
```

**Expected output:**
- ✅ All required configuration present
- ✅ Notion client initialized
- ✅ Notion database accessible
- ✅ Image processor initialized

---

## 🎯 What Works With What

| Feature | Requires | Status |
|---------|----------|--------|
| Notion Database Entry | Notion API Key + Database ID | ✅ Core |
| Notion Company Folder | Notion API Key + Template ID | ✅ Core |
| Image Background Removal | Remove.bg API Key | ⚠️ Optional |
| Image Grayscale | None (built-in) | ✅ Always works |
| Canva Slide Generation | Canva API Key + Template ID | ⚠️ Optional |
| DocSend Upload | DocSend API Key + Deck IDs | ⚠️ Optional |
| Granola Note Import | Granola API Key | ⚠️ Optional |
| AI Insights | OpenAI API Key | ⚠️ Optional |

**✅ = Works | ⚠️ = Optional enhancement**

---

## 🔧 Troubleshooting

### "NOTION_API_KEY not configured"
- Check `.env` file exists
- Verify key is correct (starts with `secret_`)
- No quotes around the value

### "Database not accessible"
- Run `setup_notion.py` to create database
- Share database with your integration
- Verify database ID is correct

### "Image processing failed"
- Remove.bg key is optional - images will be used as-is
- Check image file paths are correct
- Verify image files exist

### "Canva API failed"
- Canva API is optional
- System will use alternative method
- Or skip Canva entirely - Notion still works

---

## 📞 Need Help?

1. **Check configuration**: `python test_integration.py`
2. **Review logs**: Check error messages in results
3. **Verify API keys**: Test each service individually
4. **Check documentation**: See `QUICKSTART.md` for detailed steps

---

## Summary: Minimum to Get Started

**Absolute minimum (Notion only):**
1. Notion API key
2. Run `setup_notion.py`
3. Add IDs to `.env`
4. Share database with integration

**Recommended (Notion + Images):**
1. Everything above, plus:
2. Remove.bg API key (free)

**Full functionality:**
1. Everything above, plus:
2. Canva API (if available)
3. DocSend API (if available)
4. OpenAI API (for insights)
5. Granola API (for notes)

---

**You can start with just Notion and add other integrations later!**

