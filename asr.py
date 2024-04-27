# Module for Automatic Speech Recognition
# app/asr.py
# app/asr.py
import speech_recognition as sr
import requests
from io import BytesIO

class ASR:
    def recognize_speech(self, audio_url):
        """
        Recognizes speech from audio file located at the specified URL.

        Args:
            audio_url: URL of the audio file to be transcribed.

        Returns:
            Transcribed text.
        """
        recognizer = sr.Recognizer()

        # Download audio file from URL
        response = requests.get(audio_url)
        audio_data = BytesIO(response.content)

        # Perform speech recognition
        try:
            with sr.AudioFile(audio_data) as source:
                audio = recognizer.record(source)
            transcribed_text = recognizer.recognize_google(audio)
            return transcribed_text
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
