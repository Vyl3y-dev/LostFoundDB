import sqlite3
import os

DB_PATH = os.path.join("data", "lostfound.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            description TEXT,
            date_reported TEXT,
            location_found TEXT,
            status TEXT DEFAULT 'lost',
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()