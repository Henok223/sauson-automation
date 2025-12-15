# Complete List of Notion Database Properties

## Properties You Likely Already Have ✅

These are for **input data** (company information):

1. **Name** (or `Company Name`)
   - Type: Title or Text
   - Purpose: Company name

2. **Description**
   - Type: Text or Rich Text
   - Purpose: Company description

3. **Location** (or `Address`)
   - Type: Text or Rich Text
   - Purpose: Company location/address

4. **Investment Date**
   - Type: Date
   - Purpose: Date of investment

5. **Investment Stage** (or separate `Investment Round`, `Quarter`, `Year`)
   - Type: Select or Text
   - Purpose: Investment stage (e.g., "PRE-SEED • Q2 2024")

6. **Founders**
   - Type: Text, Rich Text, or Multi-select
   - Purpose: Founder names

7. **Co-Investors**
   - Type: Text, Rich Text, or Multi-select
   - Purpose: Co-investor names

8. **Background**
   - Type: Text or Rich Text
   - Purpose: Company background/description

**Note**: You may have these with different names or types. That's fine! The webhook will send the data, and the code will use whatever field names are in the webhook payload.

---

## Properties You NEED TO ADD ⚠️

These are for **output data** (storing the results):

### 1. Google Drive Link
- **Property Name**: `Google Drive Link` (or `Drive Link` or `PDF Link` or `Slide Link`)
- **Type**: **URL**
- **Purpose**: Store the shareable Google Drive link to the generated PDF slide
- **Required**: ✅ Yes

### 2. DocSend Link
- **Property Name**: `DocSend Link` (or `DocSend` or `Presentation Link`)
- **Type**: **URL**
- **Purpose**: Store the shareable DocSend link to the generated PDF slide
- **Required**: ✅ Yes

### 3. Status
- **Property Name**: `Status` (or `Slide Status` or `Processing Status` or `Completion Status`)
- **Type**: **Select** (with "completed" option) OR **Text**
- **Purpose**: Track whether slide generation is complete
- **Required**: ✅ Yes

---

## Complete Checklist

### Input Properties (Likely Already Exist)
- [ ] Name / Company Name
- [ ] Description
- [ ] Location / Address
- [ ] Investment Date
- [ ] Investment Stage (or Investment Round, Quarter, Year)
- [ ] Founders
- [ ] Co-Investors
- [ ] Background

### Output Properties (Need to Add)
- [ ] **Google Drive Link** (URL type)
- [ ] **DocSend Link** (URL type)
- [ ] **Status** (Select with "completed" or Text type)

---

## Quick Setup Guide

### In Your Notion Database:

1. **Click the "+" button** to add a new property

2. **Add "Google Drive Link"**:
   - Name: `Google Drive Link`
   - Type: **URL**
   - Click "Create"

3. **Add "DocSend Link"**:
   - Name: `DocSend Link`
   - Type: **URL**
   - Click "Create"

4. **Add "Status"**:
   - Name: `Status`
   - Type: **Select**
   - Add option: `completed`
   - (Or use **Text** type if you prefer)
   - Click "Create"

---

## Property Name Matching

The code will try these property names in order:

**For Google Drive Link:**
1. `Google Drive Link`
2. `Drive Link`
3. `PDF Link`
4. `Slide Link`

**For DocSend Link:**
1. `DocSend Link`
2. `DocSend`
3. `Presentation Link`

**For Status:**
1. `Status`
2. `Slide Status`
3. `Processing Status`
4. `Completion Status`

**If you use different names**, just tell me and I'll update the code to match!

---

## Summary

**Total Properties Needed:**
- **Input properties**: ~8 (likely already exist)
- **Output properties**: **3 (need to add)**

**Action Required:**
Add these 3 properties to your Notion database:
1. Google Drive Link (URL)
2. DocSend Link (URL)
3. Status (Select with "completed" or Text)

That's it! Once you add these 3 properties, you're ready to test.


