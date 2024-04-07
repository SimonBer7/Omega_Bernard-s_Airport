
from src.data.database import Database
from src.logic.aplication import Application
import tkinter as tk

def main():
    root = tk.Tk()
    database = Database()
    app = Application(database, root)
    app.start()
    root.mainloop()


if __name__ == "__main__":
    main()
