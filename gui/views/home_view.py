# gui/views/home_view.py
import tkinter as tk

class HomeView(tk.Frame):
    """Just navigation for now."""
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="🌸 Lost & Found — Home", font=("Arial", 18)).pack(pady=12)
        tk.Button(self, text="➕ Add Item", width=22,
                  command=lambda: self.switch_view("LogItem")).pack(pady=6)
        tk.Button(self, text="🔍 View Items", width=22,
                  command=lambda: self.switch_view("Search")).pack(pady=6)