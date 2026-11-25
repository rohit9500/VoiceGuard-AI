import sqlite3
from pathlib import Path

DB_DIR = Path("database")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "history.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            filename TEXT,

            deepfake_prediction TEXT,

            deepfake_confidence REAL,

            transcript TEXT,

            scam_prediction TEXT,

            scam_confidence REAL,

            risk_score REAL

        )
        """)

        self.conn.commit()

    def insert(self,
               timestamp,
               filename,
               deepfake_prediction,
               deepfake_confidence,
               transcript,
               scam_prediction,
               scam_confidence,
               risk_score):

        self.cursor.execute("""
        INSERT INTO history(

            timestamp,
            filename,
            deepfake_prediction,
            deepfake_confidence,
            transcript,
            scam_prediction,
            scam_confidence,
            risk_score

        )

        VALUES(?,?,?,?,?,?,?,?)

        """,(timestamp,
             filename,
             deepfake_prediction,
             deepfake_confidence,
             transcript,
             scam_prediction,
             scam_confidence,
             risk_score))

        self.conn.commit()

    def fetch(self):

        self.cursor.execute("""

        SELECT *

        FROM history

        ORDER BY id DESC

        """)

        return self.cursor.fetchall()