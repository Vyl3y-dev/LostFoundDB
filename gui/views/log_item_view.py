# gui/views/log_item_view.py
import tkinter as tk
from tkinter import messagebox
# NOTE: you will import add_item from db.database AFTER you implement it.

class LogItemView(tk.Frame):
    """Form to add a new item. You will wire the DB call yourself."""
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="📝 Add Item", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Description").grid(row=1, column=0, sticky="e", padx=6, pady=3)
        self.e_desc = tk.Entry(self, width=45); self.e_desc.grid(row=1, column=1, padx=6, pady=3)

        tk.Label(self, text="Location Found").grid(row=2, column=0, sticky="e", padx=6, pady=3)
        self.e_loc = tk.Entry(self, width=45); self.e_loc.grid(row=2, column=1, padx=6, pady=3)

        tk.Button(self, text="Save", command=self._on_save).grid(row=3, column=0, pady=10)
        tk.Button(self, text="⬅ Back", command=lambda: self.switch_view("Home")).grid(row=3, column=1, pady=10, sticky="e")

        self.status = tk.Label(self, text="", fg="blue"); self.status.grid(row=4, column=0, columnspan=2)

    def _on_save(self):
        """TODO: validate inputs and call db.database.add_item."""
        d = (self.e_desc.get() or "").strip()
        l = (self.e_loc.get() or "").strip()
        if not (d and l):
            messagebox.showwarning("Almost!", "Please fill in both fields 💖")
            return

        # TODO:
        # from db.database import add_item
        # add_item(d, l)

        self.status.config(text="(stub) Saved! Wire DB next ✨")
        self.e_desc.delete(0, tk.END); self.e_loc.delete(0, tk.END)