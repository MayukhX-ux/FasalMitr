from plyer import tts
import speech_recognition as sr

# Speech-to-text (STT)
def listen(language_code="en"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        # For local, limited: use PocketSphinx (English only)
        # For multilingual: use Google Web Speech API (internet needed)
        text = r.recognize_google(audio, language=language_code)
        return text
    except Exception as e:
        return f"Could not understand: {e}"

# Text-to-speech (TTS)
def speak(text, language_code="en"):
    # Plyer TTS works for many languages if OS supports, else fallback to English
    try:
        tts.speak(text)
    except Exception:
        # Optional: fallback to Google Text-to-Speech API for advanced TTS
        pass