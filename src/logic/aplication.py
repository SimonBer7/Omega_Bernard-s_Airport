"""
Class: Application

This class represents the main application logic for the flight reservation system. It interacts with the database through various data access objects (DAOs) to perform operations such as user authentication, registration, profile management, and data retrieval.

Attributes:
- running (bool): Indicates whether the application is running.
- database (Database): An instance of the Database class for database interactions.
- user_interface (MainWindow): An instance of the MainWindow class for user interface.
- logged_user (Passenger): An instance of the Passenger class representing the currently logged-in user.
- users_reservation (list): A list containing reservations associated with the logged-in user.
- log_writer (Log_writer): An instance of the Log_writer class for logging application activities.
- database_checker (Database_checker): An instance of the Database_checker class for checking database tables.
- passenger_dao (PassengerDao): An instance of the PassengerDao class for passenger-related database operations.
- pilot_dao (PilotDao): An instance of the PilotDao class for pilot-related database operations.
- plane_dao (PlaneDao): An instance of the PlaneDao class for plane-related database operations.
- destination_dao (DestinationDao): An instance of the DestinationDao class for destination-related database operations.
- flight_dao (FlightDao): An instance of the FlightDao class for flight-related database operations.
- reservation_dao (ReservationDao): An instance of the ReservationDao class for reservation-related database operations.

Methods:
- start(self): Starts the application by initializing necessary components and showing the main window.
- main_win(self): Displays the main window of the application.
- authorization(self, email, password): Authenticates a user based on provided email and password.
- registration(self, passenger): Registers a new passenger in the system.
- change_email(self, new_email, old_email, password): Updates the email of the logged-in user.
- update_profile(self, new_email): Updates the profile of the logged-in user.
- delete_account(self): Deletes the account of the logged-in user.
- load_passengers(self): Retrieves all passengers from the database.
- load_pilots(self): Retrieves all pilots from the database.
- load_planes(self): Retrieves all planes from the database.
- load_destinations(self): Retrieves all destinations from the database.
- load_flights(self): Retrieves all flights from the database.
- load_reservations(self): Retrieves all reservations from the database.
"""

from src.presentation.main_view import MainWindow
from src.logic.database_checker import Database_checker
from src.data.models.passenger import Passenger
from src.data.dao.passengerDao import PassengerDao
from src.data.dao.pilotDao import PilotDao
from src.data.dao.planeDao import PlaneDao
from src.data.dao.destinationDao import DestinationDao
from src.data.dao.flightDao import FlightDao
from src.data.dao.reservationDao import ReservationDao
from src.logic.log_writter import Log_writter


class Application:
    """
    Class representing the main application logic for the flight reservation system.
    """

    def __init__(self, db):
        """
        Initializes a new Application object.

        Parameters:
        - db (Database): An instance of the Database class for database interactions.
        """
        self.running = False
        self.database = db
        self.user_interface = None
        self.logged_user = None
        self.users_reservation = None
        self.log_writer = Log_writter()
        self.database_checker = Database_checker(self, db)
        self.passenger_dao = PassengerDao(self.database)
        self.pilot_dao = PilotDao(self.database)
        self.plane_dao = PlaneDao(self.database)
        self.destination_dao = DestinationDao(self.database)
        self.flight_dao = FlightDao(self.database)
        self.reservation_dao = ReservationDao(self.database)

    def start(self):
        """
        Starts the application by initializing necessary components and showing the main window.
        """
        self.running = True
        self.main_win()

    def main_win(self):
        """
        Displays the main window of the application.
        """
        main = MainWindow(self)
        self.database_checker.check_tables()
        main.mainloop()

    def authorization(self, email, password):
        """
        Authenticates a user based on provided email and password.

        Parameters:
        - email (str): The email of the user.
        - password (str): The password of the user.

        Returns:
        - bool: True if authentication is successful, False otherwise.
        """
        try:
            user = self.passenger_dao.read_to_login(email, password)
            if user is None:
                raise Exception("Error, there is some problem with login")
            else:
                self.logged_user = Passenger(user.name, user.email, user.password, user.phone_num, user.pin)
                self.users_reservation = self.passenger_dao.read_reservations(
                    self.passenger_dao.read_id(self.logged_user.get_pin()))
                self.database_checker.show_flights()
                return True
        except Exception as e:
            self.log_writer.write_to_log(e)
            return False

    def registration(self, passenger):
        """
        Registers a new passenger in the system.

        Parameters:
        - passenger (Passenger): An instance of Passenger representing the new passenger.

        Returns:
        - bool: True if registration is successful, False otherwise.
        """
        try:
            message = self.passenger_dao.insert(passenger)
            if message is None:
                raise Exception("Error, there is some problem with inserting")
            else:
                return True
        except Exception as e:
            self.log_writer.write_to_log(e)
            return False

    def change_email(self, new_email, old_email, password):
        """
        Updates the email of the logged-in user.

        Parameters:
        - new_email (str): The new email.
        - old_email (str): The old email.
        - password (str): The password of the user.

        Returns:
        - bool: True if email is successfully updated, False otherwise.
        """
        try:
            if self.logged_user.get_email() == old_email:
                message = self.passenger_dao.update(new_email, old_email, password)
                if message is False:
                    raise Exception("Error, there is some problem with update")
                else:
                    self.update_profile(new_email)
                    return True
        except Exception as e:
            self.log_writer.write_to_log(e)
            return False

    def update_profile(self, new_email):
        """
        Updates the profile of the logged-in user.

        Parameters:
        - new_email (str): The new email.
        """
        try:
            if new_email is None:
                raise Exception("Invalid input")
            else:
                self.logged_user.email = new_email
        except Exception as e:
            self.log_writer.write_to_log(e)

    def delete_account(self):
        """
        Deletes the account of the logged-in user.

        Returns:
        - bool: True if the account is successfully deleted, False otherwise.
        """
        if self.passenger_dao.delete_passenger_reservation(
                self.passenger_dao.read_id(self.logged_user.get_pin())) and self.passenger_dao.delete(
            self.logged_user):
            return True
        else:
            return False

    def load_passengers(self):
        """
        Retrieves all passengers from the database.

        Returns:
        - list: A list containing passenger data.
        """
        data = self.passenger_dao.read_all_passengers()
        return data

    def load_pilots(self):
        """
        Retrieves all pilots from the database.

        Returns:
        - list: A list containing pilot data.
        """
        data = self.pilot_dao.read_all_pilots()
        return data

    def load_planes(self):
        """
        Retrieves all planes from the database.

        Returns:
        - list: A list containing plane data.
        """
        data = self.plane_dao.read_all_planes()
        return data

    def load_destinations(self):
        """
        Retrieves all destinations from the database.

        Returns:
        - list: A list containing destination data.
        """
        data = self.destination_dao.read_all_destinations()
        return data

    def load_flights(self):
        """
        Retrieves all flights from the database.

        Returns:
        - list: A list containing flight data.
        """
        data = self.flight_dao.read()
        return data

    def load_reservations(self):
        """
        Retrieves all reservations from the database.

        Returns:
        - list: A list containing reservation data.
        """
        data = self.reservation_dao.read()
        return data
