# Indic Duolingo

An interactive multilingual learning platform powered by Sarvam AI, AI4Bharat, and OpenAI.

## Why Indic Duolingo?

Language learning in India is essential due to the country's linguistic diversity, where each state often speaks its own language. People here are generally enthusiastic about learning new languages, and conversational practice can be more engaging and effective than traditional teaching methods. 

Indic Duolingo is created to make language learning more accessible and interactive by using an advanced LLM for conversational practice in English, with automatic translation and transliteration into the target language. This approach allows users to learn reading, pronunciation, and speaking skills through real-time translation and high-quality voice guidance.

## Features
- Real-time translation to 10 Indian languages
- Accurate transliteration for better pronunciation
- High-quality text-to-speech audio output
- Adjustable speech pace and multiple voice options
- Try different scenarios:
  - General conversation
  - Kirana store shopping
  - Banking interactions
  - Railway ticket booking
  - Restaurant ordering

## API's Used
- Translation: Sarvam AI's Maurya model
- Text-to-Speech: Sarvam AI's Bulbul model
- Transliteration: AI4Bharat's Indic-Transliteration
- Conversational AI: OpenAI's GPT-4o

## HuggingFace Space

Try it out on the [HuggingFace Spaces](https://huggingface.co/spaces/ravithejads/indicduolingo)

## Project Structure

Here’s a brief description of each file in this repository:

1. `app.py`: The main application file that contains the code to run Indic Duolingo as a gradio application. This script brings together all components like translation, transliteration, and text-to-speech to create the user interface and handle interactions.

2. `app.ipynb`: A Jupyter notebook version of the application, designed to run a Gradio interface for interactive testing or demonstrations. This file can be useful for exploring the application’s functionality in a more interactive.

3. `response_generation.py`: Contains code related to generating responses in the conversation, using LLM, translation, transliteration and text to speech APIs to create interactive dialogues for language practice.

4. `translation.py`: Handles the translation functionality, using Sarvam AI’s Maurya model to translate sentences from English to the chosen Indian language.

5. `config.py`: Contains configuration settings for the application, such as default language, role player settings, and other constants used across multiple files.

6. `transliteration.py`: Manages the transliteration functionality using AI4Bharat’s Indic-Transliteration to help users learn accurate pronunciation.

7. `tts.py`: The text-to-speech module that uses Sarvam AI’s Bulbul model to convert translated text into spoken audio, helping users learn pronunciation with voice guidance.

## Setup

To run the application locally, follow these instructions:

1. Clone the repository:
```bash
git clone https://github.com/ravi03071991/indic-duolingo.git
cd indic-duolingo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key (Available at https://platform.openai.com/account/api-keys)
- `SARVAM_API_KEY`: Your Sarvam AI API key (Available at https://dashboard.sarvam.ai/)

4. Run the application:
```bash
python app.py
```

5. Alternatively, you can use app.ipynb to create a Gradio interface.

## How to Use the Gradio Interface Application?

Here’s a step-by-step guide on how to use it:

1. **Select Conversation Mode:**

Choose the conversation mode from the dropdown at the top. This offers options General Conversation, Kirana Store Owner, Bank Employee, Railway Ticket Clerk, Restaurant Waiter allowing for conversations in various situations.

2. **Choose the Language:**

In the "Language" dropdown, select the Indian language you want to learn (e.g., Telugu, Hindi, etc.). This will enable the app to translate English text into the selected language.

3. **Select Speaker Voice:**

Choose a voice option (e.g., "Meera") to customize the audio output for text-to-speech. Different voices can add variety to your language-learning experience.

4. **Adjust Speech Pace:**

Use the "Speech Pace" slider to adjust the speed of the audio playback. Slower speeds can help with learning pronunciation, while faster speeds may be helpful for advanced learners.

5. **English Chat:**

Type your message in English in the chat box at the bottom and press Enter to submit. This message will be displayed in the English Chat section.

6. **Translation:**

The app will translate your English message into the selected language (e.g., Telugu) and display it in the Translation box.

7. **Transliteration:**

To help with pronunciation, the translated message will also be displayed in the Transliteration section, showing how to pronounce the sentence using English characters.

8. **Audio Output:**

Both your message and the assistant’s response will be available as audio. You can play the User Message and Assistant Response audio clips to hear the pronunciation and improve your speaking skills.

9. **Clear Chat:**

Use the Clear Chat button to reset the interface and start a new conversation.

By following these steps, you can practice speaking and understanding the selected language, making language learning more interactive and effective.