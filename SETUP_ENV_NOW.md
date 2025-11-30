# Setup .env File - Required!

## ✅ .env File Created

I've created the `.env` file for you. Now you need to add your API keys.

## Required: Notion API Key

1. **Get your Notion API key:**
   - Go to: https://www.notion.so/my-integrations
   - Click "New integration" (or use existing)
   - Copy the "Internal Integration Token"
   - It starts with `secret_`

2. **Add to .env file:**
   ```bash
   cd ~/slauson-automation
   nano .env
   ```
   
   Or open it in any text editor and add:
   ```
   NOTION_API_KEY=secret_your_token_here
   ```

## Optional: Database ID

If you want the automation to create Notion entries, you'll also need:

1. **Get your database ID:**
   - Open your "Burton test" database in Notion
   - Copy the URL
   - The ID is the long string after the last `/`
   - Example: `https://notion.so/Your-Page-abc123def456...`
   - The ID is: `abc123def456...`

2. **Add to .env:**
   ```
   NOTION_DATABASE_ID=abc123def456...
   ```

## Quick Setup

**Minimum required (just to test webhook):**
```env
NOTION_API_KEY=secret_your_token_here
```

**For full automation:**
```env
NOTION_API_KEY=secret_your_token_here
NOTION_DATABASE_ID=your_database_id_here
```

## After Adding Keys

1. **Restart your server:**
   - Press Ctrl+C to stop the current server
   - Run: `python webhook_listener.py` again

2. **Test again:**
   - Create a new entry in Notion
   - Watch the server logs

## Check Current Error

**Look at your server terminal** - you should now see a more detailed error message that will tell us exactly what's missing.

---

**Add your NOTION_API_KEY to the .env file and restart the server!**

