# 🌐 Shanghainese Learning Web App

Beautiful, interactive web interface for learning Shanghainese!

## 🚀 Quick Start

### 1. Make sure dependencies are installed:
```bash
cd "/Users/ritaluo/Documents/Code Base"
pip install flask openai gradio_client
```

### 2. Start the web server:
```bash
python web_app.py
```

### 3. Open your browser:
Visit: **http://127.0.0.1:5000**

## 📱 Features

### 🌐 Translator (Home Page)
- **Mandarin → Shanghainese**
- **English → Shanghainese**
- Click examples to try instantly
- Hear authentic pronunciation
- Clean, modern interface

### 📚 Vocabulary Browser
- Browse by category (Greetings, Pronouns, etc.)
- See English, Mandarin, and Shanghainese
- Listen to pronunciation for each word
- Beautiful card-based interface

### 🎴 Flashcard Mode
- Select a category to study
- Interactive flip cards
- Audio pronunciation
- Track what you know
- Progress tracking

### 🎯 Quiz Mode
- Customizable quiz length (5-20 questions)
- Multiple choice format
- Instant feedback
- Score tracking
- Performance visualization

## 🎨 Interface Highlights

- **Responsive Design** - Works on desktop, tablet, and mobile
- **Modern UI** - Bootstrap 5 + custom styling
- **Chinese Font Support** - Proper display of Chinese characters
- **Smooth Animations** - Professional transitions and effects
- **Color-Coded Feedback** - Visual cues for correctand incorrect answers

## 📁 Project Structure

```
Code Base/
├── web_app.py                    # Flask application
├── templates/
│   ├── base.html                 # Base template with navigation
│   ├── index.html                # Translator page
│   ├── vocabulary.html           # Vocabulary browser
│   ├── flashcards.html           # Flashcard mode
│   └── quiz.html                 # Quiz mode
├── static/
│   ├── css/
│   │   └── style.css             # Custom styles
│   └── audio/                    # Generated audio files
├── shanghainese_vocab.json       # Vocabulary database
└── import openai.py              # CLI version (still works!)
```

## 🔧 Customization

### Add More Vocabulary
Edit `shanghainese_vocab.json`:
```json
{
  "new_category": [
    {
      "english": "word",
      "mandarin": "中文",
      "shanghainese": "上海话",
      "pinyin": "romanization"
    }
  ]
}
```

### Change Colors
Edit `static/css/style.css` and modify the `:root` variables:
```css
:root {
    --primary-red: #dc3545;    /* Main accent color */
    --secondary-gold: #ffc107; /* Secondary accent */
}
```

### Add More Features
The Flask app in `web_app.py` is modular - add new routes and templates easily!

## 💡 Usage Tips

### Translator
1. Select Mandarin or English as source
2. Type or click an example
3. Click "Translate"
4. Click "Hear Pronunciation" for audio
5. Press Ctrl+Enter in text box for quick translate

### Flashcards
1. Choose a category
2. See English + Mandarin
3. Think of answer
4. Click "Show Answer"
5. Listen to pronunciation
6. Mark if you knew it
7. See your score at the end

### Quiz
1. Choose number of questions (5-20)
2. Click "Start Quiz"
3. Select your answer
4. See instant feedback
5. View final score and performance

## 🎯 Keyboard Shortcuts

- **Translator**: `Ctrl+Enter` to translate
- **All Forms**: `Enter` to submit
- **Modal Dialogs**: `Esc` to close

## 🔊 Audio Features

- **Authentic Shanghainese TTS** - Not Mandarin reading!
- **Instant Playback** - Click to hear immediately
- **Cached Files** - Audio saved in `static/audio/`
- **Browser Compatibility** - Works in all modern browsers

## 📊 Progress Tracking

Currently the web app doesn't save progress between sessions. To add this:
1. Use cookies/localStorage for client-side tracking
2. Or add a database (SQLite) for server-side tracking

## 🛠️ Troubleshooting

### Server won't start
```bash
# Check if port 5000 is already in use
lsof -i :5000

# Kill the process if needed
kill -9 <PID>
```

### Audio not working
- Check internet connection (requires Hugging Face API)
- Wait a few seconds for first audio generation
- Check browser console for errors

### Translation errors
- Verify OpenAI API key is valid
- Check API credits/quota
- Look at terminal for error messages

## 🌟 Advantages Over CLI Version

✅ **Better UX** - Visual, intuitive interface
✅ **Audio Playback** - Built-in player
✅ **Multiple Modes** - Easy switching
✅ **Mobile Friendly** - Works on phone/tablet
✅ **No Terminal** - Just use browser
✅ **Shareable** - Can deploy online

## 🚀 Next Steps

### Deploy Online (Optional)
1. **Heroku**: Easy deployment, free tier available
2. **Railway**: Modern alternative to Heroku
3. **PythonAnywhere**: Good for Flask apps
4. **AWS/Google Cloud**: For production use

### Add Features
- User accounts and login
- Saved progress with database
- Spaced repetition algorithm
- Speech recognition (speak and check)
- Leaderboard for quizzes
- Share results on social media

## 📝 Notes

- Keep `import openai.py` for command-line use
- Web app and CLI app work independently
- Both use the same vocabulary JSON file
- Audio files auto-delete on server restart

---

**Enjoy learning Shanghainese! 🏮 侬好!**
