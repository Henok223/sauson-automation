#!/bin/bash

# Quick script to check if webhook is working

echo "Checking webhook status..."
echo "=========================="
echo ""

# Check if server is running
if curl -s http://localhost:5001/health > /dev/null 2>&1; then
    echo "✅ Webhook server is running"
else
    echo "❌ Webhook server is NOT running"
    echo "   Start it with: cd slauson-automation && source venv/bin/activate && python webhook_listener.py"
    exit 1
fi

# Check ngrok
if curl -s http://localhost:4040/api/tunnels > /dev/null 2>&1; then
    echo "✅ ngrok is running"
    URL=$(curl -s http://localhost:4040/api/tunnels 2>/dev/null | python3 -c "import sys, json; data = json.load(sys.stdin); tunnels = data.get('tunnels', []); print(tunnels[0]['public_url'] if tunnels else '')" 2>/dev/null)
    if [ -n "$URL" ]; then
        echo "   URL: $URL/webhook/onboarding"
    fi
else
    echo "❌ ngrok is NOT running"
    echo "   Start it with: ngrok http 5001"
fi

echo ""
echo "Recent requests (check ngrok web interface):"
echo "   http://localhost:4040"
echo ""
echo "Server logs:"
echo "   Check the terminal where webhook_listener.py is running"
echo ""

