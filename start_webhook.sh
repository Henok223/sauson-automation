#!/bin/bash

# Quick start script for webhook server
# Usage: ./start_webhook.sh

echo "Starting Slauson Automation Webhook Server..."
echo "=============================================="
echo ""
echo "The server will start on: http://localhost:5000"
echo ""
echo "For Zapier testing, you'll need ngrok:"
echo "1. Install ngrok: https://ngrok.com/download"
echo "2. In a new terminal, run: ngrok http 5000"
echo "3. Copy the ngrok URL to your Zapier webhook"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "Starting server..."
echo ""

cd "$(dirname "$0")"
python webhook_listener.py

