"""
Module: DestinationDao

This module contains the DestinationDao class, which provides methods for interacting with a destination database.
"""

from src.logic.log_writter import Log_writter

class DestinationDao:
    """
    A class representing a data access object for handling destination data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the DestinationDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writer = Log_writter()

    def insert(self, destination):
        """
        Inserts a new destination into the database.

        Parameters:
        - destination: An object representing the destination to be inserted.

        Returns:
        - True if the destination was successfully inserted, False otherwise.
        """
        try:
            if destination is None:
                raise Exception("Invalid destination object")

            sql_statement = "INSERT INTO destination(country, capital, avg_temp) VALUES (?, ?, ?);"
            values = (str(destination.country), str(destination.capital), float(destination.avg_temp))
            self.database.execute(sql_statement, values)
            self.log_writer.write_to_log("Destination inserted successfully.")
            return True
        except Exception as e:
            self.log_writer.write_to_log(f"Error inserting destination into the database: {str(e)}")
            return False

    def read_by_country(self, name):
        """
        Retrieves the ID of a destination by its country name.

        Parameters:
        - name: The name of the country.

        Returns:
        - The ID of the destination if found, None otherwise.
        """
        try:
            if name is None:
                raise ValueError("Invalid destination object")

            sql_statement = "SELECT destination.id FROM destination WHERE country = ?;"
            values = (str(name),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            self.log_writer.write_to_log("Error with reading id")

    def read_all_destinations(self):
        """
        Retrieves all destinations from the database.

        Returns:
        - A list of all destinations in the database.
        """
        try:
            sql_statement = "SELECT * FROM print_all_destinations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            self.log_writer.write_to_log("Error with reading destinations from the database")

    def update(self, name_of_country, avg_temp):
        """
        Updates the average temperature of a destination.

        Parameters:
        - name_of_country: The name of the country whose destination is to be updated.
        - avg_temp: The new average temperature value.

        Returns:
        - None
        """
        try:
            if name_of_country is None or avg_temp is None:
                raise ValueError()
            sql_statement = "UPDATE destination SET avg_temp = ? WHERE country = ?;"
            values = (float(avg_temp), str(name_of_country))
            self.database.execute(sql_statement, values)
            self.log_writer.write_to_log("Destination updated successfully.")
        except ValueError:
            self.log_writer.write_to_log("Error with updating")

    def delete(self, name_of_country):
        """
        Deletes a destination from the database.

        Parameters:
        - name_of_country: The name of the country whose destination is to be deleted.

        Returns:
        - True if the destination was successfully deleted, False otherwise.
        """
        try:
            if name_of_country is None:
                raise ValueError()

            sql_statement = "DELETE FROM destination WHERE country = ?;"
            values = (str(name_of_country),)
            self.database.execute(sql_statement, values)
            self.log_writer.write_to_log("Destination deleted successfully.")
            return True
        except ValueError:
            self.log_writer.write_to_log("Invalid object")
            return False
        except Exception:
            self.log_writer.write_to_log("Error with deleting")
            return False
