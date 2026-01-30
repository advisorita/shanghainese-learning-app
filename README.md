# 🏮 Shanghainese Learning App

An interactive application for learning Shanghainese dialect from English and Mandarin, featuring both CLI and web interfaces with authentic pronunciation support.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.0-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg)

## ✨ Features

### 🎯 Dual Interface
- **CLI Application** - Terminal-based interactive learning tool
- **Web Application** - Modern Flask web interface with beautiful UI

### 🔊 Authentic Pronunciation
- Authentic Shanghainese TTS (via Hugging Face)
- Automatic fallback to OpenAI TTS when needed
- Adjustable speaking speed

### 📚 Learning Modes

**CLI App:**
1. **Browse Vocabulary** - Explore categorized vocabulary (70+ words/phrases)
2. **Flashcard Mode** - Interactive flashcard learning
3. **Quiz Mode** - Multiple-choice quizzes
4. **Translator** - Real-time translation with audio
5. **Progress Tracking** - Track learning progress

**Web App:**
- Real-time translation interface
- Audio pronunciation player
- Vocabulary browser
- Interactive flashcards
- Quiz system

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key
- Internet connection

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/shanghainese-learning-app.git
cd shanghainese-learning-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### Run CLI App

```bash
python shanghainese_learning_app.py
```

### Run Web App

```bash
python web_app.py
```

Then open your browser to `http://localhost:8080`

## 📖 Vocabulary Database

The app includes **70+ words and phrases** organized into categories:

- **Greetings** - Basic greetings and polite expressions
- **Pronouns** - Personal pronouns (I, you, he/she, we, they)
- **Questions** - Question words (what, where, how, etc.)
- **Time** - Time-related words
- **Common Verbs** - Essential verbs
- **Common Phrases** - Useful everyday phrases
- **Numbers** - Numbers 1-10

### Adding More Vocabulary

Edit `shanghainese_vocab.json`:

```json
{
  "category_name": [
    {
      "english": "English word",
      "mandarin": "中文",
      "shanghainese": "上海话",
      "pinyin": "romanization"
    }
  ]
}
```

## 🎓 Key Shanghainese Features

### Pronouns
- 侬 (nong) = you
- 伊 (yi) = he/she
- 阿拉 (a la) = we/us
- 伊拉 (yi la) = they/them

### Common Patterns
- 勿/弗 for negation (not 不)
- 七 (qi) for "go" (sounds like 去)
- 啥 for "what" (not 什么)
- 阿里 for "where" (not 哪里)

### Unique Grammar
- Question particle: 伐 (va)
- Time prefix: 今朝 (today), 夜里 (night)
- Verbs: 巴相 (play), 晓得 (know), 讲 (speak)

## 🔧 Technical Details

### Translation Engine
- Uses **GPT-4o** with extensive Shanghainese vocabulary and grammar rules
- Trained on authentic examples and dialect-specific patterns
- Supports both Mandarin and English input

### Text-to-Speech (TTS)
- **Primary**: Hugging Face Shanghainese TTS model (authentic dialect pronunciation)
- **Fallback**: OpenAI TTS with Chinese voice (when HF is rate-limited)
- Automatic failover ensures continuous functionality

### Tech Stack
- **Backend**: Python, Flask
- **AI/ML**: OpenAI GPT-4o, Gradio Client
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **TTS**: Hugging Face Spaces, OpenAI Audio API

## 📁 Project Structure

```
shanghainese-learning-app/
├── shanghainese_learning_app.py    # CLI application
├── web_app.py                       # Flask web server
├── shanghainese_vocab.json         # Vocabulary database
├── requirements.txt                # Python dependencies
├── templates/                      # HTML templates
│   ├── index.html
│   ├── vocabulary.html
│   ├── flashcards.html
│   └── quiz.html
├── static/                         # Static assets
│   ├── css/
│   ├── js/
│   └── audio/
└── README.md                       # This file
```

## 🌐 Deployment

### Deploy with ngrok (Quick Share)

```bash
# Start the web app
python web_app.py

# In another terminal, start ngrok
./ngrok http 8080
```

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for production deployment options.

## 🐛 Troubleshooting

### TTS Not Working
- **Rate Limiting**: The app automatically falls back to OpenAI TTS
- **No Audio**: Check internet connection and API credentials

### Translation Errors
- Verify OpenAI API key is valid
- Check API quota/credits
- Ensure internet connection

### Audio Files
- Audio files are saved as `.wav` format in `static/audio/`
- Files are timestamped and won't overwrite each other

## 📚 Resources

### Datasets & References
- [WenetSpeech-Wu](https://arxiv.org/html/2601.11027) - 8,000 hours Wu dialect data
- [Shanghainese Dictionary](https://shanghaidictionary.com/) - 20,000+ words
- [Omniglot Shanghainese](https://www.omniglot.com/language/phrases/shanghainese.php)

### TTS Model
- [Hugging Face Shanghainese TTS](https://huggingface.co/spaces/CjangCjengh/Shanghainese-TTS)

## 🤝 Contributing

Contributions are welcome! To add vocabulary:
1. Edit `shanghainese_vocab.json`
2. Follow the existing format
3. Verify translations with native speakers
4. Submit a pull request

## 📄 License

Educational use only. Please respect the sources and datasets used.

## 🙏 Credits

- OpenAI GPT-4o for translations
- CjangCjengh for Shanghainese TTS model
- Online Shanghainese dictionaries and resources
- Wu dialect linguistics research

---

**Happy Learning! 侬好! 🏮**

Made with ❤️ for Shanghainese language preservation and learning
