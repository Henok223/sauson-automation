# Production Deployment Guide

## Quick Deployment Options

### Option 1: Railway (Recommended - Easiest)

**Steps:**

1. **Install Railway CLI:**
   ```bash
   npm i -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Deploy:**
   ```bash
   cd ~/slauson-automation
   railway init
   railway up
   ```

4. **Set Environment Variables:**
   - Go to Railway dashboard
   - Add variables:
     - `REMOVEBG_API_KEY` (if using)
     - `PORT` (set to 5001 or let Railway assign)

5. **Get Your URL:**
   - Railway provides: `https://your-app.railway.app`
   - Webhook URL: `https://your-app.railway.app/webhook/onboarding`

6. **Update Zapier:**
   - Replace ngrok URL with Railway URL
   - Test!

**Cost:** Free tier available, then pay-as-you-go

---

### Option 2: Render

**Steps:**

1. **Go to:** https://render.com
2. **Create Account** (free tier available)
3. **New Web Service**
4. **Connect Repository** (or deploy from local)
5. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python webhook_listener.py`
   - **Environment:** Python 3
6. **Add Environment Variables:**
   - `REMOVEBG_API_KEY`
   - `PORT` (Render will set this)
7. **Deploy**
8. **Get URL:** `https://your-app.onrender.com/webhook/onboarding`

**Cost:** Free tier available

---

### Option 3: Heroku

**Steps:**

1. **Install Heroku CLI:**
   ```bash
   brew install heroku/brew/heroku
   ```

2. **Login:**
   ```bash
   heroku login
   ```

3. **Create App:**
   ```bash
   cd ~/slauson-automation
   heroku create slauson-automation
   ```

4. **Set Environment Variables:**
   ```bash
   heroku config:set REMOVEBG_API_KEY=your_key
   ```

5. **Deploy:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

6. **Get URL:** `https://slauson-automation.herokuapp.com/webhook/onboarding`

**Cost:** $7/month for basic dyno

---

## Required Files for Deployment

### 1. `Procfile` (for Heroku/Railway)

Create `Procfile`:
```
web: python webhook_listener.py
```

### 2. `runtime.txt` (optional - specify Python version)

```
python-3.11.0
```

### 3. Update `webhook_listener.py` for Production

Make sure it uses environment PORT:
```python
port = int(os.getenv("PORT", 5001))
```

(Already done!)

---

## Post-Deployment Checklist

- [ ] Webhook server is running
- [ ] Health check works: `https://your-url.com/health`
- [ ] Environment variables set
- [ ] Zapier webhook URL updated
- [ ] Test webhook receives requests
- [ ] Monitor logs for errors
- [ ] Set up uptime monitoring

---

## Environment Variables Needed

**Minimum:**
```env
PORT=5001  # Usually set by platform
```

**Optional:**
```env
REMOVEBG_API_KEY=your_key  # For background removal
OPENAI_API_KEY=your_key    # For Granola insights (future)
```

**Not Needed (Zapier handles):**
- ❌ NOTION_API_KEY
- ❌ CANVA_API_KEY
- ❌ DOCSEND_API_KEY

---

## Testing Production

1. **Health Check:**
   ```bash
   curl https://your-url.com/health
   ```
   Should return: `{"status": "healthy"}`

2. **Test Webhook:**
   - Create test entry in Notion
   - Check server logs
   - Verify processing completes

3. **Monitor:**
   - Check Railway/Render/Heroku logs
   - Verify no errors
   - Confirm requests are being processed

---

## Quick Start: Railway

**Fastest deployment:**

```bash
# 1. Install
npm i -g @railway/cli

# 2. Login
railway login

# 3. Deploy
cd ~/slauson-automation
railway init
railway up

# 4. Get URL (shown in terminal)
# 5. Update Zapier webhook URL
# 6. Done!
```

**Time: ~5 minutes** ⚡

---

**Choose your platform and deploy! Railway is the fastest option.** 🚀

