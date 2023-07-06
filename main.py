import pyttsx3
import speech_recognition as sr
from pyllamacpp.model import Model

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set the voice
engine.setProperty('voice', voices[1].id)

# Set the speech rate
voicespeed = 160
engine.setProperty('rate', voicespeed)

# Set the model path

model = Model('Path/To/Model')

context = "You are a helpful AI assistant and your name is Name you give straight answers to whatever you were asked."


def transcribe_audio_to_text(filename):
    """
    Transcribes audio from a file to text using Google Speech Recognition API.

    Args:
        filename (str): Path to the audio file.

    Returns:
        str: Transcribed text from the audio file.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping Unknown Error")


def generate_response(prompt):
    """
    Generates a response using the  model based on the given prompt.

    Args:
        prompt (str): Prompt to generate a response for.

    Returns:
        str: Generated response.
    """
    prompt_with_context = f"{context} {prompt}"
    response = " "
    for token in model.generate(prompt_with_context):
        response += f"{token}"
    return response


def speak_text(text):
    """
    Speaks out the given text using the text-to-speech engine.

    Args:
        text (str): Text to be spoken out.
    """
    engine.say(text)
    engine.runAndWait()


def main():
    """
    Main function to run the AI assistant.
    """
    while True:
        print("Listening...")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                if text:
                    print(f"You said: {text}")
                    response = generate_response(text)
                    print(f"A.I. says: {response}")
                    speak_text(response)

            except Exception as e:
                print("An error occurred: {}".format(e))


if __name__ == "__main__":
    main()
