import sqlite3
import threading

class DBConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path, check_same_thread=False, timeout=10)
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA journal_mode=WAL")  # Optional but improves concurrency

    @classmethod
    def get_instance(cls, db_path):
        with cls._lock:
            if cls._instance is None:
                cls._instance = DBConnection(db_path)
            return cls._instance

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def executescript(self, script):
        self.cursor.executescript(script)
        self.connection.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.connection.commit()
        self.connection.close()
        DBConnection._instance = None
