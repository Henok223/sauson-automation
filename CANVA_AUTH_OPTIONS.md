# Canva Authentication Options

## The Situation

Canva **does NOT provide a simple API key** for server-to-server automation. Instead, they use **OAuth 2.0 Authorization Code flow with PKCE**, which requires user login.

## Your Options

### Option 1: One-Time OAuth Setup (Recommended if you want Canva API)

**How it works:**
1. You log in to Canva **once** (one-time setup)
2. We get an access token + refresh token
3. We store these tokens and reuse them
4. The refresh token automatically gets new access tokens when they expire

**Pros:**
- Uses your actual Canva template
- Full Canva API access
- Works with Data Autofill

**Cons:**
- Requires one-time user login
- Need to handle token refresh

**Implementation:**
I can create a one-time OAuth setup script that:
- Opens a browser for you to log in
- Gets and stores the tokens
- Automatically refreshes tokens when needed

### Option 2: Use Alternative Method (Already Working!)

**How it works:**
- Uses Gemini AI to generate slides from your template image
- No Canva API needed
- Already working in your code!

**Pros:**
- No authentication needed
- Already working
- Uses your template image

**Cons:**
- Doesn't use Canva's Data Autofill
- Generated slides (but match your template)

### Option 3: Canva Enterprise + Autofill API

**Requirements:**
- Canva Enterprise subscription
- App approval from Canva
- Full OAuth implementation

**If you have Canva Enterprise:**
- I can implement the full Autofill API
- Requires OAuth flow (one-time setup)

## Current Status

Your code is **already using Option 2** (alternative method) when Canva API fails. It's working!

## Recommendation

**If you want to use your Canva template with Data Autofill:**
- Choose **Option 1** (one-time OAuth setup)
- I'll create a setup script for you

**If the alternative method is working well:**
- Keep using it! No changes needed.

## Next Steps

Tell me which option you prefer:
1. **"Set up OAuth"** - I'll create a one-time login script
2. **"Keep using alternative"** - No changes needed, it's working
3. **"I have Canva Enterprise"** - I'll implement full Autofill API


