# 🚀 Quick Start - Webhook Server

## ✅ Dependencies Installed!

All packages are now installed in a virtual environment. Here's how to start your server:

## Start the Server

### Option 1: Use the start script (Easiest)
```bash
cd slauson-automation
./start_server.sh
```

### Option 2: Manual start
```bash
cd slauson-automation
source venv/bin/activate
python webhook_listener.py
```

You should see:
```
Running on http://0.0.0.0:5000
```

## Connect to Zapier

1. **Start ngrok** (in a new terminal):
   ```bash
   ngrok http 5000
   ```

2. **Copy the ngrok URL** (e.g., `https://abc123.ngrok.io`)

3. **Update Zapier webhook URL**:
   - Change from: `https://httpbin.org/post`
   - Change to: `https://YOUR-NGROK-URL.ngrok.io/webhook/onboarding`

4. **Test it!** Create a new entry in your "Burton test" database

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
- Make sure you activated the virtual environment:
  ```bash
  source venv/bin/activate
  ```
- You should see `(venv)` in your terminal prompt

### Server won't start
- Check if port 5000 is already in use
- Try a different port: `PORT=5001 python webhook_listener.py`

### Can't connect from Zapier
- Make sure ngrok is running
- Verify the URL in Zapier matches ngrok URL exactly
- Check ngrok web interface shows requests

---

**You're ready to go!** Start the server and connect it to Zapier! 🎉

