# Fixing 500 Error

## ✅ Good News: Webhook is Working!

Your webhook is receiving requests from Zapier! The 500 error means the server received the request but encountered an error while processing it.

## 🔍 Check Server Terminal

Look at your server terminal - you should now see detailed error information including:
- Error message
- Error type
- Full traceback

This will tell us exactly what's wrong.

## Common Causes of 500 Errors

### 1. Missing .env File or API Keys

**Check if .env exists:**
```bash
cd ~/slauson-automation
ls -la .env
```

**If missing, create it:**
```bash
cp .env.example .env
```

**Then add your API keys:**
- `NOTION_API_KEY` (required)
- `NOTION_DATABASE_ID` (required)
- Other keys as needed

### 2. Missing Required Configuration

The error might be:
- `NOTION_API_KEY not configured`
- `NOTION_DATABASE_ID not configured`
- Missing required fields in the payload

### 3. Image Download Issues

If headshot_url or logo_url are invalid:
- URLs might be inaccessible
- Notion file URLs might need authentication
- Files might not exist

### 4. Notion API Issues

- Invalid API key
- Database not shared with integration
- Missing permissions

## 🔧 Quick Fixes

### Check Error Details

**Look at your server terminal** - the error message will show exactly what's wrong.

### Common Fixes:

1. **Missing .env file:**
   ```bash
   cd ~/slauson-automation
   cp .env.example .env
   # Then add your NOTION_API_KEY
   ```

2. **Missing API key:**
   - Get from: https://www.notion.so/my-integrations
   - Add to .env: `NOTION_API_KEY=secret_...`

3. **Missing database ID:**
   - Run: `python setup_notion.py`
   - Or get from Notion database URL
   - Add to .env: `NOTION_DATABASE_ID=...`

## 📋 Next Steps

1. **Check server terminal** for the detailed error message
2. **Share the error** and I'll help you fix it
3. **Common fixes** are listed above

---

**The webhook connection is working!** We just need to fix the processing error. What error message do you see in your server terminal?

