# tests/test_nlp.py
import unittest
from app.nlp import NLP

class TestNLP(unittest.TestCase):
    def setUp(self):
        self.nlp = NLP()

    def test_process_text(self):
        text = "sample text"
        processed_text = self.nlp.process_text(text)
        self.assertIsInstance(processed_text, str)
        self.assertEqual(processed_text, "SAMPLE TEXT")  # Example test case
