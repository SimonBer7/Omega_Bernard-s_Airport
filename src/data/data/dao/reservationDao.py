"""
Module: ReservationDao

This module contains the ReservationDao class, which provides methods for interacting with a reservation database.
"""

from src.logic.log_writter import Log_writter

class ReservationDao:
    """
    A class representing a data access object for handling reservation data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the ReservationDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writter = Log_writter()

    def insert(self, res):
        """
        Inserts a new reservation into the database.

        Parameters:
        - res: An object representing the reservation to be inserted.

        Returns:
        - True if the reservation was successfully inserted, False otherwise.
        """
        try:
            if res is None:
                raise ValueError()
            sql_statement = "INSERT INTO reservation(pin, passenger_id, flight_id, date, price) VALUES (?, ?, ?, ?, ?);"
            date_str = res.date.strftime('%Y-%m-%d %H:%M:%S')
            values = (int(res.pin), int(res.passenger_id), int(res.flight_id), date_str, int(res.price))
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Reservation was created :)")
            return True
        except ValueError:
            self.log_writter.write_to_log("Error with creating reservation")
            return False

    def read(self):
        """
        Retrieves all reservations from the database.

        Returns:
        - A list of all reservations in the database.
        """
        try:
            sql_statement = "SELECT * FROM print_all_reservations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            self.log_writter.write_to_log("Error with reading destinations from database")

    def read_reservations(self, passenger_id, pin):
        """
        Retrieves reservations for a specific passenger from the database.

        Parameters:
        - passenger_id: The ID of the passenger.
        - pin: The PIN of the passenger.

        Returns:
        - A list of reservations for the specified passenger.
        """
        try:
            if passenger_id is None or pin is None:
                raise ValueError()
            sql_statement = "EXEC print_reservation_detail ?, ?"
            values = (int(passenger_id), int(pin))
            data = self.database.execute_with_data(sql_statement, values)
            return data
        except ValueError:
            self.log_writter.write_to_log("Error with reading from database")

    def update(self, pin, new_price):
        """
        Updates the price of a reservation in the database.

        Parameters:
        - pin: The PIN of the reservation.
        - new_price: The new price of the reservation.

        Returns:
        - None
        """
        try:
            if pin is None or new_price is None:
                raise ValueError()

            sql_statement = "UPDATE reservation SET price = ? WHERE pin = ?"
            values = (int(new_price), int(pin))
            self.database.execute(sql_statement, values)
        except ValueError:
            self.log_writter.write_to_log("Error with updating price")

    def delete(self, pin):
        """
        Deletes a reservation from the database.

        Parameters:
        - pin: The PIN of the reservation to be deleted.

        Returns:
        - True if the reservation was successfully deleted, False otherwise.
        """
        try:
            if pin is None:
                raise ValueError()
            sql_statement = "DELETE FROM reservation WHERE pin = ?"
            values = (int(pin),)
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Reservation was deleted")
            return True
        except ValueError:
            self.log_writter.write_to_log("Error with deleting reservation")
            return False

    def delete_by_pas_id(self, id):
        """
        Deletes reservations for a specific passenger from the database.

        Parameters:
        - id: The ID of the passenger whose reservations are to be deleted.

        Returns:
        - True if the reservations were successfully deleted, False otherwise.
        """
        try:
            if id is None:
                raise ValueError()
            sql_statement = "DELETE FROM reservation WHERE passenger_id = ?"
            values = (int(id),)
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Reservation was deleted")
            return True
        except ValueError:
            self.log_writter.write_to_log("Error with deleting reservation")
            return False
