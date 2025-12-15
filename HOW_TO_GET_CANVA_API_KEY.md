# How to Get Your Canva API Key

## Step-by-Step Instructions

### 1. Go to Canva Developers Portal
Visit: **https://developers.canva.com/**

### 2. Sign In or Create Account
- Sign in with your Canva account
- If you don't have an account, create one (it's free)

### 3. Create a New App
1. Once logged in, go to **"My Apps"** section
2. Click **"Create a new app"** or **"New App"**
3. Fill in the app details:
   - **App Name**: e.g., "Slauson Automation"
   - **Description**: e.g., "Portfolio company slide generation"
   - **App Type**: Select appropriate type (usually "Server-side app" or "API app")

### 4. Skip Optional Steps (If Prompted)
- **Translation/UI Strings**: This is **optional** - you can click "Skip" or "Continue"
- **App Store Listing**: Optional for internal use

### 5. Get Your API Credentials
After creating the app, you'll see one of these:

#### Option A: API Key (Bearer Token)
- Look for **"API Key"** or **"Access Token"**
- It will be a long string like: `OC-AZrV8PyvUWAe...` or similar
- **Copy this key** - you'll need it for your `.env` file

#### Option B: OAuth Credentials (Client ID/Secret)
- If you see **Client ID** and **Client Secret** instead:
  - You already have these from before:
    - `CANVA_CLIENT_ID=OC-AZrV8PyvUWAe`
    - `CANVA_CLIENT_SECRET=YOUR_CANVA_CLIENT_SECRET_HERE`
  - We can use OAuth authentication instead

### 6. Add to Your .env File
Once you have the API key, add it to your `.env` file:

```bash
CANVA_API_KEY=your_api_key_here
CANVA_TEMPLATE_ID=DAG7c2W8dpV
```

## Important Notes

- **Keep your API key secret** - Don't share it publicly or commit it to GitHub
- **API keys have rate limits** - Check Canva's documentation for limits
- **Some features may require OAuth** - If API key doesn't work, we'll use OAuth

## If You Already Have OAuth Credentials

If you see Client ID/Secret instead of an API key, we can use OAuth. The code can be updated to:
1. Use your existing Client ID/Secret
2. Generate an access token
3. Use that token for API calls

## Troubleshooting

### "I don't see an API Key"
- Check if you need to enable API access in app settings
- Look for "Access Token" or "Bearer Token" instead
- Some apps use OAuth only - we can configure that

### "Translation step is blocking me"
- **Skip it** - It's optional for API access
- Click "Skip" or "Continue" to proceed

### "I see Client ID/Secret but no API Key"
- That's fine! We can use OAuth authentication
- Share your Client ID/Secret and I'll update the code

## Next Steps

1. **Get your API key** from Canva Developers Portal
2. **Add it to `.env`** as `CANVA_API_KEY`
3. **Test the webhook** - It should now use Canva API

## Quick Links

- **Canva Developers Portal**: https://developers.canva.com/
- **Canva API Documentation**: https://developers.canva.com/docs
- **Your App Dashboard**: https://developers.canva.com/apps


