# New Workflow Implementation

## Overview

The codebase has been updated to implement a complete workflow for automated slide generation with the following steps:

1. **Receive webhook POST** with company data + Notion fields
2. **Download & process headshots** using Gemini 3 Pro (background removal, greyscale, combining multiple headshots)
3. **Generate map** using Gemini 3 Pro with location pin
4. **Call Canva API** to create/populate slide design with company text fields
5. **Generate/convert to PDF**
6. **Upload PDF to Google Drive** (return shareable link)
7. **Upload PDF to DocSend** (return shareable link)
8. **Update Notion record** with both URLs + "completed" status
9. **Return JSON response** to Zapier (success flag + links)

## New Files Created

### `google_drive_integration.py`
- Handles Google Drive API authentication (supports service account or OAuth)
- Uploads PDFs and generates shareable links
- Creates folders if needed

## Updated Files

### `image_processor.py`
- **New method**: `process_headshots_with_gemini()` - Uses Gemini 3 Pro to:
  - Remove backgrounds from headshots
  - Convert to greyscale
  - Combine multiple headshots in overlapping style (like the slide design)
- **New method**: `generate_map_with_gemini()` - Uses Gemini 3 Pro to:
  - Generate stylized map with location pin
  - Create orange-outlined US map with yellow location marker

### `canva_integration.py`
- Updated `create_portfolio_slide()` to properly use Canva API:
  - Upload images to Canva
  - Duplicate template
  - Use Autofill API to populate text fields
  - Export as PDF
- Supports map image upload if provided

### `notion_integration.py`
- **New method**: `update_company_record()` - Updates Notion records with:
  - Google Drive link
  - DocSend link
  - Status (set to "completed")

### `webhook_listener.py`
- Completely rewritten workflow handler
- Implements all 9 steps of the new workflow
- Handles multiple headshots (for multiple founders)
- Generates map based on company location
- Uploads to both Google Drive and DocSend
- Updates Notion record
- Returns JSON response with success flag and links

### `config.py`
- Added Google Drive configuration:
  - `GOOGLE_DRIVE_CREDENTIALS_JSON` - JSON string of credentials
  - `GOOGLE_SERVICE_ACCOUNT_PATH` - Path to service account JSON file
  - `GOOGLE_DRIVE_FOLDER_ID` - Optional folder ID to upload to

### `requirements.txt`
- Added Google Drive API dependencies:
  - `google-auth>=2.23.0`
  - `google-auth-oauthlib>=1.1.0`
  - `google-auth-httplib2>=0.1.1`
  - `google-api-python-client>=2.100.0`

## Environment Variables Required

Add these to your `.env` file:

```bash
# Existing
GEMINI_API_KEY=your_gemini_api_key
CANVA_API_KEY=your_canva_api_key
CANVA_TEMPLATE_ID=your_template_id
NOTION_API_KEY=your_notion_api_key
DOCSEND_API_KEY=your_docsend_api_key

# New - Google Drive (choose one method)
# Method 1: Service Account (recommended for server-side)
GOOGLE_SERVICE_ACCOUNT_PATH=/path/to/service-account.json

# Method 2: OAuth Credentials (JSON string)
GOOGLE_DRIVE_CREDENTIALS_JSON='{"type":"service_account","project_id":"..."}'

# Optional
GOOGLE_DRIVE_FOLDER_ID=your_folder_id  # Upload to specific folder
```

## Webhook Payload Format

The webhook expects the following JSON structure:

```json
{
  "company_data": {
    "name": "Company Name",
    "description": "Company description",
    "address": "Los Angeles, CA",  // Used for map generation
    "investment_date": "2024-12-01",
    "investment_round": "PRE-SEED",
    "quarter": "Q2",
    "year": "2024",
    "founders": ["Founder 1", "Founder 2"],  // Array of founder names
    "co_investors": ["Investor 1", "Investor 2"],  // Array or comma-separated string
    "background": "Company background text...",
    "headshots": ["url1", "url2"]  // Optional: array of headshot URLs (if multiple)
  },
  "headshot": "base64_or_url",  // Single headshot (or use headshots array)
  "headshot_url": "https://...",  // Alternative field name
  "logo": "base64_or_url",
  "logo_url": "https://...",
  "notion_page_id": "page_id_here",  // Required for Notion update
  "notion_created_time": "...",
  "notion_last_edited": "..."
}
```

## Response Format

The webhook returns:

```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": "https://docsend.com/view/...",
  "notion_page_id": "page_id",
  "errors": []  // Array of any errors encountered
}
```

## Canva Template Requirements

Your Canva template should have the following placeholders for Autofill:

**Text Fields:**
- `company_name` - Company name
- `description` - Company description
- `location` - Company location/address
- `investment_date` - Investment date
- `investment_round` - Investment round (e.g., "PRE-SEED")
- `quarter` - Quarter (e.g., "Q2")
- `year` - Year (e.g., "2024")
- `founders` - Founders names (comma-separated)
- `co_investors` - Co-investors (comma-separated)
- `background` - Background/description text

**Image Fields:**
- `headshot` - Combined processed headshots
- `logo` - Company logo
- `map` - Generated map image (optional)

## Notion Database Properties

Your Notion database should have these properties (names can vary, code tries multiple):

**URL Properties:**
- "Google Drive Link" or "Drive Link" or "PDF Link" or "Slide Link"
- "DocSend Link" or "DocSend" or "Presentation Link"

**Status Property:**
- "Status" or "Slide Status" or "Processing Status" or "Completion Status"
  - Can be a Select field (with "completed" option) or Text field

## Installation

1. Install new dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Google Drive credentials:
   - **Option A (Service Account - Recommended)**: 
     - Go to Google Cloud Console
     - Create a service account
     - Download JSON key file
     - Set `GOOGLE_SERVICE_ACCOUNT_PATH` to the file path
   
   - **Option B (OAuth)**:
     - Follow Google OAuth setup
     - Set `GOOGLE_DRIVE_CREDENTIALS_JSON` with credentials JSON

3. Update your `.env` file with all required API keys

4. Restart your webhook server

## Testing

Test the webhook with a POST request:

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data": {
      "name": "Test Company",
      "description": "Test description",
      "address": "Los Angeles",
      "investment_date": "2024-12-01",
      "investment_round": "PRE-SEED",
      "quarter": "Q2",
      "year": "2024",
      "founders": ["Founder 1", "Founder 2"],
      "co_investors": ["Investor 1"],
      "background": "Test background"
    },
    "headshot_url": "https://example.com/headshot.jpg",
    "logo_url": "https://example.com/logo.png",
    "notion_page_id": "your_page_id"
  }'
```

## Notes

- **Gemini 3 Pro**: The code uses Gemini 2.0 Flash or Gemini 1.5 Pro (falls back to gemini-pro-vision)
- **Multiple Headshots**: Supports multiple founders by passing an array in `company_data.headshots`
- **Map Generation**: Extracts city name from address if full address is provided
- **Error Handling**: Each step has error handling and continues even if one step fails
- **Fallbacks**: If Gemini fails, falls back to manual image processing methods

## Troubleshooting

1. **Google Drive upload fails**: Check service account permissions and folder access
2. **Gemini processing fails**: Verify `GEMINI_API_KEY` is set and has proper quota
3. **Canva API fails**: Falls back to alternative PIL-based slide generation
4. **Notion update fails**: Check property names match your database schema


