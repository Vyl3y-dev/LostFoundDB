import tkinter as tk
from gui.views.home_view import HomeView
from db.database import init_db

class AppController:
    def __init__(self, root):
        self.root = root
        self.container = tk.Frame(root)
        self.container.pack(fill='both', expand=True)
        self.current_view = None
        self.show_view(HomeView)

    def show_view(self, view_class):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self.container, self)
        self.current_view.pack(fill='both', expand=True)

def launch_app():
    init_db()
    root = tk.Tk()
    root.title("Lost & Found System")
    root.geometry("800x600")
    AppController(root)
    root.mainloop()