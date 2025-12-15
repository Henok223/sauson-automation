# Gemini API Quota Fix

## Issue: Quota Exceeded Error

You're getting a `429` error because:
- `gemini-2.0-flash-exp` requires a **paid tier** (free tier limit is 0)
- The code was trying to use this model first

## ✅ Fixed!

I've updated the code to:
1. **Try free tier models first**:
   - `gemini-1.5-flash` (free tier ✅)
   - `gemini-1.5-pro` (free tier ✅)
   - `gemini-pro` (free tier ✅)
   - `gemini-2.0-flash-exp` (paid tier only)

2. **Add retry logic** for quota errors:
   - Automatically retries with exponential backoff
   - Waits for the suggested retry time from API

3. **Better error messages** if quota is exceeded

## What Changed

### Before:
- Tried `gemini-2.0-flash-exp` first (paid tier only)
- Failed immediately with quota error

### After:
- Tries `gemini-1.5-flash` first (free tier)
- Falls back to other free tier models
- Retries on quota errors
- Only uses paid tier models if available

## Next Steps

1. **Restart your server** to load the changes
2. **Test again** - it should now use free tier models
3. **If you still get quota errors**:
   - Check your usage: https://ai.dev/usage?tab=rate-limit
   - Free tier has limits (15 requests/minute for gemini-1.5-flash)
   - Wait a minute and try again
   - Or upgrade to paid tier: https://ai.google.dev/pricing

## Free Tier Limits

- **gemini-1.5-flash**: 15 requests/minute
- **gemini-1.5-pro**: 2 requests/minute
- **gemini-pro**: 60 requests/minute

The code will automatically use the best available free tier model!


