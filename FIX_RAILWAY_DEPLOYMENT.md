# Fix Railway Deployment

## Common Deployment Issues

### Issue 1: Build Failed

**Possible causes:**
- Missing dependencies
- Python version mismatch
- Build command issues

**Solution:**
1. Check Railway build logs (link provided)
2. Look for specific error messages
3. Common fixes below

### Issue 2: Missing Requirements

**Check:**
- `requirements.txt` exists and is correct
- All dependencies are listed

### Issue 3: Port Configuration

**Railway sets PORT automatically:**
- Your code already uses `os.getenv("PORT", 5001)`
- Railway will set PORT environment variable
- Should work automatically

### Issue 4: Python Version

**Check `runtime.txt`:**
- Should specify Python version
- Railway supports Python 3.11+

## Quick Fixes

### Fix 1: Update Requirements

Make sure `requirements.txt` has all dependencies:
```txt
requests>=2.31.0
python-dotenv>=1.0.0
Pillow>=10.0.0
notion-client>=2.2.1
openai>=1.3.0
removebg>=0.4
PyPDF2>=3.0.0
Flask>=3.0.0
```

### Fix 2: Check Procfile

Your `Procfile` should be:
```
web: python webhook_listener.py
```

### Fix 3: Add railway.json

I've created `railway.json` to help Railway detect the setup.

### Fix 4: Check Build Logs

**In Railway dashboard:**
1. Go to your project
2. Click on the service
3. Check "Deployments" tab
4. Click on failed deployment
5. View build logs

**Look for:**
- Python version errors
- Missing package errors
- Import errors
- Port binding errors

## Manual Deployment Steps

### Option 1: Redeploy

1. **Fix any issues** found in build logs
2. **Redeploy:**
   ```bash
   railway up
   ```

### Option 2: Deploy from GitHub

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your-repo-url
   git push -u origin main
   ```

2. **In Railway:**
   - Connect GitHub repository
   - Railway will auto-deploy

### Option 3: Check Environment Variables

**In Railway dashboard:**
- Go to Variables tab
- Add any needed variables:
  - `REMOVEBG_API_KEY` (optional)
  - `FLASK_DEBUG=False` (for production)

## Debugging Steps

1. **Check build logs** in Railway dashboard
2. **Share the error message** - I can help fix it
3. **Try local build:**
   ```bash
   pip install -r requirements.txt
   python webhook_listener.py
   ```
   If this works locally, it's a Railway config issue

## Common Error Messages

### "No module named 'flask'"
**Fix:** Make sure `requirements.txt` includes Flask

### "Port already in use"
**Fix:** Railway sets PORT automatically, your code should use it

### "Python version not found"
**Fix:** Check `runtime.txt` has valid Python version

### "Build command failed"
**Fix:** Check build logs for specific error

---

**What error do you see in the Railway build logs?** Share it and I'll help fix it!

