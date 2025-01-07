import argparse
import logging
from onyxai.core import Core
from config.settings import APP_NAME, VERSION

# Set up logging
logging.basicConfig(
    filename='onyxai.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def display_banner():
    """
    Display a welcome banner with application details.
    """
    print(f"""
    ================================
    Welcome to {APP_NAME} (v{VERSION})
    ================================
    """)

def interactive_menu(core):
    """
    Interactive menu system for user commands.
    """
    while True:
        print("\nSelect an option:")
        print("1. Process single input")
        print("2. Simulate batch processing")
        print("3. Check blockchain transaction status")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            user_input = input("Enter data to process: ").strip()
            if user_input:
                processed_data = core.ai_engine.process_data({"input": user_input})
                print(f"Processed Data: {processed_data}")
                tx = core.blockchain_connector.send_data(processed_data)
                print(f"Transaction ID: {tx['transaction_id']}")
                logging.info(f"Processed and sent data: {processed_data}")
            else:
                print("Input cannot be empty.")
        
        elif choice == "2":
            print("Simulating batch processing...")
            core.process_batch_jobs()
        
        elif choice == "3":
            tx_id = input("Enter transaction ID to check: ").strip()
            if tx_id:
                status = core.blockchain_connector.get_transaction_status(tx_id)
                print(f"Transaction Status: {status['status']}")
                logging.info(f"Checked status for transaction ID: {tx_id}")
            else:
                print("Transaction ID cannot be empty.")
        
        elif choice == "4":
            print("Exiting OnyxAI. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    """
    Main entry point of the application.
    """
    parser = argparse.ArgumentParser(description=f"{APP_NAME} Decentralized AI Platform")
    parser.add_argument(
        '--mode',
        type=str,
        default="interactive",
        choices=["interactive", "batch"],
        help="Run mode: interactive or batch"
    )
    args = parser.parse_args()
    
    logging.info(f"Starting {APP_NAME} in {args.mode} mode.")
    
    display_banner()
    core = Core()
    
    if args.mode == "interactive":
        print("Entering Interactive Mode...")
        interactive_menu(core)
    elif args.mode == "batch":
        print("Processing batch jobs...")
        core.process_batch_jobs()
        logging.info("Batch processing completed.")

if __name__ == "__main__":
    main()
