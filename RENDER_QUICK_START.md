# Render Quick Start - 5 Minute Deployment

## 🚀 Fastest Path to Production

### 1. Sign Up (1 minute)
- Go to: https://render.com
- Sign up with email
- Verify email

### 2. Create Web Service (2 minutes)

1. Click **"New +"** → **"Web Service"**

2. **If you have GitHub:**
   - Connect GitHub
   - Select/create repo
   - Render auto-detects Python

3. **If no GitHub (manual):**
   - Choose "Deploy manually"
   - We'll set it up via web interface

### 3. Configure (1 minute)

**Settings:**
- **Name:** `slauson-automation`
- **Environment:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`

**Environment Variables (optional):**
- `REMOVEBG_API_KEY` = your_key

### 4. Deploy (1 minute)

- Click **"Create Web Service"**
- Wait ~2-3 minutes
- Get URL: `https://slauson-automation.onrender.com`

### 5. Update Zapier

- Change webhook URL to: `https://slauson-automation.onrender.com/webhook/onboarding`
- Test!

---

## 📋 Exact Settings for Render

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn --bind 0.0.0.0:$PORT webhook_listener:app
```

**Environment Variables:**
- `REMOVEBG_API_KEY` (optional)

**That's it!** Render handles everything else automatically.

---

**Total time: ~5 minutes** ⚡

**Much easier than Railway!** Try Render now! 🎯

