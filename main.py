
from src.data.database import Database
from src.logic.aplication import Application


def main():
    database = Database()
    app = Application(database)
    app.start()


if __name__ == "__main__":
    main()
