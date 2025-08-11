import tkinter as tk
from tkinter import ttk
from db.database import list_items

class SearchView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="🔍 Search Items", font=("Arial", 16)).pack(pady=10)

        self.search_var = tk.StringVar()
        bar = tk.Frame(self); bar.pack()
        tk.Entry(bar, textvariable=self.search_var, width=40).pack(side="left", padx=5)
        tk.Button(bar, text="Search", command=self.load_items).pack(side="left")

        self.tree = ttk.Treeview(self, columns=("Description","Location","Date Found"), show="headings")
        for col in ("Description","Location","Date Found"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        tk.Button(self, text="⬅ Back", command=lambda: self.switch_view("Home")).pack(pady=5)
        self.load_items()

    def load_items(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        for r in list_items():
            self.tree.insert("", "end", iid=r["id"],
                             values=(r["description"], r["location"], r["date_found"]))
