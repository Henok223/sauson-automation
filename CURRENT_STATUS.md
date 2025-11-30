# Current Status - Debugging

## What I See in Your Logs

✅ **Good News:**
- Webhook is receiving requests from Zapier
- Server is running and responding
- Requests are reaching your server

❌ **Issues:**
1. **Missing images**: Latest request doesn't have `headshot_url` or `logo_url`
2. **400/500 errors**: Requests are failing
3. **Server restarting**: File changes causing restarts (this is normal in debug mode)

## What's Happening

Looking at your logs:
- **First request** (12:16:31): Had `headshot_url` and `logo_url` → Got 500 error
- **Second request** (12:19:19): Missing `headshot_url` and `logo_url` → Got 400 error

## The Problem

The latest request from Zapier doesn't include the image URLs. This could mean:
1. **Images not attached** in Notion entry
2. **Zapier not sending** the file URLs
3. **Field mapping issue** in Zapier

## Next Steps

### 1. Check Your Notion Entry

Make sure your test entry has:
- ✅ **Headshot** file attached (not just a URL)
- ✅ **Logo** file attached (not just a URL)
- ✅ Files are actually uploaded to Notion

### 2. Check Zapier Field Mapping

In your Zap webhook step, verify:
- `headshot_url`: `{{1.Headshot}}`
- `logo_url`: `{{1.Logo}}`

### 3. Test Again

After I update the code with better logging:
1. **Create a new entry** in Notion
2. **Make sure Headshot and Logo files are attached**
3. **Set Status = "Ready"** (if using filter)
4. **Watch the server logs** - you'll see more detailed info

## Updated Code

I've added better logging so you'll see:
- What's in `company_data`
- Company name
- Detailed error messages
- Success/failure status

---

**Try creating a new entry with Headshot and Logo files attached, and watch the server logs!**

