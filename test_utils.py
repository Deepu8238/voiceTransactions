# tests/test_utils.py
import unittest
from app.utils import format_transaction_data

class TestUtils(unittest.TestCase):
    def test_format_transaction_data(self):
        data = {"amount": 100, "recipient": "recipient"}
        formatted_data = format_transaction_data(data)
        self.assertIsInstance(formatted_data, str)
        self.assertEqual(formatted_data, "amount: 100, recipient: recipient")  # Placeholder test case
