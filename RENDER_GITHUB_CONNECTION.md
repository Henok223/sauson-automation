# Render Can't See GitHub Repository - Troubleshooting

## Common Issues & Solutions

### Issue 1: GitHub Account Not Connected to Render

**Solution:**
1. Go to: https://dashboard.render.com/
2. Click your profile icon (top right)
3. Go to **"Account Settings"**
4. Click **"Connect GitHub"** or **"GitHub"** tab
5. Authorize Render to access your GitHub account
6. Make sure you grant access to the repository

---

### Issue 2: Repository is Private

If your repository is private, Render needs explicit access:

**Solution:**
1. Go to: https://github.com/settings/installations
2. Find **"Render"** in your installed GitHub Apps
3. Click **"Configure"**
4. Under **"Repository access"**, select:
   - **"Only select repositories"**
   - Choose **"sauson-automation"** (or your repo name)
5. Click **"Save"**

**OR** in Render:
1. Go to: https://dashboard.render.com/
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect GitHub"**
4. You may need to re-authorize and select the repository

---

### Issue 3: Repository Name Mismatch

Your repository is named: **`sauson-automation`** (note the spelling)

Make sure you're searching for the exact name in Render:
- ✅ `sauson-automation`
- ❌ `slauson-automation` (different spelling)

---

### Issue 4: GitHub App Permissions

Render needs read access to your repositories:

**Check Permissions:**
1. Go to: https://github.com/settings/installations
2. Click **"Render"**
3. Verify it has access to:
   - ✅ Repository contents (read)
   - ✅ Metadata (read)
   - ✅ Pull requests (if using auto-deploy)

---

### Issue 5: Organization Repository

If the repository is under an organization:

1. The organization owner needs to approve Render access
2. Go to organization settings → Third-party access
3. Approve Render's access request

---

## Step-by-Step: Connect Repository to Render

### Method 1: From Render Dashboard

1. **Go to Render:** https://dashboard.render.com/
2. **Click:** "New +" → "Web Service"
3. **Connect GitHub:**
   - If not connected, click "Connect GitHub"
   - Authorize Render
   - Grant repository access
4. **Select Repository:**
   - Search for: `sauson-automation`
   - Or: `Henok223/sauson-automation`
5. **Configure:**
   - Name: `slauson-automation`
   - Branch: `main`
   - Root Directory: `/` (leave empty)
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`

### Method 2: Manual Deploy (If GitHub Connection Fails)

1. **Clone repository locally** (if needed)
2. **In Render:**
   - Choose "Deploy manually"
   - Upload files or connect via Git URL

---

## Verify Repository Access

### Check in GitHub:
1. Go to: https://github.com/Henok223/sauson-automation/settings/access
2. Under "Third-party access", you should see "Render"
3. If not, Render needs to be authorized

### Check in Render:
1. Go to: https://dashboard.render.com/account
2. Under "GitHub", verify your account is connected
3. Check repository access permissions

---

## Quick Fix: Reconnect GitHub

If nothing works, try disconnecting and reconnecting:

1. **In Render:**
   - Go to Account Settings
   - Disconnect GitHub
   - Reconnect GitHub
   - Grant access to `sauson-automation`

2. **In GitHub:**
   - Go to Settings → Applications → Authorized OAuth Apps
   - Revoke Render access
   - Re-authorize from Render

---

## Repository Details

- **Full Name:** `Henok223/sauson-automation`
- **URL:** https://github.com/Henok223/sauson-automation
- **Visibility:** Check if private (may need explicit access)
- **Branch:** `main`

---

## Still Can't See It?

1. **Check repository visibility:**
   ```bash
   # Is it private? Render needs explicit access for private repos
   ```

2. **Try searching with full path:**
   - `Henok223/sauson-automation`
   - Not just `sauson-automation`

3. **Check Render logs:**
   - Look for error messages about repository access

4. **Contact Render Support:**
   - They can help with repository access issues

---

**Most common fix: Re-authorize GitHub in Render and grant access to the specific repository!**

