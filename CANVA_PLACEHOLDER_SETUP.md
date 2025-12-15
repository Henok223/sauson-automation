# Canva Placeholder Setup - Exact Instructions

## For TEXT Fields

### Option 1: Use Placeholder Text (Easier)
**Put the placeholder text directly in your text boxes:**

- In the text box where company name should go → type: `{{company_name}}`
- In the text box for description → type: `{{description}}`
- In the text box for location → type: `{{location}}`
- In the text box for investment date → type: `{{investment_date}}`
- In the text box for investment round → type: `{{investment_round}}`
- In the text box for quarter → type: `{{quarter}}`
- In the text box for year → type: `{{year}}`
- In the text box for founders → type: `{{founders}}`
- In the text box for co-investors → type: `{{co_investors}}`
- In the text box for background → type: `{{background}}`

**Example:**
- Your "Company Name" text box should literally contain: `{{company_name}}`
- Your "Description" text box should contain: `{{description}}`

The `{{}}` tells Canva (and our code) that this is a placeholder that will be replaced with actual data.

### Option 2: Use Canva's Autofill Feature
If Canva has an Autofill UI feature:
- Select the text element
- Use the Autofill/Data feature to link it to a field named `company_name`, `description`, etc.

**I recommend Option 1 (placeholder text) as it's simpler and more reliable.**

---

## For IMAGE Placeholders

**NO - Don't create text fields!** 

Instead, create **actual image placeholders/frames**:

1. **Add an image frame/placeholder** where the image should go:
   - For headshots (bottom right) → Add an image frame/placeholder
   - For logo (top right) → Add an image frame/placeholder  
   - For map (upper right, optional) → Add an image frame/placeholder

2. **Name these image placeholders** (not as text, but as the placeholder name):
   - The headshot image frame should be named: `headshot`
   - The logo image frame should be named: `logo`
   - The map image frame should be named: `map`

3. **How to name image placeholders in Canva:**
   - Select the image frame/placeholder
   - Look for a "Name" or "ID" field in the properties panel
   - OR use Canva's Autofill feature to assign it to an image field named `headshot`, `logo`, `map`

**Visual Example:**
- Text box with `{{company_name}}` → This is a TEXT placeholder
- Image frame/placeholder named `headshot` → This is an IMAGE placeholder
- Image frame/placeholder named `logo` → This is an IMAGE placeholder

---

## Summary

### TEXT Fields:
✅ **DO THIS:** Put placeholder text like `{{company_name}}` directly in your text boxes
❌ **DON'T:** Just leave text boxes empty or put sample text

### IMAGE Fields:
✅ **DO THIS:** Create actual image frames/placeholders and name them `headshot`, `logo`, `map`
❌ **DON'T:** Create text fields with placeholder names for images

---

## Quick Setup Checklist

**Text Elements:**
- [ ] Company name text box contains: `{{company_name}}`
- [ ] Description text box contains: `{{description}}`
- [ ] Location text box contains: `{{location}}`
- [ ] Investment date text box contains: `{{investment_date}}`
- [ ] Investment round text box contains: `{{investment_round}}`
- [ ] Quarter text box contains: `{{quarter}}`
- [ ] Year text box contains: `{{year}}`
- [ ] Founders text box contains: `{{founders}}`
- [ ] Co-investors text box contains: `{{co_investors}}`
- [ ] Background text box contains: `{{background}}`

**Image Elements:**
- [ ] Image frame for headshots exists and is named: `headshot`
- [ ] Image frame for logo exists and is named: `logo`
- [ ] Image frame for map exists and is named: `map` (optional)

---

## Still Confused?

If you're not sure how to:
- **Add placeholder text to text boxes**: Just type `{{field_name}}` directly in the text box
- **Create image placeholders**: Add an image element/frame, then name it in the properties panel
- **Name image placeholders**: Look for "Name", "ID", or "Autofill" options when you select the image frame

Let me know if you need clarification on any step!


