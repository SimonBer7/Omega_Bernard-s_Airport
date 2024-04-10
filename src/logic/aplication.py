
from src.views.main_view import MainWindow
from src.data.models.passenger import Passenger
from src.data.dao.passengerDao import PassengerDao


class Application:
    def __init__(self, db):
        self.running = False
        self.database = db
        self.user_interface = None
        self.logged_user = None
        self.admin = Passenger("Admin", "admin@gmail.com", "admin", "111111111", "111111/1111")
        self.passenger_dao = PassengerDao(self.database)

    def start(self):
        self.running = True
        self.main_win()

    def main_win(self):
        main = MainWindow(self)
        main.mainloop()




    def authorization(self, email, password):
        try:
            user = self.passenger_dao.read_to_login(email, password)
            if user is None:
                raise Exception("Error, there is some problem with login")
            else:
                self.logged_user = Passenger(user.name, user.email, user.password, user.phone_num, user.pin)
                return True
        except Exception as e:
            print(e)
            return False

    def registration(self, passenger):
        try:
            message = self.passenger_dao.insert(passenger)
            if message is None:
                raise Exception("Error, there is some problem with inserting")
            else:
                return True
        except Exception as e:
            print(e)
            return False




