import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

AUDIO_FOLDER = "generated_audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)


def generate_audio(script: str) -> str:

    if not API_KEY:
        raise ValueError("ELEVENLABS_API_KEY not found in environment variables")

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": script,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"TTS generation failed: {response.text}")

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filename