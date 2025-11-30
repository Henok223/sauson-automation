# Start the Webhook Server

## Correct Path

The project is in your **home directory**, not Downloads.

## Start the Server

Run these commands:

```bash
cd ~/slauson-automation
source venv/bin/activate
python webhook_listener.py
```

**Or use the full path:**

```bash
cd /Users/henoktewolde/slauson-automation
source venv/bin/activate
python webhook_listener.py
```

## What You Should See

```
 * Running on http://0.0.0.0:5001
 * Debug mode: on
 * Serving Flask app 'webhook_listener'
```

## Keep This Terminal Open

- All webhook requests will appear here
- You'll see logs when Zapier sends data
- Keep it visible to monitor activity

## Quick Start Script

You can also use:

```bash
cd ~/slauson-automation
./start_server.sh
```

---

**The server will run until you press Ctrl+C**

