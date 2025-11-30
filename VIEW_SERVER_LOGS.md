# How to View Server Logs

## Where to See Server Logs

The webhook server logs appear in the **terminal where you started it**.

## If You Started It in Background

If the server is running in the background, you have a few options:

### Option 1: Find the Terminal Window

The server is running in a terminal window. Look for:
- A terminal window showing Flask output
- Output like: `* Running on http://0.0.0.0:5001`
- Any log messages when requests come in

### Option 2: Restart and Watch Logs

Stop the current server and restart it in a visible terminal:

1. **Stop the current server:**
   ```bash
   pkill -f webhook_listener.py
   ```

2. **Start it in a new terminal window:**
   ```bash
   cd slauson-automation
   source venv/bin/activate
   python webhook_listener.py
   ```

3. **Keep this terminal visible** - all logs will appear here

### Option 3: Check Recent Logs

If the server is writing to a log file, check:
```bash
# Check if there's a log file
ls -la slauson-automation/*.log 2>/dev/null || echo "No log files found"
```

## What You Should See

When a webhook request comes in, you'll see:

```
Received webhook request: POST /webhook/onboarding
Headers: {...}
Payload keys: ['company_data', 'headshot_url', ...]
Processing images...
Creating Notion database entry...
Creating Notion company folder...
Generating Canva slide...
Processing complete. Success: True
```

## If You See Nothing

**No logs = No requests received**

This means:
- Zapier didn't trigger (check Zap is ON)
- ngrok isn't running (Zapier can't reach your server)
- Request failed before reaching server

## Quick Test

**Test if server is receiving requests:**

1. **In a new terminal**, test the webhook directly:
   ```bash
   curl -X POST http://localhost:5001/webhook/onboarding \
     -H "Content-Type: application/json" \
     -d '{"company_data": {"name": "Test"}, "headshot_url": "https://example.com/h.jpg", "logo_url": "https://example.com/l.png"}'
   ```

2. **Check the server terminal** - you should see the request logged

If this works but Zapier doesn't, the issue is with ngrok or Zapier configuration.

## Recommended: Restart Server in Visible Terminal

**Best practice:** Always run the server in a terminal window you can see:

```bash
cd slauson-automation
source venv/bin/activate
python webhook_listener.py
```

Keep this terminal open and visible - you'll see all requests and logs in real-time!

