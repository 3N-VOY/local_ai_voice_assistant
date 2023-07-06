## Local AI Voice Assistant

The AI Voice Assistant is a Python-based project that enables voice-controlled interactions with an AI assistant. The assistant can transcribe audio files to text, generate text-based responses, and convert the generated text into speech.

## Features

- Speech-to-Text Transcription: The assistant utilizes the Google Speech Recognition API to transcribe audio files to text.
- Text Generation: It generates responses based on user prompts using a language model.
- Text-to-Speech Synthesis: The assistant uses pyttsx3 library for converting generated text responses into speech.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/3N-VOY/local_ai_voice_assistant.git
   pip install -r requirements.txt

## Usage
To use the AI voice assistant, follow these steps:

Make sure you have the required dependencies installed (see "Requirements" section).
Set the appropriate model path in the code. (I used the Vicuna-Normal-7b-GGML model quantized 8 from https://huggingface.co)
Change the name field in the context 
Run the main() function to start the AI assistant.
The assistant will continuously listen for voice commands and provide responses.

## Project Structure
The main code file for the AI voice assistant is main.py. It includes the following components:

Speech-to-text transcription: The transcribe_audio_to_text function transcribes audio files to text using the Google Speech Recognition API.
Text generation: The generate_response function generates text-based responses using a language model.
Text-to-speech synthesis: The speak_text function converts generated text responses into speech.
License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the AI Voice Assistant, feel free to open an issue or submit a pull request.

