# Fix Python Version Issue

## Problem

Railway is trying to install a specific Python version (3.11.0) that doesn't have a precompiled binary for the build environment.

## ✅ Fix Applied

I've removed `runtime.txt` and updated `nixpacks.toml` to use a more flexible Python version.

## Redeploy

```bash
railway up
```

## What Changed

**Removed:**
- `runtime.txt` (was too specific: python-3.11.0)

**Updated:**
- `nixpacks.toml` - Now uses `python3` instead of `python311`

Railway/Nixpacks will automatically use a compatible Python 3.11+ version.

## Alternative: Remove nixpacks.toml

If it still fails, Railway can auto-detect everything:

```bash
# Delete nixpacks.toml and let Railway auto-detect
rm nixpacks.toml
railway up
```

Railway's auto-detection is usually very good for Python apps.

## If Still Failing: Use Render

**Render handles Python versions automatically and is more reliable:**

1. Go to: https://render.com
2. New Web Service
3. Environment: Python 3
4. Build: `pip install -r requirements.txt`
5. Start: `gunicorn --bind 0.0.0.0:$PORT webhook_listener:app`
6. Deploy

**Render is much easier for Python deployments!**

---

**Try redeploying - Railway should auto-detect Python now!**

