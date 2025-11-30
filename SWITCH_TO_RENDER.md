# Switch to Render - Recommended Solution

## Why Switch?

Railway is having persistent connection/timeout issues. **Render is more reliable** for Python apps and easier to use.

## Render Deployment (5 Minutes)

### Step 1: Create Account
1. Go to: https://render.com
2. Sign up (free tier available)
3. Verify email

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Choose: **"Public Git repository"** or **"Deploy manually"**

**If using Git:**
- Connect your GitHub account
- Select repository (or create one)

**If manual:**
- We'll upload files directly

### Step 3: Configure Service

**Basic Settings:**
- **Name:** `slauson-automation`
- **Region:** Choose closest to you (US East, US West, etc.)
- **Branch:** `main` (or `master`)
- **Root Directory:** (leave empty)

**Build & Deploy:**
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`

**Advanced Settings (optional):**
- **Auto-Deploy:** Yes (deploys on git push)

### Step 4: Environment Variables

Click **"Environment"** tab and add:

- `REMOVEBG_API_KEY` = your_key (optional, for background removal)
- `FLASK_DEBUG` = `False` (for production)

**Note:** `PORT` is automatically set by Render - don't add it!

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Wait for build (~2-3 minutes)
3. Get your URL: `https://slauson-automation.onrender.com`
4. Your webhook URL: `https://slauson-automation.onrender.com/webhook/onboarding`

### Step 6: Update Zapier

1. Go to your Zap
2. Update webhook step
3. Change URL from ngrok to: `https://slauson-automation.onrender.com/webhook/onboarding`
4. Test!

---

## Manual Deploy (If No Git)

If you don't have a Git repo, you can deploy manually:

1. **Create service** in Render
2. **Connect via Render CLI** or
3. **Use Render's web interface** to upload files

---

## Why Render is Better

✅ **More reliable** - Better uptime than Railway  
✅ **Easier** - Web interface, no CLI needed  
✅ **Better Python support** - Handles Python apps perfectly  
✅ **Free tier** - Available  
✅ **Auto-deploy** - Deploys on git push  
✅ **Better logs** - Clearer error messages  

---

## After Deployment

1. **Test health check:**
   ```bash
   curl https://slauson-automation.onrender.com/health
   ```
   Should return: `{"status": "healthy"}`

2. **Update Zapier webhook URL**
3. **Test with real entry**
4. **Monitor in Render dashboard**

---

**Render is the way to go!** It's much more reliable than Railway for Python apps. 🚀

