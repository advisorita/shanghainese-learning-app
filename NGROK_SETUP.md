# 🔐 ngrok Setup Guide

## Quick Setup (2 minutes)

### Step 1: Create Free Account

1. Go to: https://dashboard.ngrok.com/signup
2. Sign up with Google, GitHub, or email
3. **It's completely FREE!**

### Step 2: Get Your Auth Token

1. After signup, you'll see your dashboard
2. Go to: https://dashboard.ngrok.com/get-started/your-authtoken
3. Copy your authtoken (looks like: `2a_bC3dE4fG5hI6jK7lM8nO9pQ0rS1tU2vW3xY4zA5b`)

### Step 3: Add Auth Token to ngrok

Run this command (replace with YOUR token):

```bash
cd "/Users/ritaluo/Documents/Code Base"
./ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

**Example:**
```bash
./ngrok config add-authtoken 2a_bC3dE4fG5hI6jK7lM8nO9pQ0rS1tU2vW3xY4zA5b
```

### Step 4: Start ngrok

```bash
./ngrok http 8080
```

### Step 5: Get Your URL

You'll see output like:
```
Forwarding    https://abc-123-def.ngrok-free.app -> http://localhost:8080
```

**Share the `https://` URL with anyone!**

---

## Alternative: Use Different Tool (No Account Needed)

If you don't want to create an ngrok account, you can use **localhost.run** instead:

```bash
# Make sure your Flask app is running
python web_app.py

# In another terminal:
ssh -R 80:localhost:8080 localhost.run
```

You'll get a URL like: `https://abc123.localhost.run`

---

## Full Automated Script

After adding your authtoken, you can use:

```bash
cd "/Users/ritaluo/Documents/Code Base"
./deploy_ngrok.sh
```

This will:
1. Check if app is running
2. Start ngrok automatically
3. Show you the public URL

---

**Next:** After adding your authtoken, let me know and I'll help you start it!
