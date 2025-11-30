# Railway Deployment Fix

## Issue: Deploy Failed

Railway deployments often fail because Flask's development server isn't suitable for production.

## ✅ Fix Applied

I've updated your files to use **Gunicorn** (production WSGI server):

1. **Added gunicorn to requirements.txt**
2. **Updated Procfile** to use gunicorn
3. **Created nixpacks.toml** for Railway build configuration

## Redeploy

**Now redeploy:**

```bash
cd ~/slauson-automation
railway up
```

## What Changed

### Before:
```
web: python webhook_listener.py
```

### After:
```
web: gunicorn --bind 0.0.0.0:$PORT webhook_listener:app
```

## If It Still Fails

**Check Railway build logs:**
1. Go to: https://railway.com/project/8463ad66-4bdc-481d-90f7-914016f6b722
2. Click on your service
3. View "Deployments" tab
4. Click on failed deployment
5. Check "Build Logs"

**Common errors:**
- **"Module not found"** → Check requirements.txt
- **"Port binding error"** → Gunicorn should fix this
- **"Python version"** → Check runtime.txt

## Alternative: Use Render Instead

If Railway continues to have issues, Render is often easier:

1. Go to: https://render.com
2. New Web Service
3. Connect GitHub or deploy from local
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`
6. Deploy

---

**Try redeploying with the updated files!** The gunicorn change should fix it.

