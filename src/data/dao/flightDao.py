"""
Module: FlightDao

This module contains the FlightDao class, which provides methods for interacting with a flight database.
"""

import datetime
from src.logic.log_writter import Log_writter

class FlightDao:
    """
    A class representing a data access object for handling flight data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the FlightDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writer = Log_writter()

    def insert(self, flight):
        """
        Inserts a new flight into the database.

        Parameters:
        - flight: An object representing the flight to be inserted.

        Returns:
        - None
        """
        try:
            if flight is None:
                raise Exception("Invalid flight object")

            sql_statement = "INSERT INTO flight(fly_number, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price) VALUES (?, ?, ?, ?, ?, ?, ?);"
            values = (
                int(flight.get_fly_number()), int(flight.get_destination_id()), int(flight.get_plane_id()),
                int(flight.get_pilot_id()), datetime.datetime.strptime(flight.get_date_leaving(), "%Y-%m-%d").date(),
                datetime.datetime.strptime(flight.get_date_arriving(), "%Y-%m-%d").date(), int(flight.get_price())
            )
            self.database.execute(sql_statement, values)
            self.log_writer.write_to_log("Flight was created")
        except Exception as e:
            self.log_writer.write_to_log(f"Error inserting flight into the database: {str(e)}")

    def read(self):
        """
        Retrieves all flights from the database.

        Returns:
        - A list of all flights in the database or a message indicating no flights available.
        """
        try:
            sql_statement = "SELECT * FROM print_all_flights;"
            result = self.database.execute_with_data(sql_statement, None)
            if result:
                return result
            else:
                return "No flights available."
        except Exception as e:
            self.log_writer.write_to_log(f"Error with printing flights from the database: {str(e)}")

    def read_flight_id(self, fly_num):
        """
        Retrieves the ID of a flight by its flight number.

        Parameters:
        - fly_num: The flight number.

        Returns:
        - The ID of the flight if found, None otherwise.
        """
        try:
            if fly_num is None:
                raise ValueError()
            sql_statement = "SELECT flight.id FROM flight WHERE fly_number = ?"
            values = (int(fly_num),)
            flight_id = self.database.execute_for_agr(sql_statement, values)
            if flight_id:
                return flight_id
            else:
                self.log_writer.write_to_log("There isn't a flight with this number")
        except ValueError:
            self.log_writer.write_to_log("Error invalid format")
        except Exception:
            self.log_writer.write_to_log("Error with reading from the database")

    def read_flight_price(self, fly_num):
        """
        Retrieves the price of a flight by its flight number.

        Parameters:
        - fly_num: The flight number.

        Returns:
        - The price of the flight if found, None otherwise.
        """
        try:
            if fly_num is None:
                raise ValueError()

            sql_statement = "SELECT flight.price FROM flight WHERE fly_number = ?;"
            values = (int(fly_num),)
            price = self.database.execute_for_agr(sql_statement, values)
            return price
        except ValueError:
            self.log_writer.write_to_log("Error with reading price from the database")

    def update(self, fly_num, new_price):
        """
        Updates the price of a flight.

        Parameters:
        - fly_num: The flight number.
        - new_price: The new price value.

        Returns:
        - None
        """
        try:
            if fly_num is None or new_price is None:
                raise ValueError()

            sql_statement = "UPDATE flight SET price = ? WHERE fly_number = ?"
            values = (int(new_price), int(fly_num))
            self.database.execute(sql_statement, values)
        except ValueError:
            self.log_writer.write_to_log("Error with updating price")

    def delete(self, fly_num):
        """
        Deletes a flight from the database.

        Parameters:
        - fly_num: The flight number.

        Returns:
        - True if the flight was successfully deleted, False otherwise.
        """
        try:
            if fly_num is None:
                raise ValueError()

            sql_statement = "DELETE FROM flight WHERE fly_number = ?"
            values = (int(fly_num),)
            self.database.execute(sql_statement, values)
            self.log_writer.write_to_log("Flight was deleted")
            return True
        except ValueError:
            self.log_writer.write_to_log("Error with deleting flight")
            return False
