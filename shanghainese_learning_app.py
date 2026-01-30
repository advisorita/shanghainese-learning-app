#!/usr/bin/env python3
"""
Shanghainese Learning App
Interactive tool for learning Shanghainese for English and Mandarin speakers
"""

import openai
from gradio_client import Client
import shutil
import json
import random
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# CONFIGURATION
# ============================================================================

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print("❌ ERROR: OPENAI_API_KEY not found in environment variables!")
    print("Please create a .env file with your API key (see .env.example)")
    exit(1)

VOCAB_FILE = "shanghainese_vocab.json"
PROGRESS_FILE = "learning_progress.json"

# ============================================================================
# CORE TRANSLATION & TTS FUNCTIONS
# ============================================================================

def get_shanghainese_text(input_text, source_lang="mandarin"):
    """
    Translate English or Mandarin to Shanghainese using GPT-4o

    Args:
        input_text: Text to translate
        source_lang: "mandarin" or "english"
    """
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    if source_lang == "english":
        system_prompt = """You are an expert in Shanghainese (上海话/沪语). Translate English to authentic Shanghainese dialect.

Key characteristics of Shanghainese:
PRONOUNS:
- Use 侬 (nong) for "you" instead of 你
- Use 伊 (yi) for "he/she" instead of 他/她
- Use 阿拉 (a la) for "we/us" instead of 我们
- Use 伊拉 (yi la) for "they/them" instead of 他们
- Use 那 (na) for "you (plural)" instead of 你们

QUESTION WORDS & LOCATION:
- Use 啥 (sa) for "what" instead of 什么
- Use 哪能 (na nen) for "how" instead of 怎么
- Use 阿里/阿里的 (a li/a li di) for "where" instead of 哪里
- Use 几钿 (jih dih) for "how much money" instead of 多少钱

NEGATION & VERBS:
- Use 勿/弗 (veq/fe) for negation instead of 不
- Use 七 (qi) phonetically for 去 (go/to go)
- Use 巴相 (ba xiang) for "play/hang out" instead of 玩
- Use 晓得 (xiao de) for "know" instead of 知道
- Use 讲 (gang) for "speak/say" instead of 说

TIME:
- Use 今朝 (jin zhao) for "today" instead of 今天
- Use 早上 (zou lang xiang) for "morning" instead of 早晨
- Use 夜里 (ya li) for "night" instead of 晚上

GREETINGS:
- 侬好 (nong ho) for "hello"
- 侬早 (nong zo) for "good morning"
- 谢谢 (xia xia/ya ya) for "thank you"
- 对弗起 (dei fe qi) for "sorry"

Keep natural, colloquial tone with authentic Shanghainese expressions.

Only return the Shanghainese translation, nothing else."""
    else:  # mandarin
        system_prompt = """You are an expert in Shanghainese (上海话/沪语). Translate Mandarin to authentic Shanghainese dialect.

Key characteristics of Shanghainese:
PRONOUNS:
- Use 侬 (nong) for "you" instead of 你
- Use 伊 (yi) for "he/she" instead of 他/她
- Use 阿拉 (a la) for "we/us" instead of 我们
- Use 伊拉 (yi la) for "they/them" instead of 他们
- Use 那 (na) for "you (plural)" instead of 你们

QUESTION WORDS & LOCATION:
- Use 啥 (sa) for "what" instead of 什么
- Use 哪能 (na nen) for "how" instead of 怎么
- Use 阿里/阿里的 (a li/a li di) for "where" instead of 哪里
- Use 几钿 (jih dih) for "how much money" instead of 多少钱

NEGATION & VERBS:
- Use 勿/弗 (veq/fe) for negation instead of 不
- Use 七 (qi) phonetically for 去 (go/to go)
- Use 巴相 (ba xiang) for "play/hang out" instead of 玩
- Use 晓得 (xiao de) for "know" instead of 知道
- Use 讲 (gang) for "speak/say" instead of 说

TIME:
- Use 今朝 (jin zhao) for "today" instead of 今天
- Use 早上 (zou lang xiang) for "morning" instead of 早晨
- Use 夜里 (ya li) for "night" instead of 晚上

GREETINGS:
- 侬好 (nong ho) for "hello"
- 侬早 (nong zo) for "good morning"
- 谢谢 (xia xia/ya ya) for "thank you"
- 对弗起 (dei fe qi) for "sorry"

Keep natural, colloquial tone with authentic Shanghainese expressions.

Examples:
Mandarin: 你今天去哪里吃饭？
Shanghainese: 侬今朝七阿里的七饭

Mandarin: 你今天去哪儿玩？
Shanghainese: 侬今朝七阿里巴相？

Mandarin: 你在干什么？
Shanghainese: 侬勒浪搭啥？

Mandarin: 我不知道
Shanghainese: 我勿晓得

Mandarin: 他去哪里了？
Shanghainese: 伊去哪里了？

Mandarin: 你好吗？
Shanghainese: 侬好伐？

Mandarin: 你吃饭了吗？
Shanghainese: 饭吃过伐？

Mandarin: 这个多少钱？
Shanghainese: 几钿？

Mandarin: 谢谢你
Shanghainese: 谢谢侬

Mandarin: 对不起
Shanghainese: 对弗起

Mandarin: 我们一起去
Shanghainese: 阿拉一道去

Mandarin: 他们在说什么？
Shanghainese: 伊拉勒浪讲啥？

Only return the Shanghainese translation, nothing else."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content


def speak_shanghainese(text, output_file="output.wav", speaking_speed=1.0):
    """
    Convert Shanghainese text to speech using authentic Shanghainese TTS
    Falls back to OpenAI TTS if Hugging Face is unavailable

    Args:
        text: Shanghainese text
        output_file: Output audio file path
        speaking_speed: Speed of speech (0.5 to 2.0)
    """
    # Try Hugging Face Shanghainese TTS first
    try:
        print(f"🔊 Generating authentic Shanghainese speech...")
        client = Client('CjangCjengh/Shanghainese-TTS')

        result = client.predict(
            text,
            False,
            speaking_speed,
            fn_index=1
        )

        if isinstance(result, dict) and 'name' in result:
            audio_path = result['name']
        else:
            audio_path = result

        shutil.copy(audio_path, output_file)
        print(f"✅ Audio saved as {output_file}")
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
                speed=speaking_speed
            )

            response.stream_to_file(output_file)
            print(f"✅ Audio saved as {output_file} (OpenAI TTS)")
            return output_file
        except Exception as openai_error:
            print(f"❌ OpenAI TTS also failed: {openai_error}")
            return None


# ============================================================================
# VOCABULARY & PROGRESS MANAGEMENT
# ============================================================================

def load_vocabulary():
    """Load vocabulary from JSON file"""
    try:
        with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Vocabulary file {VOCAB_FILE} not found!")
        return {}


def load_progress():
    """Load learning progress"""
    try:
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "words_learned": [],
            "quiz_scores": [],
            "total_study_sessions": 0,
            "last_session": None
        }


def save_progress(progress):
    """Save learning progress"""
    progress["last_session"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


# ============================================================================
# LEARNING MODES
# ============================================================================

def browse_vocabulary(vocab):
    """Browse vocabulary by category"""
    print("\n" + "="*60)
    print("📚 VOCABULARY BROWSER")
    print("="*60)

    categories = list(vocab.keys())

    while True:
        print("\nCategories:")
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat.replace('_', ' ').title()} ({len(vocab[cat])} words)")
        print("  0. Back to main menu")

        try:
            choice = int(input("\nSelect category (0-{}): ".format(len(categories))))
            if choice == 0:
                break
            if 1 <= choice <= len(categories):
                show_category(vocab[categories[choice-1]], categories[choice-1])
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a number!")


def show_category(words, category_name):
    """Display words in a category"""
    print(f"\n{'='*60}")
    print(f"📖 {category_name.replace('_', ' ').title()}")
    print(f"{'='*60}\n")

    for i, word in enumerate(words, 1):
        print(f"{i}. {word['english']}")
        print(f"   Mandarin:     {word['mandarin']}")
        print(f"   Shanghainese: {word['shanghainese']} ({word['pinyin']})")

        # Option to hear pronunciation
        if i < len(words):
            print()

    input("\n📌 Press Enter to continue...")


def flashcard_mode(vocab, progress):
    """Interactive flashcard learning"""
    print("\n" + "="*60)
    print("🎴 FLASHCARD MODE")
    print("="*60)

    # Select category
    categories = list(vocab.keys())
    print("\nSelect category:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat.replace('_', ' ').title()}")

    try:
        choice = int(input(f"\nCategory (1-{len(categories)}): "))
        if not (1 <= choice <= len(categories)):
            print("❌ Invalid choice!")
            return

        category = categories[choice-1]
        words = vocab[category].copy()
        random.shuffle(words)

        print(f"\n📚 Starting flashcards for: {category.replace('_', ' ').title()}")
        print(f"📊 {len(words)} cards to review\n")

        correct = 0
        for i, word in enumerate(words, 1):
            print(f"\n--- Card {i}/{len(words)} ---")
            print(f"English: {word['english']}")
            print(f"Mandarin: {word['mandarin']}")

            input("\n🤔 Think of the Shanghainese word, then press Enter...")

            print(f"\n✅ Answer: {word['shanghainese']} ({word['pinyin']})")

            # Option to hear it
            hear = input("🔊 Hear pronunciation? (y/n): ").lower()
            if hear == 'y':
                speak_shanghainese(word['shanghainese'], f"flashcard_{i}.wav")

            knew_it = input("Did you know it? (y/n): ").lower()
            if knew_it == 'y':
                correct += 1
                if word['shanghainese'] not in progress['words_learned']:
                    progress['words_learned'].append(word['shanghainese'])

        print(f"\n{'='*60}")
        print(f"📊 Session Complete!")
        print(f"✅ Correct: {correct}/{len(words)} ({correct/len(words)*100:.1f}%)")
        print(f"{'='*60}")

        progress['total_study_sessions'] += 1
        save_progress(progress)

    except ValueError:
        print("❌ Invalid input!")


def quiz_mode(vocab, progress):
    """Interactive quiz with multiple choice"""
    print("\n" + "="*60)
    print("🎯 QUIZ MODE")
    print("="*60)

    # Gather all words
    all_words = []
    for category in vocab.values():
        all_words.extend(category)

    if len(all_words) < 4:
        print("❌ Need at least 4 words for quiz mode!")
        return

    # Select quiz size
    try:
        num_questions = int(input(f"\nHow many questions? (max {min(20, len(all_words))}): "))
        num_questions = min(num_questions, len(all_words))
    except ValueError:
        num_questions = 5

    quiz_words = random.sample(all_words, num_questions)
    score = 0

    print(f"\n📝 Starting quiz with {num_questions} questions!\n")

    for i, word in enumerate(quiz_words, 1):
        print(f"\n--- Question {i}/{num_questions} ---")

        # Randomly choose question type
        q_type = random.choice(['eng_to_sh', 'man_to_sh', 'sh_to_eng'])

        if q_type == 'eng_to_sh':
            print(f"What is '{word['english']}' in Shanghainese?")
            correct_answer = word['shanghainese']
        elif q_type == 'man_to_sh':
            print(f"What is '{word['mandarin']}' in Shanghainese?")
            correct_answer = word['shanghainese']
        else:  # sh_to_eng
            print(f"What does '{word['shanghainese']}' mean in English?")
            correct_answer = word['english']

        # Generate multiple choice options
        if q_type == 'sh_to_eng':
            options = [word['english']]
            other_words = [w for w in all_words if w['english'] != word['english']]
            options.extend([w['english'] for w in random.sample(other_words, min(3, len(other_words)))])
        else:
            options = [word['shanghainese']]
            other_words = [w for w in all_words if w['shanghainese'] != word['shanghainese']]
            options.extend([w['shanghainese'] for w in random.sample(other_words, min(3, len(other_words)))])

        random.shuffle(options)

        # Display options
        for j, option in enumerate(options, 1):
            print(f"  {j}. {option}")

        try:
            answer = int(input("\nYour answer (1-4): "))
            if options[answer-1] == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {correct_answer}")
        except (ValueError, IndexError):
            print(f"❌ Invalid input! Correct answer: {correct_answer}")

    # Show results
    percentage = (score / num_questions) * 100
    print(f"\n{'='*60}")
    print(f"🏆 QUIZ COMPLETE!")
    print(f"📊 Score: {score}/{num_questions} ({percentage:.1f}%)")
    print(f"{'='*60}")

    # Save score
    progress['quiz_scores'].append({
        'date': datetime.now().isoformat(),
        'score': score,
        'total': num_questions,
        'percentage': percentage
    })
    save_progress(progress)


def translator_mode():
    """Free translation mode"""
    print("\n" + "="*60)
    print("🌐 TRANSLATOR MODE")
    print("="*60)

    while True:
        print("\n1. Mandarin → Shanghainese")
        print("2. English → Shanghainese")
        print("0. Back to main menu")

        choice = input("\nSelect (0-2): ")

        if choice == '0':
            break
        elif choice in ['1', '2']:
            source = 'mandarin' if choice == '1' else 'english'
            text = input(f"\nEnter {source.title()} text: ")

            if not text.strip():
                continue

            print("\n🔄 Translating...")
            result = get_shanghainese_text(text, source)
            print(f"\n✅ Shanghainese: {result}")

            # Option to hear it
            hear = input("\n🔊 Hear pronunciation? (y/n): ").lower()
            if hear == 'y':
                speak_shanghainese(result, "translation_output.wav")
        else:
            print("❌ Invalid choice!")


def view_progress(progress):
    """Display learning progress"""
    print("\n" + "="*60)
    print("📈 YOUR PROGRESS")
    print("="*60)

    print(f"\n📚 Words learned: {len(progress['words_learned'])}")
    print(f"🎓 Study sessions: {progress['total_study_sessions']}")
    print(f"📅 Last session: {progress.get('last_session', 'Never')}")

    if progress['quiz_scores']:
        print(f"\n🎯 Quiz History (last 5):")
        for quiz in progress['quiz_scores'][-5:]:
            date = quiz['date'][:10]
            print(f"  {date}: {quiz['score']}/{quiz['total']} ({quiz['percentage']:.1f}%)")

    if progress['words_learned']:
        print(f"\n📝 Recently learned words:")
        for word in progress['words_learned'][-10:]:
            print(f"  • {word}")

    input("\n📌 Press Enter to continue...")


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main application loop"""
    vocab = load_vocabulary()
    progress = load_progress()

    if not vocab:
        print("❌ Unable to load vocabulary database!")
        return

    print("\n" + "="*60)
    print("🏮 SHANGHAINESE LEARNING APP 🏮")
    print("Learn Shanghainese from English & Mandarin")
    print("="*60)

    while True:
        print("\n📋 MAIN MENU:")
        print("  1. 📚 Browse Vocabulary")
        print("  2. 🎴 Flashcard Mode")
        print("  3. 🎯 Quiz Mode")
        print("  4. 🌐 Translator")
        print("  5. 📈 View Progress")
        print("  0. ❌ Exit")

        choice = input("\nSelect option (0-5): ")

        if choice == '0':
            print("\n👋 再会 (Goodbye)! Happy learning!")
            break
        elif choice == '1':
            browse_vocabulary(vocab)
        elif choice == '2':
            flashcard_mode(vocab, progress)
        elif choice == '3':
            quiz_mode(vocab, progress)
        elif choice == '4':
            translator_mode()
        elif choice == '5':
            view_progress(progress)
        else:
            print("❌ Invalid choice! Please select 0-5.")


if __name__ == "__main__":
    main()
