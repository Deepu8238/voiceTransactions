# tests/test_transaction_handler.py
import unittest
from app.transaction_handler import TransactionHandler

class TestTransactionHandler(unittest.TestCase):
    def setUp(self):
        self.transaction_handler = TransactionHandler()

    def test_process_transaction(self):
        transaction_data = {"amount": 100, "recipient": "recipient"}
        result = self.transaction_handler.process_transaction(transaction_data)
        self.assertEqual(result, "Transaction processed successfully")  # Placeholder test case
