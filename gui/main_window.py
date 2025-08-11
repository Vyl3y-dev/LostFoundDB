import tkinter as tk
from gui.views.home_view import HomeView
from gui.views.log_item_view import LogItemView
from gui.views.search_view import SearchView

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lost & Found App")
        self.geometry("700x450")
        self._current = None
        self._views = {
            "Home": HomeView,
            "LogItem": LogItemView,
            "Search": SearchView,
        }
        self.show_frame("Home")

    def show_frame(self, name: str):
        if self._current:
            self._current.destroy()
        view_cls = self._views[name]
        # pass the callback into the view
        self._current = view_cls(self, self.show_frame)
        self._current.pack(fill="both", expand=True)
