import tkinter as tk

class SearchView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Search Lost Items", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_view(HomeView)).pack(pady=10)

from gui.views.home_view import HomeView