#!/bin/bash

# Script to get ngrok URL
# Make sure ngrok is running first: ngrok http 5000

echo "Checking for ngrok URL..."
echo ""

# Try to get URL from ngrok API
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels 2>/dev/null | python3 -c "import sys, json; data = json.load(sys.stdin); print(data['tunnels'][0]['public_url'] if data.get('tunnels') else '')" 2>/dev/null)

if [ -n "$NGROK_URL" ]; then
    echo "✅ Found ngrok URL:"
    echo ""
    echo "   $NGROK_URL"
    echo ""
    echo "📋 Use this in Zapier:"
    echo "   $NGROK_URL/webhook/onboarding"
    echo ""
else
    echo "❌ Ngrok doesn't appear to be running"
    echo ""
    echo "To start ngrok:"
    echo "   1. Make sure your webhook server is running (port 5000)"
    echo "   2. In a new terminal, run: ngrok http 5000"
    echo "   3. Then run this script again"
    echo ""
    echo "Or check ngrok web interface: http://localhost:4040"
fi

