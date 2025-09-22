# main.py
from db.database import init_db
from gui.main_window import MainWindow

def main():
    """App entrypoint: init DB, launch GUI."""
    init_db()           # TODO: implement inside db/database.py
    app = MainWindow()  # TODO: implement inside gui/main_window.py
    app.mainloop()

if __name__ == "__main__":
    main()