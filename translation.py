import requests
from config import SARVAM_BASE_URL, LANGUAGES
import os

def translate_using_sarvam(text: str, target_language: str) -> str:
    """Translate text using Sarvam AI's translation API"""

    url = f"{SARVAM_BASE_URL}/translate"
    
    payload = {
        "input": text,
        "source_language_code": "en-IN",
        "target_language_code": LANGUAGES[target_language]["code"],
        "speaker_gender": "Male",  # Can be made configurable if needed
        "mode": "formal",
        "model": "mayura:v1",
        "enable_preprocessing": False
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-subscription-key": os.environ['SARVAM_API_KEY']
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()["translated_text"]
    else:
        raise Exception(f"Translation error: {response.text}")