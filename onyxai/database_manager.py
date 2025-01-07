import sqlite3

class DatabaseManager:
    def __init__(self, db_name="onyxai.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create tables for storing data.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id TEXT PRIMARY KEY,
                data TEXT,
                status TEXT
            )
        """)
        self.conn.commit()

    def insert_transaction(self, txn_id, data, status):
        """
        Insert a new transaction record.
        """
        self.cursor.execute("INSERT INTO transactions VALUES (?, ?, ?)", (txn_id, str(data), status))
        self.conn.commit()

    def get_transaction(self, txn_id):
        """
        Retrieve a transaction record by ID.
        """
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (txn_id,))
        return self.cursor.fetchone()
