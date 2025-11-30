# ngrok Authentication Setup

ngrok requires a free account to use. Here's how to set it up:

## Step 1: Sign Up for ngrok (Free)

1. Go to: https://dashboard.ngrok.com/signup
2. Sign up with your email (free account is fine)
3. Verify your email

## Step 2: Get Your Authtoken

1. After signing up, go to: https://dashboard.ngrok.com/get-started/your-authtoken
2. Copy your authtoken (it looks like: `2abc123def456ghi789jkl012mno345pqr678stu901vwx234yz_5A6B7C8D9E0F1G2H3I4J5K`)

## Step 3: Configure ngrok

In your terminal, run:

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

Replace `YOUR_AUTHTOKEN_HERE` with the token you copied.

**Example:**
```bash
ngrok config add-authtoken 2abc123def456ghi789jkl012mno345pqr678stu901vwx234yz_5A6B7C8D9E0F1G2H3I4J5K
```

You should see:
```
Authtoken saved to configuration file: /Users/yourusername/.ngrok2/ngrok.yml
```

## Step 4: Start ngrok

Now you can start ngrok:

```bash
ngrok http 5001
```

You should see:
```
Session Status                online
Account                       Your Email
Forwarding                    https://abc123-def456.ngrok-free.app -> http://localhost:5001
```

## Quick Setup Commands

1. **Sign up**: https://dashboard.ngrok.com/signup
2. **Get token**: https://dashboard.ngrok.com/get-started/your-authtoken
3. **Configure**: `ngrok config add-authtoken YOUR_TOKEN`
4. **Start**: `ngrok http 5001`

## Alternative: One-Line Setup

If you want to do it all at once:

```bash
# 1. Sign up at https://dashboard.ngrok.com/signup
# 2. Get your token from https://dashboard.ngrok.com/get-started/your-authtoken
# 3. Run this (replace with your token):
ngrok config add-authtoken YOUR_TOKEN_HERE && ngrok http 5001
```

---

**Once configured, ngrok will remember your authtoken and you won't need to enter it again!**

