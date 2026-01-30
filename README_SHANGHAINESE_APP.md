# 🏮 Shanghainese Learning App

An interactive Python application for learning Shanghainese dialect from English and Mandarin.

## Features

✨ **6 Learning Modes:**

1. **📚 Browse Vocabulary** - Explore categorized vocabulary (greetings, pronouns, verbs, etc.)
2. **🎴 Flashcard Mode** - Interactive flashcard learning with pronunciation
3. **🎯 Quiz Mode** - Multiple-choice quizzes to test your knowledge
4. **🌐 Translator** - Translate Mandarin/English to Shanghainese
5. **📈 Progress Tracking** - Track words learned, quiz scores, and study sessions
6. **🔊 Authentic Pronunciation** - Hear words spoken in authentic Shanghainese

## Installation

### Prerequisites
- Python 3.9+
- OpenAI API key (for translations)
- Internet connection (for TTS)

### Install Dependencies

```bash
pip install openai gradio_client
```

## Usage

### Quick Start

```bash
python shanghainese_learning_app.py
```

### Individual Features

**Translation Only:**
```bash
python import\ openai.py
```

## File Structure

```
Code Base/
├── shanghainese_learning_app.py    # Main learning application
├── import openai.py                 # Simple translator script
├── shanghainese_vocab.json         # Vocabulary database
├── learning_progress.json          # Your progress (auto-created)
└── README_SHANGHAINESE_APP.md      # This file
```

## Vocabulary Database

The app includes **70+ words and phrases** organized into categories:

- **Greetings** - Basic greetings and polite expressions
- **Pronouns** - Personal pronouns (I, you, he/she, we, they)
- **Questions** - Question words (what, where, how, etc.)
- **Time** - Time-related words (today, morning, night, etc.)
- **Common Verbs** - Essential verbs (go, play, know, speak, eat)
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

## How It Works

### Translation Engine
- Uses **GPT-4o** with extensive Shanghainese vocabulary and grammar rules
- Trained on authentic examples and dialect-specific patterns
- Supports both Mandarin and English input

### Text-to-Speech (TTS)
- Uses **Hugging Face Shanghainese TTS** model
- Authentic dialect pronunciation (not Mandarin reading)
- Adjustable speaking speed
- Free to use

### Progress Tracking
All progress is saved locally in `learning_progress.json`:
- Words learned
- Quiz scores and history
- Total study sessions
- Last session date

## Learning Tips

1. **Start with Greetings** - Learn basic greetings first
2. **Use Flashcards Daily** - Review 10-15 words per day
3. **Listen Carefully** - Pay attention to tones and pronunciation
4. **Take Quizzes** - Test yourself regularly
5. **Practice Speaking** - Repeat words after the TTS

## Key Shanghainese Features

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

## Troubleshooting

### TTS Not Working
- Check internet connection
- Hugging Face API may be slow during peak hours
- Try again or skip pronunciation for now

### Translation Errors
- Verify OpenAI API key is valid
- Check API quota/credits
- Ensure internet connection

### Audio Files
- Audio files are saved as `.wav` format
- Files are overwritten each time
- Use macOS `open` command or any audio player

## Resources

### Datasets Used
- [WenetSpeech-Wu](https://arxiv.org/html/2601.11027) - 8,000 hours Wu dialect data
- [Shanghainese Dictionary](https://shanghaidictionary.com/) - 20,000+ words
- [Omniglot Shanghainese](https://www.omniglot.com/language/phrases/shanghainese.php)

### TTS Model
- [Hugging Face Shanghainese TTS](https://huggingface.co/spaces/CjangCjengh/Shanghainese-TTS)

## Future Enhancements

- [ ] Add more vocabulary categories (food, travel, business)
- [ ] Speech recognition (speak and check pronunciation)
- [ ] Spaced repetition algorithm
- [ ] Export progress to CSV
- [ ] Web interface with Flask/Streamlit
- [ ] Mobile app version
- [ ] Community vocabulary contributions

## Contributing

To add vocabulary:
1. Edit `shanghainese_vocab.json`
2. Follow the existing format
3. Verify translations with native speakers

## License

Educational use only. Please respect the sources and datasets used.

## Credits

- OpenAI GPT-4o for translations
- CjangCjengh for Shanghainese TTS model
- Online Shanghainese dictionaries and resources
- Wu dialect linguistics research

---

**Happy Learning! 侬好! 🏮**
