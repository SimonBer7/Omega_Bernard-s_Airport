"""
Module: PilotDao

This module contains the PilotDao class, which provides methods for interacting with a pilot database.
"""

from src.logic.log_writter import Log_writter

class PilotDao:
    """
    A class representing a data access object for handling pilot data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the PilotDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writter = Log_writter()

    def insert(self, pilot):
        """
        Inserts a new pilot into the database.

        Parameters:
        - pilot: An object representing the pilot to be inserted.

        Returns:
        - True if the pilot was successfully inserted, False otherwise.
        """
        try:
            if pilot is None:
                raise Exception("Invalid pilot object")

            sql_statement = "INSERT INTO pilot(name, age, email, phone_num) VALUES (?, ?, ?, ?);"
            values = (
                str(pilot.name), int(pilot.age), str(pilot.email), str(pilot.phone_num)
            )
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Pilot was inserted")
            return True
        except Exception as e:
            self.log_writter.write_to_log(f"Error inserting pilot into the database: {str(e)}")
            return False

    def read_all_pilots(self):
        """
        Retrieves all pilots from the database.

        Returns:
        - A list of all pilots in the database.
        """
        try:
            sql_statement = "SELECT * FROM print_all_pilots;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            self.log_writter.write_to_log("Error with reading pilots from database")

    def read_by_email(self, email):
        """
        Retrieves the ID of a pilot by their email address.

        Parameters:
        - email: The email address of the pilot.

        Returns:
        - The ID of the pilot if found, None otherwise.
        """
        try:
            if email is None:
                raise ValueError("Invalid name object")

            sql_statement = "SELECT pilot.id FROM pilot WHERE email = ?;"
            values = (str(email),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            self.log_writter.write_to_log("Error with reading id")

    def update(self, old_email, new_email, name):
        """
        Updates a pilot's email address.

        Parameters:
        - old_email: The old email address of the pilot.
        - new_email: The new email address of the pilot.
        - name: The name of the pilot.

        Returns:
        - None
        """
        try:
            if name is None and new_email is None and old_email is None:
                raise ValueError()
            sql_statement = "UPDATE pilot SET email = ? WHERE email = ? AND name = ?;"
            values = (str(new_email), str(old_email), str(name))
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Pilot's email was updated.")
        except ValueError:
            self.log_writter.write_to_log("Error Invalid values")
        except Exception as e:
            self.log_writter.write_to_log(f"Error updating pilot into the database: {str(e)}")

    def delete(self, email):
        """
        Deletes a pilot from the database.

        Parameters:
        - email: The email address of the pilot.

        Returns:
        - True if the pilot was successfully deleted, False otherwise.
        """
        try:
            if email is None:
                raise ValueError()
            sql_statement = "DELETE FROM pilot WHERE email = ?;"
            values = (str(email),)
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Pilot was deleted.")
            return True
        except ValueError:
            self.log_writter.write_to_log("Error with deleting pilot")
            return False
