import time

class TransactionManager:
    def __init__(self):
        self.transactions = {}

    def create_transaction(self, data):
        """
        Simulate creating a blockchain transaction.
        """
        transaction_id = f"txn_{int(time.time())}"
        self.transactions[transaction_id] = {"data": data, "status": "pending"}
        print(f"Transaction {transaction_id} created.")
        return transaction_id

    def update_transaction_status(self, transaction_id, status):
        """
        Update the status of a blockchain transaction.
        """
        if transaction_id in self.transactions:
            self.transactions[transaction_id]["status"] = status
            print(f"Transaction {transaction_id} status updated to {status}.")
        else:
            raise ValueError("Transaction ID not found.")

    def get_transaction(self, transaction_id):
        """
        Retrieve transaction details.
        """
        return self.transactions.get(transaction_id, "Transaction not found.")
