import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view

        tk.Label(self, text="🏠 Home", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Log New Item",
                  command=lambda: self.switch_view("LogItem")).pack(pady=6)
        tk.Button(self, text="Search Items",
                  command=lambda: self.switch_view("Search")).pack(pady=6)
