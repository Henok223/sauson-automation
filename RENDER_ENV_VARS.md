# Render Environment Variables Setup

## Required Environment Variables

Go to your Render dashboard → `sauson-automation-3` → **Environment** tab and add these:

### Template Paths (Required)
```
SLIDE_TEMPLATE_PATH=templates/SLAUSON&CO.Template.pdf
MAP_TEMPLATE_PATH=templates/map_template.pdf
```

### API Keys (Required)
```
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_DRIVE_FOLDER_ID=your_google_drive_folder_id
NOTION_API_KEY=your_notion_api_key
```

### Canva (Optional - for Canva fallback)
```
CANVA_CLIENT_ID=your_canva_client_id
CANVA_CLIENT_SECRET=your_canva_client_secret
CANVA_REFRESH_TOKEN=your_canva_refresh_token
CANVA_ACCESS_TOKEN=your_canva_access_token
```

### Google Drive (Required)
```
GOOGLE_DRIVE_CREDENTIALS_JSON={"type":"service_account",...}  # Full JSON as string
```
OR
```
GOOGLE_SERVICE_ACCOUNT_PATH=path/to/service-account.json
```

### Optional
```
DOCSEND_API_KEY=your_docsend_api_key
REMOVEBG_API_KEY=your_removebg_api_key
FLASK_DEBUG=false
PORT=5001  # Render sets this automatically, but you can override
```

## Quick Setup Steps

1. **Go to Render Dashboard**: https://dashboard.render.com
2. **Click on `sauson-automation-3` service**
3. **Go to "Environment" tab**
4. **Add each variable** using the "Add Environment Variable" button
5. **Save changes** - Render will automatically redeploy

## Template Files

The template files are now in the `templates/` directory in your repository:
- `templates/SLAUSON&CO.Template.pdf` (main slide template)
- `templates/map_template.pdf` (map template)

These will be available at those paths on Render after deployment.

## Testing

After setting environment variables, test the webhook:
```bash
curl https://sauson-automation-3.onrender.com/health
```

Should return: `{"status": "healthy"}`

