# Testing HTML → PDF Webhook

## Step 1: Install Dependencies

First, make sure you have the required packages:

```bash
pip install weasyprint jinja2
```

Or if using a specific Python version:

```bash
pip3 install weasyprint jinja2
```

## Step 2: Start the Webhook Server

Open a terminal and run:

```bash
cd /Users/henoktewolde/slauson-automation
python webhook_listener.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5001
```

**Keep this terminal open** - the server needs to be running.

## Step 3: Test the Webhook

Open a **new terminal window** and run:

```bash
cd /Users/henoktewolde/slauson-automation
python test_webhook_direct.py
```

## Step 4: Check the Output

### In the test script output, you should see:

1. **"📄 Using HTML → PDF method..."** - This confirms HTML → PDF is being used
2. **"✓ Slide created with HTML → PDF"** - Success message
3. **Status Code: 200** - Request succeeded
4. **Response with Google Drive and DocSend links**

### In the server terminal, you should see:

```
📄 Using HTML → PDF method...
✓ Slide created with HTML → PDF
Uploading PDF to Google Drive...
✓ Uploaded to Google Drive: https://...
```

## What to Look For

✅ **Success indicators:**
- "📄 Using HTML → PDF method..." appears in server logs
- "✓ Slide created with HTML → PDF" message
- Status code 200
- Google Drive link in response

❌ **If HTML → PDF fails, you'll see:**
- "⚠️ HTML → PDF failed: [error]"
- "🎨 Using Canva template..." (fallback)
- Or "Falling back to Gemini method..." (last resort)

## Troubleshooting

### Error: "No module named 'weasyprint'"
```bash
pip install weasyprint jinja2
```

### Error: "No module named 'jinja2'"
```bash
pip install jinja2
```

### Error: "Connection refused"
- Make sure the webhook server is running in another terminal
- Check that it's running on port 5001 (default)

### HTML → PDF fails but Canva works
- Check server logs for the specific error
- Common issues:
  - Missing fonts (weasyprint will use system fonts)
  - Image loading issues (check image URLs/paths)
  - CSS rendering issues

## Testing with Custom Data

You can modify `test_webhook_direct.py` to test with different company data:

```python
test_payload = {
    "company_data__name": "Your Company Name",
    "company_data__description": "Your description...",
    # ... etc
}
```

## Viewing the Generated PDF

After a successful test:
1. Check the Google Drive link in the response
2. Or check the server terminal for the file path (if saved locally)
3. The PDF should match your template design with:
   - Orange sidebar
   - Yellow highlight boxes
   - Large orange company name
   - Circular logo
   - Map with location pin
   - Headshots in bottom right

