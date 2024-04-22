"""
Module: PlaneDao

This module contains the PlaneDao class, which provides methods for interacting with a plane database.
"""

from src.logic.log_writter import Log_writter

class PlaneDao:
    """
    A class representing a data access object for handling plane data in a database.

    Attributes:
    - database: A database connection object.
    - log_writer: An instance of Log_writter for logging errors and actions.
    """

    def __init__(self, database):
        """
        Initializes the PlaneDao object.

        Parameters:
        - database: A database connection object.
        """
        self.database = database
        self.log_writter = Log_writter()

    def insert(self, plane):
        """
        Inserts a new plane into the database.

        Parameters:
        - plane: An object representing the plane to be inserted.

        Returns:
        - True if the plane was successfully inserted, False otherwise.
        """
        try:
            if plane is None:
                raise Exception("Invalid plane object")

            sql_statement = "INSERT INTO plane(name, type, capacity, active) VALUES (?, ?, ?, ?);"
            values = (
                str(plane.get_name()), str(plane.get_type()), int(plane.get_capacity()),
                int(plane.get_active())
            )
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Plane was inserted")
            return True
        except Exception as e:
            self.log_writter.write_to_log(f"Error inserting plane into the database: {str(e)}")
            return False

    def read_all_planes(self):
        """
        Retrieves all planes from the database.

        Returns:
        - A list of all planes in the database.
        """
        try:
            sql_statement = "SELECT * FROM print_all_planes;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            self.log_writter.write_to_log("Error with reading from database")

    def read_by_name(self, name):
        """
        Retrieves the ID of a plane by its name.

        Parameters:
        - name: The name of the plane.

        Returns:
        - The ID of the plane if found, None otherwise.
        """
        try:
            if name is None:
                raise ValueError("Invalid name object")

            sql_statement = "SELECT plane.id FROM plane WHERE name = ?;"
            values = (str(name),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            self.log_writter.write_to_log("Error with reading id")

    def update(self, name, active):
        """
        Updates a plane's status.

        Parameters:
        - name: The name of the plane.
        - active: The new status of the plane (1 for active, 0 for inactive).

        Returns:
        - None
        """
        try:
            if name is None and active is None:
                raise ValueError()
            sql_statement = "UPDATE plane SET active = ? WHERE name = ?;"
            values = (int(active), str(name))
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Plane status was updated.")
        except ValueError:
            self.log_writter.write_to_log("Invalid object")
        except Exception:
            self.log_writter.write_to_log("Error with updating")

    def delete(self, name):
        """
        Deletes a plane from the database.

        Parameters:
        - name: The name of the plane.

        Returns:
        - True if the plane was successfully deleted, False otherwise.
        """
        try:
            if name is None:
                raise ValueError()
            sql_statement = "DELETE FROM plane WHERE name = ?;"
            values = (str(name),)
            self.database.execute(sql_statement, values)
            self.log_writter.write_to_log("Plane was deleted.")
            return True
        except ValueError:
            self.log_writter.write_to_log("Invalid object")
            return False
        except Exception:
            self.log_writter.write_to_log("Error with deleting")
            return False
