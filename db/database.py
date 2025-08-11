import os, sqlite3
from datetime import datetime

DB_FILE = os.path.join("data", "local.db")

def _ensure_data_dir():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

def _connect():
    # Row factory lets you access cols by name: row["description"]
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    _ensure_data_dir()
    with _connect() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            location    TEXT NOT NULL,
            date_found  TEXT NOT NULL,
            claimed     INTEGER NOT NULL DEFAULT 0,
            date_claimed TEXT
        )
        """)
        # Optional: simple schema versioning
        cur.execute("""
        CREATE TABLE IF NOT EXISTS meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

# ---------- CRUD helpers ----------
def insert_item(description: str, location: str, date_found: str | None = None) -> int:
    if not date_found:
        date_found = datetime.now().strftime("%Y-%m-%d %H:%M")
    with _connect() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO items (description, location, date_found)
            VALUES (?, ?, ?)
        """, (description, location, date_found))
        return cur.lastrowid

def list_items(limit: int = 200, include_claimed: bool = True) -> list[sqlite3.Row]:
    q = "SELECT * FROM items"
    params = ()
    if not include_claimed:
        q += " WHERE claimed = 0"
    q += " ORDER BY datetime(date_found) DESC LIMIT ?"
    params += (limit,)
    with _connect() as conn:
        return conn.execute(q, params).fetchall()

def search_items(text: str = "", only_unclaimed: bool = False) -> list[sqlite3.Row]:
    clauses = []
    params = []
    if text:
        clauses.append("(description LIKE ? OR location LIKE ?)")
        like = f"%{text}%"
        params += [like, like]
    if only_unclaimed:
        clauses.append("claimed = 0")
    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    q = f"SELECT * FROM items{where} ORDER BY datetime(date_found) DESC"
    with _connect() as conn:
        return conn.execute(q, params).fetchall()

def mark_claimed(item_id: int) -> None:
    with _connect() as conn:
        conn.execute("""
            UPDATE items
            SET claimed = 1, date_claimed = ?
            WHERE id = ?
        """, (datetime.now().strftime("%Y-%m-%d %H:%M"), item_id))

def update_item(item_id: int, *, description: str | None = None, location: str | None = None) -> None:
    sets, params = [], []
    if description is not None:
        sets.append("description = ?"); params.append(description)
    if location is not None:
        sets.append("location = ?"); params.append(location)
    if not sets:
        return
    params.append(item_id)
    with _connect() as conn:
        conn.execute(f"UPDATE items SET {', '.join(sets)} WHERE id = ?", params)

def delete_item(item_id: int) -> None:
    with _connect() as conn:
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
