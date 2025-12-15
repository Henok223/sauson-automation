# Fix OAuth Access Denied Error

## The Problem

You're getting "access_denied" because your email (hmikaeltewolde@gmail.com) isn't added as a test user in the OAuth consent screen.

## Solution: Add Yourself as a Test User

### Step 1: Go to OAuth Consent Screen

1. **Go to**: https://console.cloud.google.com/
2. **Select project**: `romanproject-481203`
3. **Navigate to**: "APIs & Services" → "OAuth consent screen"

### Step 2: Configure OAuth Consent Screen

If not already configured:

1. **User Type**: Choose "External" (unless you have Google Workspace)
2. **App information**:
   - App name: `Slauson Automation`
   - User support email: `hmikaeltewolde@gmail.com`
   - App logo: (optional)
3. **App domain**: (can skip for testing)
4. **Developer contact**: `hmikaeltewolde@gmail.com`
5. **Click "Save and Continue"**

### Step 3: Add Test Users (CRITICAL!)

1. **Scroll to "Test users" section**
2. **Click "+ ADD USERS"**
3. **Add your email**: `hmikaeltewolde@gmail.com`
4. **Click "Add"**
5. **Click "Save and Continue"**

### Step 4: Scopes (if prompted)

- Add scope: `https://www.googleapis.com/auth/drive.file`
- Click "Save and Continue"

### Step 5: Summary

- Review settings
- Click "Back to Dashboard"

## Step 6: Try OAuth Setup Again

After adding yourself as a test user:

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python setup_google_oauth.py
```

This time it should work!

## Alternative: Publish the App (Not Recommended for Testing)

If you want to skip test users, you can publish the app, but this requires:
- Privacy policy URL
- Terms of service URL
- App verification (can take days)

**Better to just add yourself as a test user!**

## Quick Checklist

- [ ] Go to OAuth consent screen
- [ ] Configure app (if not done)
- [ ] Add `hmikaeltewolde@gmail.com` as test user
- [ ] Save
- [ ] Run `python setup_google_oauth.py` again

## Still Having Issues?

If you still get errors:
1. Make sure you're using the correct Google account (hmikaeltewolde@gmail.com)
2. Check that the email is exactly the same (case-sensitive)
3. Wait a few minutes after adding test user (Google needs to sync)
4. Try in an incognito/private browser window


