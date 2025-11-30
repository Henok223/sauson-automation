# Using Port 5001 Instead of 5000

Port 5000 is already in use on your Mac (likely by macOS AirPlay). The server is now configured to use **port 5001** by default.

## ✅ Server Configuration Updated

The webhook server now defaults to port 5001. Here's how to use it:

## Start the Server

### Option 1: Use the start script
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

The server will run on: `http://localhost:5001`

## Start ngrok

**Important**: Use port 5001 in ngrok:

```bash
ngrok http 5001
```

You'll see output like:
```
Forwarding   https://abc123-def456.ngrok-free.app -> http://localhost:5001
```

## Zapier Webhook URL

Use this format:
```
https://YOUR-NGROK-URL.ngrok-free.app/webhook/onboarding
```

**Example:**
```
https://abc123-def456.ngrok-free.app/webhook/onboarding
```

## Using a Different Port

If you want to use a different port:

```bash
PORT=8080 python webhook_listener.py
```

Then start ngrok with that port:
```bash
ngrok http 8080
```

## Quick Checklist

- [ ] Server running on port 5001
- [ ] ngrok running: `ngrok http 5001`
- [ ] Copy ngrok URL
- [ ] Update Zapier: `https://YOUR-URL.ngrok-free.app/webhook/onboarding`
- [ ] Test with a Notion entry

---

**The server is ready on port 5001!** Just make sure ngrok uses the same port.

