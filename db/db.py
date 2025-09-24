import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("data", "itemlog.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        description TEXT NOT NULL,
        location_found TEXT NOT NULL,
        found_by TEXT,
        claimed INTEGER DEFAULT 0,
        claimed_by TEXT,
        logged_by TEXT NOT NULL,
        date_added TEXT DEFAULT (date('now')) NOT NULL,
        date_claimed TEXT DEFAULT (date('now'))
    )
    ''')
    conn.commit()
    conn.close()

def insert_item(name, desc, location, foundBy, claimed, claimedBy, loggedBy, dateAdded, dateClaimed):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO Items (item_name, description, location_found, found_by, claimed, claimed_by, logged_by, date_added, date_claimed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (name, desc, location, foundBy, claimed, claimedBy, loggedBy, dateAdded, dateClaimed))
    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Items ORDER BY id DESC')
    results = cur.fetchall()
    conn.close()
    return results