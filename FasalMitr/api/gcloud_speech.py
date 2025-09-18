import os
from google.cloud import speech_v1p1beta1 as speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud-service-account.json"

def google_speech_to_text(audio_data, language_code="en-IN"):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code
    )
    response = client.recognize(config=config, audio=audio)
    return " ".join([result.alternatives[0].transcript for result in response.results])