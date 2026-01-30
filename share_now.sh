#!/bin/bash
echo ""
echo "============================================================"
echo "🌐 Sharing Your Shanghainese App!"
echo "============================================================"
echo ""
echo "Starting SSH tunnel to localhost.run..."
echo ""
echo "⚠️  IMPORTANT: When you see a 'fingerprint' message, type 'yes'"
echo ""
echo "Your public URL will appear below:"
echo "============================================================"
echo ""

ssh -o StrictHostKeyChecking=no -R 80:localhost:8080 localhost.run
