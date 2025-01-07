import unittest
from onyxai.blockchain_connector import BlockchainConnector

class TestBlockchainConnector(unittest.TestCase):
    def setUp(self):
        self.connector = BlockchainConnector("https://fake-blockchain.com")

    def test_send_data(self):
        data = {"key": "value"}
        result = self.connector.send_data(data)
        self.assertIn("transaction_id", result)

    def test_get_transaction_status(self):
        status = self.connector.get_transaction_status("txn_123456")
        self.assertEqual(status["status"], "confirmed")

if __name__ == "__main__":
    unittest.main()
