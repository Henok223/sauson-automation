# Notion Database - Example Entry

## Complete Example Data for Testing

Here's a complete example entry you can use to test your automation:

---

## Field Setup & Example Values

### 1. **Name** (Title Property)
**Type**: Title  
**Example Value**: 
```
TechFlow AI
```

### 2. **Description 1** (Text Property)
**Type**: Text (or Rich Text)  
**Example Value**:
```
TechFlow AI is revolutionizing the way businesses manage their workflow automation through intelligent AI-powered solutions. The platform combines machine learning with intuitive design to help teams automate repetitive tasks and focus on what matters most.
```

### 3. **Location** (Text Property)
**Type**: Text  
**Example Value**:
```
Los Angeles, CA
```
**Note**: Can also be full address like "123 Main St, Los Angeles, CA 90001"

### 4. **Investment Date 1** (Date Property)
**Type**: Date  
**Example Value**:
```
2024-03-15
```
or
```
March 15, 2024
```

### 5. **Investment Stage** (Text Property)
**Type**: Text  
**Example Value**:
```
PRE-SEED
```
**Other Options**: `SEED`, `SERIES A`, `SERIES B`, `SERIES C`, `BRIDGE`, etc.

### 6. **Founders** (Multi-Select Property)
**Type**: Multi-select  
**Example Values** (create these as select options):
- `Sarah Chen`
- `Michael Rodriguez`
- `David Kim`

**How to Set Up**:
1. Create the multi-select property
2. Add options: "Sarah Chen", "Michael Rodriguez", "David Kim"
3. Select all three for this example entry

**Alternative**: If you want comma-separated text instead:
- **Type**: Text
- **Example Value**: `Sarah Chen, Michael Rodriguez, David Kim`

### 7. **Co-Investors 1** (Multi-Select Property)
**Type**: Multi-select  
**Example Values** (create these as select options):
- `Andreessen Horowitz`
- `Sequoia Capital`
- `First Round Capital`

**How to Set Up**:
1. Create the multi-select property
2. Add options: "Andreessen Horowitz", "Sequoia Capital", "First Round Capital"
3. Select all three for this example entry

**Alternative**: If you want comma-separated text instead:
- **Type**: Text
- **Example Value**: `Andreessen Horowitz, Sequoia Capital, First Round Capital`

### 8. **Background** (Text Property)
**Type**: Text (or Rich Text)  
**Example Value**:
```
TechFlow AI was founded in 2023 by a team of former Google and Microsoft engineers who saw the need for more intelligent automation tools. The company has quickly gained traction in the enterprise market, with over 500 companies using their platform. Their unique approach combines natural language processing with visual workflow builders, making automation accessible to non-technical users.
```

### 9. **Google Drive Link** (URL Property)
**Type**: URL  
**Example Value** (will be auto-populated):
```
https://drive.google.com/file/d/1a2b3c4d5e6f7g8h9i0j/view?usp=sharing
```
**Note**: This will be automatically filled by the automation after processing

### 10. **DocSend Link** (URL Property)
**Type**: URL  
**Example Value** (will be auto-populated):
```
https://docsend.com/view/abc123xyz
```
**Note**: This will be automatically filled by the automation after processing

### 11. **Status** (Select or Text Property)
**Type**: Select (recommended) or Text  
**Example Options** (if Select):
- `pending`
- `processing`
- `completed`
- `error`

**Example Value** (for testing):
```
pending
```

**How to Set Up**:
1. Create Select property
2. Add options: "pending", "processing", "completed", "error"
3. Set initial value to "pending"

### 12. **headshot_url** (File Property)
**Type**: File  
**What to Upload**: 
- Upload actual headshot image files (JPG, PNG)
- Can upload multiple files if you have multiple founders
- Example: Upload `sarah_headshot.jpg`, `michael_headshot.jpg`, `david_headshot.jpg`

**Note**: 
- Notion will automatically provide URLs
- Zapier will convert these to URLs when sending to webhook
- Code will download and process them

### 13. **logo_url** (File Property)
**Type**: File  
**What to Upload**:
- Upload actual logo image file (PNG recommended, transparent background)
- Example: Upload `techflow_logo.png`

**Note**: 
- Notion will automatically provide URLs
- Zapier will convert these to URLs when sending to webhook
- Code will download and use it in the slide

---

## Complete Example Entry Summary

| Field Name | Type | Example Value |
|------------|------|---------------|
| **Name** | Title | `TechFlow AI` |
| **Description 1** | Text | `TechFlow AI is revolutionizing...` |
| **Location** | Text | `Los Angeles, CA` |
| **Investment Date 1** | Date | `2024-03-15` |
| **Investment Stage** | Text | `PRE-SEED` |
| **Founders** | Multi-select | `Sarah Chen`, `Michael Rodriguez`, `David Kim` |
| **Co-Investors 1** | Multi-select | `Andreessen Horowitz`, `Sequoia Capital`, `First Round Capital` |
| **Background** | Text | `TechFlow AI was founded in 2023...` |
| **Google Drive Link** | URL | *(auto-filled)* |
| **DocSend Link** | URL | *(auto-filled)* |
| **Status** | Select | `pending` |
| **headshot_url** | File | *(upload image files)* |
| **logo_url** | File | *(upload image file)* |

---

## Quick Setup Steps

1. **Create the properties** in your Notion database with the exact names above
2. **Set the correct types** (Title, Text, Date, Multi-select, URL, File, Select)
3. **Create a test entry** with the example values above
4. **Upload images**:
   - Upload headshot images to `headshot_url` property
   - Upload logo image to `logo_url` property
5. **Set Status** to `pending`
6. **Trigger from Zapier** to test!

---

## Alternative Example (Different Company)

If you want a second example for testing:

| Field Name | Example Value |
|------------|---------------|
| **Name** | `GreenEnergy Solutions` |
| **Description 1** | `GreenEnergy Solutions provides sustainable energy management systems for commercial buildings, reducing carbon footprint by up to 40% while cutting energy costs.` |
| **Location** | `Dallas, TX` |
| **Investment Date 1** | `2024-06-20` |
| **Investment Stage** | `SEED` |
| **Founders** | `Emma Watson`, `James Park` |
| **Co-Investors 1** | `Kleiner Perkins`, `Greylock Partners` |
| **Background** | `Founded in 2022, GreenEnergy Solutions has deployed their technology in over 200 commercial buildings across the Southwest. The company's proprietary AI algorithms optimize energy consumption in real-time, making it a leader in the smart building space.` |
| **Status** | `pending` |

---

## Notes

- **Multi-select vs Text**: If you use multi-select, Zapier will send it as an array. If you use text with commas, the code will split it automatically.
- **Date Format**: Notion dates can be in various formats - the code will handle them
- **Images**: Make sure images are uploaded as **files** (not URLs) - Notion will provide URLs automatically
- **Status**: Start with `pending` - it will be updated to `completed` after processing

---

## Testing Checklist

- [ ] All properties created with correct names
- [ ] All properties have correct types
- [ ] Test entry created with example data
- [ ] Headshot images uploaded to `headshot_url`
- [ ] Logo image uploaded to `logo_url`
- [ ] Status set to `pending`
- [ ] Zapier webhook configured
- [ ] Ready to test! 🚀

