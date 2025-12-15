# Google OAuth Setup - Personal Account (hmikaeltewolde@gmail.com)

## Quick Setup Steps

### Step 1: Create OAuth Credentials in Google Cloud Console

1. **Go to**: https://console.cloud.google.com/
2. **Select project**: `romanproject-481203` (or create new one)
3. **Enable Google Drive API**:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Drive API"
   - Click "Enable"
4. **Create OAuth Credentials**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - If prompted, configure OAuth consent screen first:
     - User Type: External (or Internal if you have Workspace)
     - App name: "Slauson Automation"
     - User support email: hmikaeltewolde@gmail.com
     - Add your email as a test user
   - Application type: **Desktop app**
   - Name: "Slauson Automation Desktop"
   - Click "Create"
5. **Download credentials**:
   - Click the download icon next to your OAuth client
   - Save the JSON file as `credentials.json` in your project directory

### Step 2: Run OAuth Setup Script

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python setup_google_oauth.py
```

This will:
1. Open a browser window
2. Ask you to sign in with **hmikaeltewolde@gmail.com**
3. Ask for permission to access Google Drive
4. Save the authorization token to `token.json`

### Step 3: Verify Setup

After running the script, you should have:
- ✅ `credentials.json` - OAuth client credentials
- ✅ `token.json` - Your authorization token

The code will now use your personal Google account!

## What Happens Next

- ✅ Files upload to **your personal Google Drive** (hmikaeltewolde@gmail.com)
- ✅ DocSend will **auto-sync** from your personal Drive
- ✅ Everything works together!

## Troubleshooting

**"credentials.json not found"**
- Make sure you downloaded the OAuth client JSON file
- Save it as `credentials.json` in the project directory

**"OAuth consent screen not configured"**
- Follow the prompts in Google Cloud Console
- Add your email as a test user

**"Access blocked"**
- Make sure you're signing in with hmikaeltewolde@gmail.com
- Check that your email is added as a test user in OAuth consent screen

## Summary

1. Create OAuth credentials in Google Cloud Console
2. Download as `credentials.json`
3. Run `python setup_google_oauth.py`
4. Authorize with your Google account
5. Done! Files will upload to your personal Drive


