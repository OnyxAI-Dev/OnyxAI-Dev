from onyxai.ai_engine import AIEngine
from onyxai.blockchain_connector import BlockchainConnector
from config.settings import BLOCKCHAIN_PROVIDER

class Core:
    def __init__(self):
        print("Initializing OnyxAI Core...")
        self.ai_engine = AIEngine()
        self.blockchain_connector = BlockchainConnector(BLOCKCHAIN_PROVIDER)

    def start_interactive_mode(self):
        print("Entering interactive mode. Type 'exit' to quit.")
        while True:
            user_input = input(">> Enter data: ")
            if user_input.lower() == "exit":
                print("Exiting interactive mode.")
                break
            processed_data = self.ai_engine.process_data({"input": user_input})
            print(f"Processed Data: {processed_data}")
            self.blockchain_connector.send_data(processed_data)

    def process_batch_jobs(self):
        print("Processing batch jobs...")
        sample_data = [{"job_id": 1, "content": "example1"}, {"job_id": 2, "content": "example2"}]
        for data in sample_data:
            processed_data = self.ai_engine.process_data(data)
            self.blockchain_connector.send_data(processed_data)
