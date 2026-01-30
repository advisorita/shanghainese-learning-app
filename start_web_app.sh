#!/bin/bash

echo ""
echo "============================================================"
echo "🏮 Shanghainese Learning Web App 🏮"
echo "============================================================"
echo ""
echo "📦 Checking dependencies..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install Python 3.9+"
    exit 1
fi

echo "✅ Python found"

# Check if in correct directory
if [ ! -f "web_app.py" ]; then
    echo "❌ web_app.py not found! Please run from Code Base directory"
    exit 1
fi

echo "✅ Web app files found"
echo ""
echo "🚀 Starting web server..."
echo "📍 Server will be available at: http://127.0.0.1:8080"
echo "🛑 Press Ctrl+C to stop the server"
echo ""
echo "============================================================"
echo ""

# Start the Flask app
python3 web_app.py
