from ai4bharat.transliteration import XlitEngine
from config import LANGUAGES

class Transliterator:
    """Class to handle transliteration using AI4Bharat's XlitEngine"""
    def __init__(self):
        # Initialize the transliteration engine once
        self.engine = XlitEngine(
            src_script_type="indic",  # Source is Roman (English) text
            beam_width=10,            # Beam width for better accuracy
        )
    
    def transliterate(self, text: str, target_language: str) -> str:
        """
        Transliterate text to target language
        
        Args:
            text: Text to transliterate (in target language script)
            target_language: Target language key from LANGUAGES dict
            
        Returns:
            Transliterated text in Roman script
        """
        try:
            lang_code = LANGUAGES[target_language]["trans_code"]
            result = self.engine.translit_sentence(
                text,
                lang_code=lang_code
            )
            return result
        except Exception as e:
            print(f"Transliteration error for language {target_language}: {str(e)}")
            return text  # Return original text if transliteration fails

# Create a single instance to be used throughout the application
transliterator = Transliterator()

def transliterate_text(text: str, target_language: str) -> str:
    """
    Wrapper function for transliteration
    
    Args:
        text: Text to transliterate (in target language script)
        target_language: Target language key from LANGUAGES dict
        
    Returns:
        Transliterated text in Roman script
    """
    return transliterator.transliterate(text, target_language)