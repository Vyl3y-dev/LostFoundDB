# db/database.py
from pathlib import Path
import sqlite3
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "data" / "local.db"

def _connect() -> sqlite3.Connection:
    """
    Return a sqlite3 connection to the project DB.
    TODO:
      - ensure DB_PATH.parent exists
      - set conn.row_factory = sqlite3.Row
    """
    # TODO: create parent dir: DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    # TODO: set row factory for name-based access
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    """
    Create required tables if they don't exist.
    Minimum schema for now:
      items(id INTEGER PK AUTOINCREMENT,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'TURNED_IN',
            date_logged TEXT NOT NULL)
    """
    # TODO: with _connect() as conn: execute CREATE TABLE IF NOT EXISTS ...

def add_item(description: str, location: str) -> None:
    """
    Insert a single item row.
    TODO:
      - basic validation (non-empty)
      - compute current timestamp (YYYY-MM-DD HH:MM)
      - INSERT into items(...)
    """
    # TODO: implement

def all_items() -> Iterable:
    """
    Return rows for the Search view.
    TODO:
      - SELECT * FROM items ORDER BY datetime(date_logged) DESC
      - return a list/iterable of rows
    """
    # TODO: implement
    return []