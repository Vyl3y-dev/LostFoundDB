# gui/views/search_view.py
import tkinter as tk
from tkinter import ttk

class SearchView(tk.Frame):
    """Read-only list of items. You will wire DB loading yourself."""
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="🔎 Items", font=("Arial", 16)).pack(pady=8)

        # Table
        self.tree = ttk.Treeview(self, columns=("id","desc","loc","date"), show="headings", height=12)
        for col, w in (("id",60), ("desc",300), ("loc",200), ("date",140)):
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=w, anchor="w")
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        controls = tk.Frame(self); controls.pack(fill="x")
        tk.Button(controls, text="Reload (stub)", command=self.reload).pack(side="left", padx=4)
        tk.Button(controls, text="⬅ Back", command=lambda: self.switch_view("Home")).pack(side="right", padx=4)

        self.reload()

    def reload(self):
        """TODO: load rows from db.database.all_items() and insert into tree."""
        # clear
        for iid in self.tree.get_children():
            self.tree.delete(iid)

        # TODO:
        # from db.database import all_items
        # rows = all_items()
        # for r in rows:
        #     self.tree.insert("", "end", iid=r["id"], values=(r["id"], r["description"], r["location"], r["date_logged"]))

        # placeholder row so you see something
        self.tree.insert("", "end", values=("—", "(stub) add your DB call", "", ""))