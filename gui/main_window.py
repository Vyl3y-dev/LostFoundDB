# gui/main_window.py
import tkinter as tk

class MainWindow(tk.Tk):
    """
    Root window that manages swapping view frames ("scenes").
    You will:
      - set title/geometry
      - keep a dict of view name -> view class
      - implement show_frame(name) to destroy previous frame and mount new one
    """
    def __init__(self):
        super().__init__()
        self.title("Lost & Found 💗 (learning mode)")
        self.geometry("720x480")
        self._current = None

        # Lazy import after Tk is ready to avoid circular imports during early edits
        from gui.views.home_view import HomeView
        from gui.views.log_item_view import LogItemView
        from gui.views.search_view import SearchView

        self._views = {
            "Home": HomeView,
            "LogItem": LogItemView,
            "Search": SearchView,
        }
        self.show_frame("Home")

    def show_frame(self, name: str):
        """Destroy current view and mount the requested one."""
        if self._current:
            self._current.destroy()
        view_cls = self._views[name]
        # pass the scene switcher callback into the view
        self._current = view_cls(self, self.show_frame)
        self._current.pack(fill="both", expand=True)