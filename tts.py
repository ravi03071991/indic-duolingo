import requests
import base64
import tempfile
from config import SARVAM_BASE_URL, LANGUAGES
import os

def text_to_speech(text: str, target_language: str, speaker: str, pace: float) -> str:
    """Convert text to speech using Sarvam AI"""
    url = f"{SARVAM_BASE_URL}/text-to-speech"
    payload = {
        "inputs": [text],
        "target_language_code": LANGUAGES[target_language]["code"],
        "speaker": speaker,
        "pitch": 0,
        "pace": pace,
        "loudness": 1.5,
        "speech_sample_rate": 8000,
        "enable_preprocessing": False,
        "model": "bulbul:v1"
    }
    headers = {
        "Content-Type": "application/json",
        "api-subscription-key": os.environ['SARVAM_API_KEY']
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if 'audios' in response_data and len(response_data['audios']) > 0:
            audio_base64 = response_data['audios'][0]
            audio_data = base64.b64decode(audio_base64)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
            temp_file.write(audio_data)
            temp_file.close()
            return temp_file.name
    raise Exception(f"Error in TTS API: {response.text}")