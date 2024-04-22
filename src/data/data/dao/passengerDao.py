"""
Module: PassengerDao

This module contains the PassengerDao class, which provides methods for interacting with a passenger database.
"""

import re
from src.data.models.passenger import Passenger
from src.logic.log_writter import Log_writter

class PassengerDao:
    """
    A class representing a data access object for handling passenger data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the PassengerDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writter = Log_writter()

    def insert(self, passenger):
        """
        Inserts a new passenger into the database.

        Parameters:
        - passenger: An object representing the passenger to be inserted.

        Returns:
        - True if the passenger was successfully inserted, False otherwise.
        """
        try:
            if passenger is None:
                raise Exception("Invalid passenger object")

            sql_statement = "INSERT INTO passenger(name, email, password, phone_num, pin) VALUES (?, ?, ?, ?, ?);"
            values = (
                str(passenger.get_name()), str(passenger.get_email()),
                str(passenger.hash_password(passenger.get_password())), str(passenger.get_phone_num()), str(passenger.get_pin())
            )
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Passenger was created :)")
            return True
        except Exception as e:
            self.log_writter.write_to_log(f"Error inserting passenger into the database: {str(e)}")
            return False

    def read_id(self, pin):
        """
        Retrieves the ID of a passenger by their PIN.

        Parameters:
        - pin: The PIN of the passenger.

        Returns:
        - The ID of the passenger if found, None otherwise.
        """
        if pin is None:
            raise ValueError()

        sql_statement = "SELECT passenger.id FROM passenger WHERE pin = ?"
        values = (str(pin),)
        data = self.database.execute_for_agr(sql_statement, values)
        return data

    def read(self, pin):
        """
        Retrieves all flights associated with a passenger.

        Parameters:
        - pin: The PIN of the passenger.

        Returns:
        - A list of all flights associated with the passenger or an error message if no flights are found.
        """
        try:
            if pin is None:
                raise ValueError()
            sql_statement = "EXEC print_user_flights ?"
            values = (str(pin),)
            data = self.database.execute_with_data(sql_statement, values)
            return data
        except ValueError:
            self.log_writter.write_to_log("Error with reading from database")

    def read_to_login(self, email, password):
        """
        Retrieves a passenger's information for login verification.

        Parameters:
        - email: The email of the passenger.
        - password: The password of the passenger.

        Returns:
        - A Passenger object if the email and password match, None otherwise.
        """
        try:
            if email is None or password is None:
                raise ValueError("Email and password are required for login")

            password = Passenger.hash_password(password)
            sql_statement = "SELECT name, email, password, phone_num, pin FROM passenger WHERE email = ? AND password = ?;"
            values = (str(email), str(password))
            data = self.database.execute_with_data(sql_statement, values)

            if data:
                id = data[0]
                passenger = Passenger(id[0], id[1], id[2], id[3], id[4])
                return passenger
            else:
                return None
        except Exception as e:
            self.log_writter.write_to_log(f"Error with reading from database: {e}")
            return None

    def read_all_passengers(self):
        """
        Retrieves all passengers from the database.

        Returns:
        - A list of all passengers in the database.
        """
        sql_statement = "SELECT * FROM print_all_passengers;"
        data = self.database.execute_with_data(sql_statement, None)
        return data

    def read_reservations(self, passenger_id):
        """
        Retrieves all reservations associated with a passenger.

        Parameters:
        - passenger_id: The ID of the passenger.

        Returns:
        - A list of all reservations associated with the passenger or an error message if no reservations are found.
        """
        try:
            if passenger_id is None:
                raise ValueError()
            sql_statement = "EXEC print_reservations ?"
            values = (int(passenger_id),)
            data = self.database.execute_with_data(sql_statement, values)
            return data
        except ValueError:
            self.log_writter.write_to_log("Error with reading from database")

    def update(self, new_email, old_email, password):
        """
        Updates a passenger's email address.

        Parameters:
        - new_email: The new email address.
        - old_email: The old email address.
        - password: The password of the passenger for authentication.

        Returns:
        - True if the email was successfully updated, False otherwise.
        """
        try:
            if password is None or new_email is None or old_email is None:
                raise Exception("Invalid values")

            if self.is_valid_email(new_email):
                password = Passenger.hash_password(password)
                sql_statement = "UPDATE passenger SET email = ? WHERE email = ? AND password = ?;"
                values = (str(new_email), str(old_email), str(password))
                self.database.execute(sql_statement, values)
                self.log_writter.write_to_log("Passenger's email was updated :)")
                return True
        except Exception as e:
            self.log_writter.write_to_log("Error, there is some problem with updating")
            return False

    def delete(self, passenger):
        """
        Deletes a passenger from the database.

        Parameters:
        - passenger: An object representing the passenger to be deleted.

        Returns:
        - True if the passenger was successfully deleted, False otherwise.
        """
        try:
            if passenger is None:
                raise ValueError("Invalid passenger object")
            sql_statement = "DELETE FROM passenger WHERE name = ? and email = ? and password = ? and phone_num = ? and pin = ?;"
            values = (
                str(passenger.name),
                str(passenger.email),
                str(passenger.password),
                str(passenger.phone_num),
                str(passenger.pin)
            )
            self.database.execute(sql_statement, values)
            return True
        except ValueError as ve:
            self.log_writter.write_to_log(f"Error: {ve}")
            return False
        except Exception as e:
            self.log_writter.write_to_log(f"Error deleting passenger from the database: {str(e)}")
            return False

    def delete_passenger_reservation(self, passenger_id):
        """
        Deletes all reservations associated with a passenger.

        Parameters:
        - passenger_id: The ID of the passenger.

        Returns:
        - True if the reservations were successfully deleted, False otherwise.
        """
        try:
            if passenger_id is None:
                raise ValueError("Invalid passenger object")
            sql_statement = "DELETE FROM reservation WHERE passenger_id = ?;"
            values = (
                int(passenger_id),
            )
            self.database.execute(sql_statement, values)
            return True
        except ValueError as ve:
            self.log_writter.write_to_log(f"Error: {ve}")
            return False
        except Exception as e:
            self.log_writter.write_to_log(f"Error deleting passenger from the database: {str(e)}")
            return False

    def admin_delete_by_pin(self, pin):
        """
        Deletes a passenger by their PIN. (Admin functionality)

        Parameters:
        - pin: The PIN of the passenger.

        Returns:
        - True if the passenger was successfully deleted by the admin, False otherwise.
        """
        try:
            if pin is None:
                raise ValueError()
            sql_statement = "DELETE FROM passenger WHERE pin = ?;"
            values = (str(pin),)
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Passenger was deleted by admin")
            return True
        except ValueError:
            self.log_writter.write_to_log("Error with deleting passenger")
            return False

    def is_valid_email(self, email):
        """
        Validates an email address using regular expressions.

        Parameters:
        - email: The email address to validate.

        Returns:
        - True if the email address is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return True
        else:
            return False
