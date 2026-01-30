import openai
from gradio_client import Client
import pygame # To play the sound
import shutil
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. THE BRAIN: Translate to Shanghainese
def get_shanghainese_text(mandarin_input):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found in environment variables!")
        print("Please create a .env file with your API key (see .env.example)")
        exit(1)

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """You are an expert in Shanghainese (上海话/沪语). Translate Mandarin to authentic Shanghainese dialect.

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

Only return the Shanghainese translation, nothing else."""},
            {"role": "user", "content": mandarin_input}
        ]
    )
    return response.choices[0].message.content

# 2. THE VOICE: Convert Text to Speech (TTS) using Hugging Face Shanghainese TTS
def speak_dialect(text, output_file="shanghai_ai.wav", speaking_speed=1.0):
    """
    Convert Shanghainese text to speech using authentic Shanghainese TTS

    Args:
        text: Shanghainese text (not IPA)
        output_file: Output audio file path
        speaking_speed: Speed of speech (0.5 to 2.0, default 1.0)
    """
    print(f"Generating authentic Shanghainese speech for: {text}")
    client = Client('CjangCjengh/Shanghainese-TTS')

    # Call the API: text, ipa_input=False (we're using characters), speaking_speed
    result = client.predict(
        text,           # Shanghainese text
        False,          # ipa_input - we're using Shanghainese characters, not IPA
        speaking_speed, # speaking speed
        fn_index=1      # Use the endpoint that supports speaking_speed
    )

    # result is the path to the generated audio file
    # Copy it to our desired output location
    if isinstance(result, dict) and 'name' in result:
        audio_path = result['name']
    else:
        audio_path = result

    shutil.copy(audio_path, output_file)
    print(f"Authentic Shanghainese audio saved as {output_file}")

# 3. RUN IT
input_text = "你晚饭吃啥？"
sh_text = get_shanghainese_text(input_text)
print(f"AI says in Shanghainese: {sh_text}")

# Generate authentic Shanghainese speech
speak_dialect(sh_text, speaking_speed=1.0)