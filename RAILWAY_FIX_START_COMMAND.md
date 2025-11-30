# Fix Railway Start Command

## Issue

Railway is using `python webhook_listener.py` instead of gunicorn.

## ✅ Fix Applied

I've updated:
1. **railway.json** - Set start command to use gunicorn
2. **nixpacks.toml** - Explicitly set gunicorn command

## Redeploy

```bash
railway up
```

## What Changed

**railway.json now has:**
```json
"startCommand": "gunicorn --bind 0.0.0.0:$PORT webhook_listener:app"
```

**nixpacks.toml now has:**
```toml
[start]
cmd = "gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 webhook_listener:app"
```

## If It Still Fails

**Check Railway dashboard:**
1. Go to your project
2. Click "Settings"
3. Check "Start Command" - should be gunicorn
4. If not, manually set it to: `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`

## Alternative: Use Render

If Railway continues having issues, **Render is much easier:**

1. Go to: https://render.com
2. New Web Service
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`
5. Deploy

**Render is more reliable for Python apps!**

---

**Try redeploying now - the start command should be fixed!**

