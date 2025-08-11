# main.py
import sys
import traceback
import tkinter as tk
from tkinter import messagebox

from db.database import init_db
from gui.main_window import MainWindow

def main() -> int:
    try:
        # 1) Ensure database/tables exist
        init_db()

        # 2) Launch the GUI (single root window)
        app = MainWindow()
        app.mainloop()
        return 0

    except Exception as e:
        # Top-level crash handler: show a friendly popup and print a traceback
        try:
            # If Tk hasn't started yet, create a hidden root for the messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Unexpected Error", f"{type(e).__name__}: {e}")
            root.destroy()
        except Exception:
            # If even Tk is unhappy, at least dump to stderr
            print("Fatal error:", file=sys.stderr)
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
