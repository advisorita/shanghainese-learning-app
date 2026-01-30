#!/bin/bash

echo ""
echo "============================================================"
echo "🌐 Sharing Your Shanghainese App with Serveo!"
echo "============================================================"
echo ""
echo "Your public URL will appear below in ~5 seconds..."
echo "============================================================"
echo ""

# Use serveo.net which doesn't require authentication
ssh -o StrictHostKeyChecking=no -R 80:localhost:8080 serveo.net
