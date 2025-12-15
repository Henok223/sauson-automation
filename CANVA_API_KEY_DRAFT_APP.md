# Getting Canva API Key from Draft App

## ✅ You DON'T Need to Submit for Review!

For **internal use** (like your automation), you can get API credentials from a **draft app** without submitting for review.

## Where to Find Your API Key

### Option 1: In Your App Settings
1. Go to your app dashboard: https://developers.canva.com/apps
2. Click on your app (`AAG7deiE3dQ`)
3. Look for these tabs/sections:
   - **"Settings"** or **"Configuration"**
   - **"Credentials"** or **"Authentication"**
   - **"API Keys"** or **"Access Tokens"**

### Option 2: Check the App Overview
1. In your app dashboard, look at the **overview/summary page**
2. You might see:
   - **"API Key"** or **"Bearer Token"**
   - **"Client ID"** and **"Client Secret"** (for OAuth)

### Option 3: Look for "Generate API Key" Button
1. Some apps have a button to **"Generate API Key"** or **"Create Access Token"**
2. Click it to generate your API key
3. Copy it immediately (you might not be able to see it again)

## What You're Looking For

### API Key Format
- Usually starts with `OC-` or similar
- Long string of characters
- Used as: `Authorization: Bearer YOUR_API_KEY`

### OAuth Credentials (Alternative)
If you see **Client ID** and **Client Secret** instead:
- We can use OAuth authentication
- You already have these:
  - `CANVA_CLIENT_ID=OC-AZrV8PyvUWAe`
  - `CANVA_CLIENT_SECRET=YOUR_CANVA_CLIENT_SECRET_HERE`

## Quick Steps

1. **Skip the submission page** - You don't need it for API access
2. **Go to your app settings** - Look for credentials/authentication
3. **Find API Key or generate one** - Copy it
4. **Add to .env**: `CANVA_API_KEY=your_key_here`

## If You Can't Find an API Key

Some Canva apps use **OAuth only** (no direct API key). In that case:
- We'll use your Client ID/Secret
- Generate an access token programmatically
- Use that token for API calls

## Next Steps

1. **Don't worry about submission** - It's only needed for public apps
2. **Check your app settings** for API credentials
3. **Share what you find** - API key, or we'll set up OAuth


