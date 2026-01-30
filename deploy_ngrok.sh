#!/bin/bash

echo ""
echo "============================================================"
echo "🚀 Quick Deploy with ngrok"
echo "============================================================"
echo ""

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok not found!"
    echo ""
    echo "Install ngrok:"
    echo "  Mac: brew install ngrok"
    echo "  Or download from: https://ngrok.com/download"
    echo ""
    exit 1
fi

echo "✅ ngrok found"
echo ""

# Check if Flask app is running
if ! lsof -i :8080 &> /dev/null; then
    echo "⚠️  Flask app not running on port 8080"
    echo ""
    echo "Starting Flask app..."
    cd "$(dirname "$0")"
    python web_app.py > web_app.log 2>&1 &
    APP_PID=$!
    echo "✅ Flask app started (PID: $APP_PID)"
    sleep 3
else
    echo "✅ Flask app already running on port 8080"
fi

echo ""
echo "🌐 Starting ngrok..."
echo ""
echo "============================================================"
echo "📱 SHARE THIS URL WITH ANYONE:"
echo "============================================================"
echo ""

# Start ngrok
ngrok http 8080
