# Module for Natural Language Processing
# Add your NLP functionality here
# app/nlp.py
import spacy

class NLP:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text):
        """
        Processes text using natural language processing techniques.

        Args:
            text: Text input to be processed.

        Returns:
            Processed text.
        """
        doc = self.nlp(text)

        # Tokenization and part-of-speech tagging
        tokenized_text = " ".join([token.text for token in doc])
        pos_tags = [(token.text, token.pos_) for token in doc]

        processed_text = {
            "tokenized_text": tokenized_text,
            "pos_tags": pos_tags
        }

        return processed_text
