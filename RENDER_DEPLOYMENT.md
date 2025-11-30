# Render Deployment Guide (Recommended)

## Why Render?

- ✅ More reliable than Railway for Python
- ✅ Web interface (no CLI needed)
- ✅ Free tier available
- ✅ Better error messages
- ✅ Automatic deployments

## Step-by-Step Deployment

### Step 1: Create Account

1. Go to: https://render.com
2. Sign up (free tier available)
3. Verify email

### Step 2: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Choose deployment method:
   - **Option A:** Connect GitHub (if you have repo)
   - **Option B:** Manual deploy (upload files)

### Step 3: Configure Service

**If using GitHub:**
- Select your repository
- Render will auto-detect Python

**If manual deploy:**
- **Name:** `slauson-automation`
- **Environment:** `Python 3`
- **Region:** Choose closest to you
- **Branch:** `main` (or `master`)

### Step 4: Build Settings

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn --bind 0.0.0.0:$PORT webhook_listener:app
```

### Step 5: Environment Variables

Click **"Environment"** tab and add:

- `REMOVEBG_API_KEY` = your_key (optional)
- `FLASK_DEBUG` = `False` (for production)

**Note:** `PORT` is automatically set by Render - don't add it manually.

### Step 6: Deploy

1. Click **"Create Web Service"**
2. Wait for build to complete (~2-3 minutes)
3. Get your URL: `https://slauson-automation.onrender.com`
4. Your webhook URL: `https://slauson-automation.onrender.com/webhook/onboarding`

### Step 7: Update Zapier

1. Go to your Zap
2. Update webhook URL from ngrok to Render URL
3. Test!

---

## Render vs Railway

| Feature | Render | Railway |
|---------|--------|---------|
| Ease of use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Free tier | ✅ Yes | ✅ Yes |
| Web interface | ✅ Yes | ⚠️ Mostly CLI |
| Python support | ✅ Excellent | ✅ Good |
| Reliability | ✅ High | ⚠️ Can have issues |

**Recommendation: Use Render!** It's easier and more reliable.

---

## After Deployment

1. **Test health check:**
   ```bash
   curl https://your-app.onrender.com/health
   ```
   Should return: `{"status": "healthy"}`

2. **Update Zapier webhook URL**
3. **Test with real entry**
4. **Monitor logs** in Render dashboard

---

**Render is the easiest option!** Try it if Railway keeps having issues.

