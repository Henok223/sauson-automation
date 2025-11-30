# Test Data for Notion Database

## Sample Company Entry

Use this data to create a test entry in your Notion "Portfolio Companies" database:

---

## Required Fields

### **Name** (Title)
```
TechFlow Solutions
```

### **Status** (Select)
```
Ready
```
**Important:** Must be "Ready" to trigger the Zap!

### **Website** (URL)
```
https://techflow.io
```

### **Description** (Text)
```
AI-powered workflow automation platform helping teams streamline operations and increase productivity through intelligent process optimization. Founded by experienced entrepreneurs with backgrounds at Google and Microsoft.
```

### **Address** (Text)
```
123 Innovation Drive, San Francisco, CA 94105
```

### **Investment Date** (Date)
```
November 15, 2024
```
or
```
2024-11-15
```

### **Co-Investors** (Text or Multi-select)
```
Sequoia Capital, Andreessen Horowitz, Y Combinator
```

### **Number of Employees** (Number)
```
45
```

### **First Time Founder** (Checkbox)
```
☐ (unchecked - false)
```
or leave unchecked

### **Investment Memo** (URL)
```
https://docs.google.com/document/d/example123
```

---

## Image Fields

### **Headshot** (Files & Media)

**Option 1: Use a sample image URL**
```
https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop
```

**Option 2: Upload a real image**
- Download a sample headshot
- Upload directly to Notion

### **Logo** (Files & Media)

**Option 1: Use a sample image URL**
```
https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=400&h=400&fit=crop
```

**Option 2: Upload a real logo**
- Download a sample logo
- Upload directly to Notion

---

## Quick Copy-Paste Template

```
Name: TechFlow Solutions
Status: Ready
Website: https://techflow.io
Description: AI-powered workflow automation platform helping teams streamline operations and increase productivity through intelligent process optimization. Founded by experienced entrepreneurs with backgrounds at Google and Microsoft.
Address: 123 Innovation Drive, San Francisco, CA 94105
Investment Date: November 15, 2024
Co-Investors: Sequoia Capital, Andreessen Horowitz, Y Combinator
Number of Employees: 45
First Time Founder: (leave unchecked)
Investment Memo: https://docs.google.com/document/d/example123
Headshot: [Upload image or use URL]
Logo: [Upload image or use URL]
```

---

## Alternative Sample Companies

### Company 2: GreenTech Energy

```
Name: GreenTech Energy
Status: Ready
Website: https://greentech.energy
Description: Renewable energy solutions for commercial buildings, reducing carbon footprint by 40% through smart solar and battery storage systems.
Address: 456 Green Street, Austin, TX 78701
Investment Date: December 1, 2024
Co-Investors: Kleiner Perkins, First Round Capital
Number of Employees: 28
First Time Founder: ☑ (checked - true)
Investment Memo: https://docs.google.com/document/d/example456
```

### Company 3: HealthAI

```
Name: HealthAI
Status: Ready
Website: https://healthai.com
Description: AI-powered diagnostic tools for early disease detection, using machine learning to analyze medical imaging with 95% accuracy.
Address: 789 Medical Plaza, Boston, MA 02115
Investment Date: October 20, 2024
Co-Investors: General Catalyst, Accel Partners
Number of Employees: 62
First Time Founder: ☐ (unchecked)
Investment Memo: https://docs.google.com/document/d/example789
```

---

## How to Test

### Step 1: Create Entry in Notion

1. Open your **Portfolio Companies** database in Notion
2. Click **"New"** to create a new entry
3. Fill in all the fields above (use TechFlow Solutions data)
4. **Important:** Set **Status = "Ready"**
5. Upload or add images for Headshot and Logo
6. **Save** the entry

### Step 2: Watch Zapier

1. Go to your Zapier dashboard
2. Your Zap should automatically trigger
3. Watch it execute:
   - ✅ Notion trigger fires
   - ✅ Filter checks Status = "Ready"
   - ✅ Webhook sends data to your server
   - ✅ Google Drive uploads the PDF

### Step 3: Check Results

1. **Render Logs:**
   - Go to: https://dashboard.render.com/
   - Click your service → "Logs"
   - Look for webhook processing messages

2. **Google Drive:**
   - Check your Google Drive folder
   - Look for: `TechFlow_Solutions_slide.pdf`

3. **Zapier History:**
   - Check Zapier task history
   - Verify all steps completed successfully

---

## Troubleshooting

### Zapier Didn't Trigger?

- ✅ Check Status field = "Ready" (exact match, case-sensitive)
- ✅ Verify Zap is turned ON
- ✅ Check if filter is blocking the entry

### Webhook Failed?

- ✅ Check Render logs for errors
- ✅ Verify webhook URL is correct
- ✅ Check if images downloaded successfully

### PDF Not in Google Drive?

- ✅ Check Zapier task history for errors
- ✅ Verify Google Drive step is configured
- ✅ Check if base64 decoding worked

---

## Expected Results

After adding the entry:

1. ✅ **Zapier triggers** within seconds
2. ✅ **Webhook processes** the data
3. ✅ **Canva slide generated** (PDF)
4. ✅ **PDF uploaded to Google Drive**
5. ✅ **Entry appears in your drive folder**

---

**Ready to test? Create the entry in Notion with Status = "Ready"!** 🚀

