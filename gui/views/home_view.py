import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Welcome to Lost & Found", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="Log New Item", command=lambda: controller.show_view(LogItemView)).pack(pady=10)
        tk.Button(self, text="Search Items", command=lambda: controller.show_view(SearchView)).pack(pady=10)

# Avoid circular imports at top
from gui.views.log_item_view import LogItemView
from gui.views.search_view import SearchView