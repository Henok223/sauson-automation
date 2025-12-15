# Backend API Inputs

The `/webhook/onboarding` endpoint accepts POST requests with JSON payloads. It supports multiple input formats:

## Input Formats

### Format 1: Nested Structure
```json
{
  "company_data": {
    "name": "Company Name",
    "description": "Company description",
    "address": "City, State",
    "investment_date": "2024-01-15",
    "investment_round": "SEED",
    "quarter": "Q2",
    "year": "2024",
    "founders": "John Doe, Jane Smith",
    "co_investors": "Investor A, Investor B",
    "background": "Company background information"
  },
  "headshot_url": "https://example.com/headshot.jpg",
  "logo_url": "https://example.com/logo.png",
  "notion_page_id": "optional-page-id",
  "notion_created_time": "2024-01-01T00:00:00Z",
  "notion_last_edited": "2024-01-01T00:00:00Z"
}
```

### Format 2: Flat Structure (Zapier-friendly)
```json
{
  "company_data__name": "Company Name",
  "company_data__description": "Company description",
  "company_data__address": "San Francisco, CA",
  "company_data__investment_date": "2024-01-15",
  "company_data__investment_round": "SEED",
  "company_data__quarter": "Q2",
  "company_data__year": "2024",
  "company_data__founders": "John Doe, Jane Smith",
  "company_data__co_investors": "Investor A, Investor B",
  "company_data__background": "Company background information",
  "headshot_url": "https://example.com/headshot.jpg",
  "logo_url": "https://example.com/logo.png",
  "notion_page_id": "optional-page-id"
}
```

## Required Fields

### Company Information
- **name** (required): Company name
- **address** or **location** (required): City location (e.g., "San Francisco, CA" or just "San Francisco")
- **founders** (required): Comma-separated string or array of founder names
- **co_investors** (required): Comma-separated string or array of co-investor names
- **background** or **description** (required): Company background/description text

### Investment Information
- **investment_round** (optional): Investment round (e.g., "SEED", "PRE-SEED", "SERIES A")
- **quarter** (optional): Quarter (e.g., "Q1", "Q2", "Q3", "Q4")
- **year** (optional): Year (e.g., "2024")
- **investment_stage** (optional): Combined format (e.g., "SEED Q2, 2024") - if provided, overrides round/quarter/year
- **investment_date** (optional): Date of investment

### Images
- **headshot** or **headshot_url** (optional): Base64 encoded image or URL to headshot image
- **logo** or **logo_url** (optional): Base64 encoded image or URL to logo image

### Notion Integration (Optional)
- **notion_page_id**: Notion page ID to update after processing
- **notion_created_time**: Creation timestamp
- **notion_last_edited**: Last edited timestamp

## Image Input Formats

Images can be provided in two ways:

1. **URL**: `"headshot_url": "https://example.com/image.jpg"`
2. **Base64**: `"headshot": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."`

## Field Name Variations

The backend is flexible and accepts multiple field name variations:

- `address` or `location` → used for map location
- `description` or `background` → used for background text
- `founders` → can be comma-separated string or array
- `co_investors` → can be comma-separated string or array

## Investment Stage Format

The investment stage can be provided in two ways:

1. **Separate fields**:
   ```json
   {
     "investment_round": "SEED",
     "quarter": "Q2",
     "year": "2024"
   }
   ```

2. **Combined field**:
   ```json
   {
     "investment_stage": "SEED Q2, 2024"
   }
   ```

If both are provided, `investment_stage` takes precedence.

## Example Request

```bash
curl -X POST http://localhost:5001/webhook/onboarding \
  -H "Content-Type: application/json" \
  -d '{
    "company_data__name": "Astranis",
    "company_data__description": "Astranis Space Technologies is a private American satellite manufacturer...",
    "company_data__address": "San Francisco, CA",
    "company_data__investment_round": "SEED",
    "company_data__quarter": "Q2",
    "company_data__year": "2024",
    "company_data__founders": "John Gedmark, Ryan McLinko",
    "company_data__co_investors": "Blackrock, Fidelity",
    "company_data__background": "Astranis Space Technologies is a private American satellite manufacturer...",
    "headshot_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
    "logo_url": "https://images.unsplash.com/photo-1611262588024-d12430b98920?w=400&h=400&fit=crop",
    "notion_page_id": "test-page-id-12345"
  }'
```

## Response Format

```json
{
  "success": true,
  "google_drive_link": "https://drive.google.com/file/d/...",
  "docsend_link": "https://docsend.com/view/...",
  "notion_page_id": "page-id",
  "errors": []
}
```

## Notes

- If images are not provided, placeholder images will be created
- The backend automatically processes headshots (background removal, greyscale, combining multiple)
- The backend generates a map based on the city location
- The slide is created using HTML → PDF (with Canva and Gemini fallbacks)
- Results are uploaded to Google Drive and optionally DocSend
- Notion records are updated if `notion_page_id` is provided

