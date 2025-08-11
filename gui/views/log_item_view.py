import tkinter as tk
from datetime import datetime
from db.database import insert_item

class LogItemView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="📝 Log New Item", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Name/Description of the Item", font=("Arial", 10)).pack(pady=0)
        self.desc = tk.Entry(self, width=50); self.desc.pack(pady=0)
        #self.space = pack
        tk.Label(self, text="Location where Item was found", font=("Arial", 10)).pack(pady=0)
        self.loc = tk.Entry(self, width=50);  self.loc.pack(pady=0)
        self.status = tk.Label(self, text="", fg="blue"); self.status.pack()

        tk.Button(self, text="Save", command=self.save_item).pack(pady=10)
        tk.Button(self, text="⬅ Back", command=lambda: self.switch_view("Home")).pack()

    def save_item(self):
        d = self.desc.get().strip()
        l = self.loc.get().strip()
        if d and l:
            insert_item(d, l, datetime.now().strftime("%Y-%m-%d %H:%M"))
            self.status.config(text="✅ Saved!", fg="green")
            self.desc.delete(0, tk.END); self.loc.delete(0, tk.END)
        else:
            self.status.config(text="❌ Please fill out all fields.", fg="red")
