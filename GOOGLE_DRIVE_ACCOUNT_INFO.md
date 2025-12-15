# Google Drive Account & DocSend Sync

## Which Google Drive Account?

The code uploads to the **Google Drive account associated with your service account**.

### Your Service Account:
- **Path**: `/Users/henoktewolde/Downloads/romanproject-481203-4c2826e07600.json`
- This service account has its **own Google Drive**
- Files uploaded via this service account go to **that account's Drive**

### Important Questions:

1. **Is this the same Google Drive account** that's connected to DocSend?
   - If YES → DocSend will auto-sync ✅
   - If NO → DocSend won't see the files ❌

2. **Which Google account is connected to DocSend?**
   - Your personal Google account?
   - A shared/team Google account?
   - The service account's Google account?

## How DocSend Sync Works

DocSend syncs files from the **Google Drive account it's connected to**.

**For auto-sync to work:**
- The service account's Google Drive must be the same account connected to DocSend
- OR DocSend must be connected to a shared folder that the service account can access

## Options

### Option 1: Use Your Personal/Team Google Account

If DocSend is connected to your personal Google account:
1. We need to switch from service account to OAuth
2. Upload to your personal Google Drive
3. DocSend will auto-sync from there

### Option 2: Connect Service Account Drive to DocSend

If you want to use the service account:
1. Connect DocSend to the service account's Google Drive
2. Files will auto-sync

### Option 3: Upload to Shared Folder

1. Create a shared folder in your personal Google Drive
2. Give service account access to that folder
3. Upload to that shared folder
4. DocSend syncs from your personal Drive (where the folder is)

## What We Need to Know

**Tell me:**
1. Which Google account is connected to DocSend? (your personal account, team account, etc.)
2. Is the service account's Drive the same as the one connected to DocSend?

Based on your answer, I can:
- Update the code to use the correct Google account
- Or set up folder sharing
- Or configure OAuth instead of service account

## Current Setup

- **Service Account**: `romanproject-481203-4c2826e07600.json`
- **Uploads to**: Service account's Google Drive
- **DocSend sync**: Only works if DocSend is connected to that same account

Let me know which Google account DocSend is connected to, and I'll update the configuration!


