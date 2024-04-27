# tests/test_asr.py
import unittest
from app.asr import ASR

class TestASR(unittest.TestCase):
    def setUp(self):
        self.asr = ASR()

    def test_recognize_speech(self):
        audio = "audio_data"  # Replace with actual audio data
        transcribed_text = self.asr.recognize_speech(audio)
        self.assertIsInstance(transcribed_text, str)
        self.assertNotEqual(transcribed_text, "")
