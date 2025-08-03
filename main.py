import tkinter as tk
import sqlite3
from datetime import datetime

# Connect to SQLite (creates the DB if it doesn't exist)
conn = sqlite3.connect("data/local.db")
cur = conn.cursor()    

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    location TEXT,
    date_found TEXT
)
""")
conn.commit()

# Function to save item to DB
def save_item():
    desc = entry_desc.get()
    location = entry_location.get()
    date_found = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if desc and location:
        cur.execute("INSERT INTO items (description, location, date_found) VALUES (?, ?, ?)",
                    (desc, location, date_found))
        conn.commit()
        entry_desc.delete(0, tk.END)
        entry_location.delete(0, tk.END)
        lbl_status.config(text="✅ Item saved!")
    else:
        lbl_status.config(text="❌ Please fill all fields.")

# GUI setup
root = tk.Tk()
root.title("Lost & Found Tracker (Starter)")

tk.Label(root, text="Item Description").grid(row=0, column=0, padx=5, pady=5)
entry_desc = tk.Entry(root, width=40)
entry_desc.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Found At (Location)").grid(row=1, column=0, padx=5, pady=5)
entry_location = tk.Entry(root, width=40)
entry_location.grid(row=1, column=1, padx=5, pady=5)

btn_save = tk.Button(root, text="Save Item", command=save_item)
btn_save.grid(row=2, column=0, columnspan=2, pady=10)

lbl_status = tk.Label(root, text="", fg="blue")
lbl_status.grid(row=3, column=0, columnspan=2)

root.mainloop()

# Close connection on exit
conn.close()