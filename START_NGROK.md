# Start ngrok for Zapier

## ✅ ngrok is now installed!

## Start ngrok

In your terminal, run:

```bash
ngrok http 5001
```

You'll see output like:
```
Session Status                online
Account                       Your Account
Version                       3.x.x
Region                        United States (us)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123-def456.ngrok-free.app -> http://localhost:5001
```

## Copy the URL

Copy the `https://` URL from the "Forwarding" line:
```
https://abc123-def456.ngrok-free.app
```

## Use in Zapier

Update your Zapier webhook URL to:
```
https://YOUR-NGROK-URL.ngrok-free.app/webhook/onboarding
```

**Example:**
```
https://abc123-def456.ngrok-free.app/webhook/onboarding
```

## Quick Helper

After starting ngrok, you can also:
- Check the web interface: http://localhost:4040
- Or run: `./get_ngrok_url.sh`

## Keep ngrok Running

**Important**: Keep the ngrok terminal window open while testing. If you close it, the URL will stop working.

---

**Ready!** Start ngrok with `ngrok http 5001` and copy the URL! 🚀

