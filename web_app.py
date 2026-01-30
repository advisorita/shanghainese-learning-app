#!/usr/bin/env python3
"""
Shanghainese Learning Web App
Flask web interface for learning Shanghainese
"""

from flask import Flask, render_template, request, jsonify, send_file, session
import openai
from gradio_client import Client
import shutil
import json
import random
import os
from datetime import datetime
import secrets
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))

# Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print("❌ ERROR: OPENAI_API_KEY not found in environment variables!")
    print("Please create a .env file with your API key (see .env.example)")
    exit(1)

VOCAB_FILE = "shanghainese_vocab.json"
AUDIO_DIR = "static/audio"

# Ensure audio directory exists
os.makedirs(AUDIO_DIR, exist_ok=True)

# Load vocabulary
with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
    VOCABULARY = json.load(f)


def get_shanghainese_translation(text, source_lang="mandarin"):
    """Translate to Shanghainese using GPT-4o"""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    system_prompt = """You are an expert in Shanghainese (上海话/沪语). Translate to authentic Shanghainese dialect.

Key characteristics of Shanghainese:
PRONOUNS:
- Use 侬 (nong) for "you" instead of 你
- Use 伊 (yi) for "he/she" instead of 他/她
- Use 阿拉 (a la) for "we/us" instead of 我们
- Use 伊拉 (yi la) for "they/them" instead of 他们

QUESTION WORDS & LOCATION:
- Use 啥 (sa) for "what" instead of 什么
- Use 哪能 (na nen) for "how" instead of 怎么
- Use 阿里/阿里的 (a li/a li di) for "where" instead of 哪里
- Use 几钿 (jih dih) for "how much money"

NEGATION & VERBS:
- Use 勿/弗 (veq/fe) for negation instead of 不
- Use 七 (qi) for 去 (go)
- Use 巴相 (ba xiang) for "play" instead of 玩
- Use 晓得 (xiao de) for "know" instead of 知道
- Use 讲 (gang) for "speak" instead of 说

TIME:
- Use 今朝 (jin zhao) for "today"
- Use 夜里 (ya li) for "night"

Examples:
Mandarin: 你今天去哪里吃饭？
Shanghainese: 侬今朝七阿里的七饭

Mandarin: 你在干什么？
Shanghainese: 侬勒浪搭啥？

Only return the Shanghainese translation."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def generate_audio(text):
    """
    Generate Shanghainese audio
    Falls back to OpenAI TTS if Hugging Face is unavailable
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{AUDIO_DIR}/shanghainese_{timestamp}.wav"

    # Try Hugging Face Shanghainese TTS first
    try:
        print(f"🔊 Generating authentic Shanghainese speech...")
        client = Client('CjangCjengh/Shanghainese-TTS')
        result = client.predict(text, False, 1.0, fn_index=1)

        if isinstance(result, dict) and 'name' in result:
            audio_path = result['name']
        else:
            audio_path = result

        # Copy to static folder
        shutil.copy(audio_path, output_file)
        print(f"✅ Audio saved: {output_file}")
        return output_file

    except Exception as e:
        print(f"⚠️  Hugging Face unavailable (rate limit or error): {e}")
        print(f"🔄 Falling back to OpenAI TTS...")

        # Fallback to OpenAI TTS
        try:
            client = openai.OpenAI(api_key=OPENAI_API_KEY)

            # Use OpenAI's Chinese voice (alloy works well for Chinese)
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text,
                speed=1.0
            )

            response.stream_to_file(output_file)
            print(f"✅ Audio saved: {output_file} (OpenAI TTS)")
            return output_file

        except Exception as openai_error:
            print(f"❌ OpenAI TTS also failed: {openai_error}")
            return None


# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    """Translation endpoint"""
    data = request.json
    text = data.get('text', '')
    source = data.get('source', 'mandarin')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        translation = get_shanghainese_translation(text, source)
        return jsonify({
            'translation': translation,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/speak', methods=['POST'])
def speak():
    """Generate audio for Shanghainese text"""
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        audio_file = generate_audio(text)
        if audio_file:
            # Return correct path for Flask static files
            return jsonify({
                'audio_url': f'/{audio_file}',
                'success': True
            })
        else:
            return jsonify({'error': 'Failed to generate audio', 'success': False}), 500
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/vocabulary')
def vocabulary():
    """Vocabulary browser page"""
    return render_template('vocabulary.html', vocab=VOCABULARY)


@app.route('/vocabulary/<category>')
def vocabulary_category(category):
    """Get vocabulary for a specific category"""
    if category in VOCABULARY:
        return jsonify({
            'category': category,
            'words': VOCABULARY[category],
            'success': True
        })
    return jsonify({'error': 'Category not found', 'success': False}), 404


@app.route('/flashcards')
def flashcards():
    """Flashcards page"""
    return render_template('flashcards.html', categories=list(VOCABULARY.keys()))


@app.route('/flashcards/<category>')
def get_flashcards(category):
    """Get flashcards for a category"""
    if category in VOCABULARY:
        words = VOCABULARY[category].copy()
        random.shuffle(words)
        return jsonify({
            'category': category,
            'cards': words,
            'success': True
        })
    return jsonify({'error': 'Category not found', 'success': False}), 404


@app.route('/quiz')
def quiz():
    """Quiz page"""
    return render_template('quiz.html')


@app.route('/quiz/generate', methods=['POST'])
def generate_quiz():
    """Generate a quiz"""
    data = request.json
    num_questions = min(int(data.get('num_questions', 5)), 20)

    # Collect all words
    all_words = []
    for category in VOCABULARY.values():
        all_words.extend(category)

    if len(all_words) < 4:
        return jsonify({'error': 'Not enough words', 'success': False}), 400

    # Generate questions
    quiz_words = random.sample(all_words, min(num_questions, len(all_words)))
    questions = []

    for word in quiz_words:
        q_type = random.choice(['eng_to_sh', 'man_to_sh', 'sh_to_eng'])

        if q_type == 'eng_to_sh':
            question_text = f"What is '{word['english']}' in Shanghainese?"
            correct_answer = word['shanghainese']
            options = [word['shanghainese']]
            other_words = [w for w in all_words if w['shanghainese'] != word['shanghainese']]
            options.extend([w['shanghainese'] for w in random.sample(other_words, min(3, len(other_words)))])
        elif q_type == 'man_to_sh':
            question_text = f"What is '{word['mandarin']}' in Shanghainese?"
            correct_answer = word['shanghainese']
            options = [word['shanghainese']]
            other_words = [w for w in all_words if w['shanghainese'] != word['shanghainese']]
            options.extend([w['shanghainese'] for w in random.sample(other_words, min(3, len(other_words)))])
        else:  # sh_to_eng
            question_text = f"What does '{word['shanghainese']}' mean in English?"
            correct_answer = word['english']
            options = [word['english']]
            other_words = [w for w in all_words if w['english'] != word['english']]
            options.extend([w['english'] for w in random.sample(other_words, min(3, len(other_words)))])

        random.shuffle(options)

        questions.append({
            'question': question_text,
            'options': options,
            'correct_answer': correct_answer,
            'word': word
        })

    return jsonify({
        'questions': questions,
        'success': True
    })


if __name__ == '__main__':
    # Get port from environment variable (for deployment) or use default
    port = int(os.getenv('PORT', 8080))
    debug = os.getenv('FLASK_ENV') != 'production'

    print("\n" + "="*60)
    print("🏮 Shanghainese Learning Web App 🏮")
    print("="*60)
    print(f"\n🌐 Starting server at http://127.0.0.1:{port}")
    print("📱 Open your browser and visit the URL above")
    print("\nPress Ctrl+C to stop the server\n")

    # Use 0.0.0.0 for deployment, 127.0.0.1 for local
    host = '0.0.0.0' if not debug else '127.0.0.1'
    app.run(debug=debug, port=port, host=host)
