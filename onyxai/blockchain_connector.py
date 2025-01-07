import time

class BlockchainConnector:
    def __init__(self, provider_url):
        self.provider_url = provider_url
        print(f"Connected to blockchain at {self.provider_url}")

    def send_data(self, data):
        print("Simulating blockchain transaction...")
        time.sleep(1)  # Simulate network delay
        transaction_id = f"txn_{int(time.time())}"
        print(f"Data sent to blockchain: {data}. Transaction ID: {transaction_id}")
        return {"transaction_id": transaction_id}

    def get_transaction_status(self, transaction_id):
        print(f"Fetching status for transaction: {transaction_id}")
        time.sleep(1)  # Simulate network delay
        return {"transaction_id": transaction_id, "status": "confirmed"}
