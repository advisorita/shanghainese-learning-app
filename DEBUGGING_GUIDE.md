# 🔧 Debugging Guide for Web App

## ✅ Fixes Applied

1. **Audio Path Fixed** - Changed from `/audio/...` to `/static/audio/...`
2. **Console Logging Added** - All functions now log to browser console
3. **Better Error Messages** - Shows specific errors when things fail

## 🔍 How to Debug in Browser

### Open Browser Developer Console:

**Chrome/Edge:**
- Press `F12` or `Ctrl+Shift+I` (Windows/Linux)
- Press `Cmd+Option+I` (Mac)

**Safari:**
- Enable Developer menu: Safari → Preferences → Advanced → "Show Develop menu"
- Press `Cmd+Option+I`

**Firefox:**
- Press `F12` or `Ctrl+Shift+I`

### Look for Errors:

1. Open the **Console** tab in Developer Tools
2. Refresh the page
3. Try clicking the Translate button
4. Watch for messages like:
   - `Translate function called`
   - `Input text: ...`
   - `Response data: ...`

## 🐛 Common Issues & Solutions

### Issue 1: Translate Button Not Working

**Symptoms:** Nothing happens when you click Translate

**Debug:**
1. Open console (F12)
2. Click Translate button
3. Look for errors in red

**Possible Causes:**
- JavaScript error (check console)
- Empty input field
- Network error

**Solution:**
- Check console for error messages
- Make sure you entered text
- Check that server is running

### Issue 2: Audio Not Playing

**Symptoms:** Click "Hear Pronunciation" but no sound

**Debug:**
1. Check console for audio errors
2. Look for messages like "Playing audio from: ..."
3. Check if audio file path is correct

**Possible Causes:**
- Audio file path wrong (should start with `/static/`)
- TTS API slow/timeout
- Browser blocked audio

**Solution:**
- Check console logs
- Wait a few seconds (TTS takes time)
- Click speaker icon in browser bar to allow audio

### Issue 3: 404 Errors for Audio

**Symptoms:** Console shows "404 Not Found" for .wav files

**This should be FIXED now!**

If still happening:
- Check that audio files are in `/Users/ritaluo/Documents/Code Base/static/audio/`
- Make sure Flask is serving `/static/` correctly

## 📋 Checklist

Before reporting an issue:

- [ ] Server is running (check terminal)
- [ ] Using correct URL: http://127.0.0.1:8080
- [ ] Browser console is open (F12)
- [ ] Checked console for errors
- [ ] Tried refreshing the page
- [ ] Tried a different browser

## 🧪 Manual Tests

### Test 1: Translation
1. Go to http://127.0.0.1:8080
2. Type: "你好吗？"
3. Click "Translate"
4. Should see: "侬好伐？"

**Console should show:**
```
Translate function called
Input text: 你好吗？
Source language: mandarin
Sending request to /translate
Response status: 200
Response data: {success: true, translation: "侬好伐？"}
```

### Test 2: Audio
1. After translating
2. Click "Hear Pronunciation"
3. Should hear Shanghainese audio

**Console should show:**
```
Speak function called
Speaking: 侬好伐？
Sending request to /speak
Speak response status: 200
Audio URL: /static/audio/shanghainese_TIMESTAMP.wav
```

### Test 3: Vocabulary
1. Click "Vocabulary" in menu
2. Click any category card
3. Click "Listen" on a word
4. Should hear audio

## 🚀 Quick Reset

If nothing works, try full reset:

```bash
# Stop server
pkill -f "python.*web_app.py"

# Clear audio cache
rm -rf "/Users/ritaluo/Documents/Code Base/static/audio/"*

# Restart server
cd "/Users/ritaluo/Documents/Code Base"
./start_web_app.sh
```

## 📊 Check Server Status

```bash
# Is server running?
lsof -i :8080

# View server logs
cd "/Users/ritaluo/Documents/Code Base"
tail -f web_app.log
```

## 🔬 Advanced Debugging

### Test API Directly

**Test Translation:**
```bash
curl -X POST http://127.0.0.1:8080/translate \
  -H "Content-Type: application/json" \
  -d '{"text":"你好", "source":"mandarin"}'
```

**Should return:**
```json
{"success": true, "translation": "侬好"}
```

**Test Audio Generation:**
```bash
curl -X POST http://127.0.0.1:8080/speak \
  -H "Content-Type: application/json" \
  -d '{"text":"侬好"}'
```

**Should return:**
```json
{"audio_url": "/static/audio/shanghainese_TIMESTAMP.wav", "success": true}
```

## 💡 Tips

1. **Hard Refresh**: `Ctrl+F5` or `Cmd+Shift+R` to clear cache
2. **Check Network Tab**: See actual API requests
3. **Try Incognito**: Rules out extension issues
4. **Different Browser**: Chrome, Firefox, Safari

## ❓ Still Not Working?

Please provide:
1. Screenshot of browser console
2. Server log output (`tail -20 web_app.log`)
3. What browser you're using
4. Exact error messages

---

**Most common fix:** Hard refresh the page with `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)!
