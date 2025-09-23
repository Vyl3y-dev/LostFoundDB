import sqlite3
import os

DB_PATH = os.path.join("data", "lostandfound.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        description TEXT,
        location_found TEXT
    )
    ''')
    conn.commit()
    conn.close()

def insert_item(name, desc, location):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO Items (item_name, description, location_found) VALUES (?, ?, ?)',
                (name, desc, location))
    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Items ORDER BY id DESC')
    results = cur.fetchall()
    conn.close()
    return results