# Canva OAuth URLs

## Standard Canva OAuth Endpoints

Based on Canva's API documentation, here are the OAuth URLs you need:

### Authorization Server URL
```
https://www.canva.com/api/oauth/authorize
```

### Token Exchange URL
```
i 
```

## Alternative Endpoints (if above don't work)

Some Canva implementations use:
- Authorization: `https://www.canva.com/oauth/authorize`
- Token: `https://www.canva.com/api/oauth/token`

## What to Enter in Your Provider Setup

1. **Authorization Server URL**: 
   ```
   https://www.canva.com/api/oauth/authorize
   ```

2. **Token Exchange URL**:
   ```
   https://api.canva.com/rest/v1/oauth/token
   ```

## Additional OAuth Settings

You'll also need:
- **Client ID**: `OC-AZrV8PyvUWAe` (you already have this)
- **Client Secret**: `YOUR_CANVA_CLIENT_SECRET_HERE` (you already have this)
- **Redirect URI**: Usually `https://your-domain.com/oauth/callback` or `http://localhost:5001/oauth/callback` for local testing
- **Scopes**: Check Canva's documentation for required scopes (usually something like `design:read`, `design:write`, `upload:write`)

## If These Don't Work

If Canva's provider setup shows different fields or the URLs don't work:
1. Check Canva's OAuth documentation: https://developers.canva.com/docs
2. Look for "OAuth Configuration" or "Authentication" section
3. The URLs might be shown in your app's OAuth settings


