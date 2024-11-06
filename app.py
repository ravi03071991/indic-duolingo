import gradio as gr
import openai
from config import LANGUAGES, ROLES, SPEAKERS
from response_generation import end_to_end_response

# Initialize OpenAI client
client = openai.OpenAI()

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("""
# Indic Duolingo: An Interactive Multilingual Learning Platform
## Powered by Sarvam AI, AI4Bharat, and OpenAI
This interactive platform enables seamless communication across 10 different Indian languages, combining advanced translation, transliteration, and text-to-speech capabilities.
### Features
- Real-time translation to multiple Indian languages
- Accurate transliteration for better pronunciation understanding
- High-quality text-to-speech audio output
- Adjustable speech pace and multiple voice options
### Technologies
1. **Translation**: Sarvam AI's Maurya model
2. **Text-to-Speech**: Sarvam AI's Bulbul model
3. **Transliteration**: AI4Bharat's Indic-Transliteration
4. **Conversational AI**: OpenAI's GPT-4o
### How to Use
- Select your preferred Indian language
- Choose a speaker voice and adjust speech pace
- Start chatting to see translations and hear pronunciations
""")

    with gr.Row():
        with gr.Column(scale=1):
            role_selector = gr.Dropdown(
                choices=list(ROLES.keys()),
                value="General Conversation",
                label="Select Conversation Mode",
                interactive=True
            )
            
    with gr.Row():
        with gr.Column(scale=1):
            language_selector = gr.Dropdown(
                            choices=[lang["display_name"] for lang in LANGUAGES.values()],
                            value="Telugu / తెలుగు",
                            label="Language",
                            interactive=True
                        )
        with gr.Column(scale=1):
            speaker_selector = gr.Dropdown(
                choices=SPEAKERS,
                value="meera",
                label="Speaker Voice",
                interactive=True
            )
        with gr.Column(scale=1):
            pace_slider = gr.Slider(
                minimum=0.5,
                maximum=2.0,
                value=1.65,
                step=0.05,
                label="Speech Pace",
                interactive=True
            )
    
    with gr.Row():
        # English Column
        with gr.Column(scale=1):
            gr.Markdown("### English Chat")
            english_chatbot = gr.Chatbot(height=500)
        
        with gr.Column(scale=1):
            gr.Markdown(lambda l: f"### {get_language_key(l)} Translation", inputs=[language_selector])
            translated_chatbot = gr.Chatbot(height=500)
        
        with gr.Column(scale=1):
            gr.Markdown(lambda l: f"### {get_language_key(l)} Transliteration", inputs=[language_selector])
            transliterated_chatbot = gr.Chatbot(height=500)
        
        # Audio Column
        with gr.Column(scale=1):
            gr.Markdown("### Audio Output")
            with gr.Column(min_width=200):
                user_audio = gr.Audio(
                    label="User Message",
                    interactive=False,
                    elem_id="user_audio"
                )
                assistant_audio = gr.Audio(
                    label="Assistant Response",
                    interactive=False,
                    elem_id="assistant_audio"
                )
    
    # Custom CSS for audio components
    gr.HTML("""
        <style>
            #user_audio, #assistant_audio {
                margin: 10px 0;
                max-width: 100%;
            }
        </style>
    """)

    # Helper function to get language key from display name
    def get_language_key(display_name: str) -> str:
        for key, value in LANGUAGES.items():
            if value["display_name"] == display_name:
                return key
        return "Telugu"  # Default fallback
    
    with gr.Row():
        msg = gr.Textbox(
            label="Type your message here",
            placeholder="Enter your message...",
            scale=4  # Make textbox take more space
        )
        clear = gr.Button("Clear Chat", scale=1)  # Add clear button next to textbox

    def respond(message, role, language, speaker, pace, history, translated_history, transliterated_history):
        msg, hist, trans_hist, translit_hist, (new_user_audio, new_assistant_audio) = end_to_end_response(client, 
            message, role, language, speaker, pace, history, translated_history, transliterated_history)
        
        return [
            msg,
            hist,
            trans_hist,
            translit_hist,
            new_user_audio,
            new_assistant_audio
        ]
    
    msg.submit(respond, 
              inputs=[msg, role_selector, language_selector, speaker_selector, pace_slider, 
                     english_chatbot, translated_chatbot, transliterated_chatbot],
              outputs=[msg, english_chatbot, translated_chatbot, transliterated_chatbot, 
                      user_audio, assistant_audio])
    
    clear.click(lambda: ("", [], [], [], None, None), 
               outputs=[msg, english_chatbot, translated_chatbot, transliterated_chatbot, 
                       user_audio, assistant_audio])

if __name__ == "__main__":
    demo.launch(share=True)