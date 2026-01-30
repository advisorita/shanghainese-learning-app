# 🌐 Deployment Guide - Share Your Shanghainese App

## ⚠️ IMPORTANT: Before Deploying

### 1. Secure Your API Key

**CRITICAL:** Never expose your OpenAI API key publicly!

Create a `.env` file for environment variables:

```bash
cd "/Users/ritaluo/Documents/Code Base"
echo "OPENAI_API_KEY=your_key_here" > .env
echo ".env" >> .gitignore
```

Then update `web_app.py` to use environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

### 2. Create Requirements File

```bash
cd "/Users/ritaluo/Documents/Code Base"
pip freeze > requirements.txt
```

Or create manually:
```
flask==2.3.0
openai==2.15.0
gradio_client==1.3.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

---

## 🚀 Deployment Options

### Option 1: Quick Share (Temporary) - ngrok ⭐ EASIEST

**Best for:** Testing with friends, temporary sharing

**Steps:**

1. **Install ngrok:**
```bash
brew install ngrok
# Or download from https://ngrok.com/download
```

2. **Start your Flask app:**
```bash
cd "/Users/ritaluo/Documents/Code Base"
python web_app.py
```

3. **In a new terminal, run ngrok:**
```bash
ngrok http 8080
```

4. **Share the URL:**
ngrok will give you a public URL like:
```
https://abc123.ngrok.io
```

**Pros:**
- ✅ Works in 2 minutes
- ✅ No code changes needed
- ✅ Free tier available

**Cons:**
- ❌ Temporary (stops when you close terminal)
- ❌ URL changes each time
- ❌ Requires your computer running

---

### Option 2: Railway.app ⭐ RECOMMENDED

**Best for:** Permanent deployment, easy setup

**Steps:**

1. **Install Railway CLI:**
```bash
npm install -g @railway/cli
# Or use: brew install railway
```

2. **Prepare your app:**

Create `Procfile`:
```
web: gunicorn web_app:app
```

Create `runtime.txt`:
```
python-3.9
```

Update `web_app.py` to use environment port:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
```

3. **Deploy:**
```bash
cd "/Users/ritaluo/Documents/Code Base"
railway login
railway init
railway up
```

4. **Set environment variables:**
```bash
railway variables set OPENAI_API_KEY=your_key_here
```

5. **Get your URL:**
```bash
railway domain
```

**Pros:**
- ✅ Free tier ($5/month credit)
- ✅ Easy deployment
- ✅ Auto-scaling
- ✅ Permanent URL

**Cons:**
- ❌ Requires Railway account
- ❌ May have usage limits

**Cost:** Free (with limits), then $5/month

---

### Option 3: Render.com

**Best for:** Free permanent hosting

**Steps:**

1. **Push code to GitHub:**
```bash
cd "/Users/ritaluo/Documents/Code Base"
git init
git add .
git commit -m "Initial commit"
gh repo create shanghainese-app --public --source=. --push
```

2. **Go to:** https://render.com

3. **Create New Web Service:**
   - Connect GitHub repo
   - Select "shanghainese-app"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn web_app:app`

4. **Set Environment Variables:**
   - Add: `OPENAI_API_KEY` = your key

5. **Deploy!**

**Pros:**
- ✅ Free tier available
- ✅ Permanent hosting
- ✅ Auto-deploys from GitHub
- ✅ SSL certificate included

**Cons:**
- ❌ Free tier spins down after inactivity
- ❌ Slower cold starts

**Cost:** Free (with limits)

---

### Option 4: PythonAnywhere

**Best for:** Python-focused, simple setup

**Steps:**

1. **Sign up:** https://www.pythonanywhere.com

2. **Upload files:**
   - Use "Files" tab
   - Upload your project

3. **Create web app:**
   - Go to "Web" tab
   - Create new Flask app
   - Point to `web_app.py`

4. **Install dependencies:**
```bash
pip install --user flask openai gradio_client
```

5. **Set environment variables** in WSGI config

**Pros:**
- ✅ Free tier available
- ✅ Simple for Python apps
- ✅ Good for beginners

**Cons:**
- ❌ Limited resources on free tier
- ❌ Manual setup required

**Cost:** Free (limited), $5/month (starter)

---

### Option 5: Vercel (with modifications)

**Best for:** Modern deployment, serverless

**Note:** Requires converting to serverless functions (more complex)

---

### Option 6: Your Own Server (VPS)

**Best for:** Full control, advanced users

**Providers:**
- DigitalOcean ($6/month)
- Linode ($5/month)
- AWS Lightsail ($3.50/month)

**Steps:**
1. Rent a VPS
2. SSH into server
3. Install dependencies
4. Run with gunicorn + nginx
5. Setup SSL with Let's Encrypt

---

## 📋 Pre-Deployment Checklist

- [ ] API key stored in environment variables
- [ ] `.env` file in `.gitignore`
- [ ] `requirements.txt` created
- [ ] Tested locally
- [ ] Changed `debug=True` to `debug=False`
- [ ] Updated to use `0.0.0.0` host
- [ ] Created `Procfile` (for some platforms)

---

## 🔒 Security Best Practices

### 1. Environment Variables
```python
# web_app.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set!")
```

### 2. Rate Limiting
Add rate limiting to prevent abuse:

```bash
pip install flask-limiter
```

```python
from flask_limiter import Limiter

limiter = Limiter(
    app=app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)

@app.route('/translate', methods=['POST'])
@limiter.limit("10 per minute")
def translate():
    # ...
```

### 3. CORS (if needed)
```bash
pip install flask-cors
```

```python
from flask_cors import CORS
CORS(app)
```

---

## 💰 Cost Comparison

| Platform | Free Tier | Paid Tier | Best For |
|----------|-----------|-----------|----------|
| ngrok | Yes (limited) | $8/month | Testing |
| Railway | $5 credit/month | $5+/month | Production |
| Render | Yes | $7/month | Free hosting |
| PythonAnywhere | Yes (limited) | $5/month | Beginners |
| Vercel | Yes | $20/month | Serverless |
| DigitalOcean | No | $6/month | Full control |

---

## 🎯 Recommended Path

### For Quick Testing:
**Use ngrok** - Share immediately with friends

### For Permanent Free Hosting:
**Use Render.com** - Best free tier, automatic deploys

### For Production:
**Use Railway** - Reliable, scalable, good pricing

---

## 📝 Step-by-Step: Deploy to Railway (Recommended)

Let me create the files you need...

