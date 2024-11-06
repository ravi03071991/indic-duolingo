from typing import List, Tuple, Any
from translation import translate_using_sarvam
from transliteration import transliterate_text
from tts import text_to_speech
from config import ROLES

def end_to_end_response(client: Any, message: str, role: str, language: str, speaker: str, pace: float,
                      history: List[Tuple[str, str]], 
                      translated_history: List[Tuple[str, str]], 
                      transliterated_history: List[Tuple[str, str]]) -> Tuple[str, List, List, List, Tuple[str, str]]:
    """Main function to handle chat, translation, transliteration, and audio generation"""
    try:
        # Initialize histories
        history = history or []
        translated_history = translated_history or []
        transliterated_history = transliterated_history or []
        
        # Get response from ChatGPT first for the conversation
        messages = []
        # messages.append({"role": "system", "content": "You are a helpful assistant."})
        messages.append({"role": "system", "content": ROLES[role]["system_prompt"]})
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
        messages.append({"role": "user", "content": message})
        
        # Get ChatGPT response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        english_response = response.choices[0].message.content
        
        # Translate both messages
        translated_user_message = translate_using_sarvam(message, language)
        translated_response = translate_using_sarvam(english_response, language)

        print("original message", message)
        print("translated user message", translated_user_message)
        print("translated response", translated_response)
        
        # Transliterate both translated messages separately
        transliterated_user = transliterate_text(translated_user_message, language)
        transliterated_response = transliterate_text(translated_response, language)

        print("transliterated user", transliterated_user)
        print("transliterated response", transliterated_response)
        
        # Generate audio for translated messages
        user_audio = text_to_speech(translated_user_message, language, speaker, pace)
        assistant_audio = text_to_speech(translated_response, language, speaker, pace)
        
        return ("", 
                history + [(message, english_response)],
                translated_history + [(translated_user_message, translated_response)],
                transliterated_history + [(transliterated_user, transliterated_response)],  # Keep user and response separate
                (user_audio, assistant_audio))
                
    except Exception as e:
        print(f"Error in chat and translate: {str(e)}")
        # gr.Warning(f"Error in chat and translate: {str(e)}")
        # return message, history, translated_history, transliterated_history, (None, None)