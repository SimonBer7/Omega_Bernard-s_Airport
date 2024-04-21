"""
Class: Database_checker

This class is responsible for checking the existence of essential database tables and ensuring they contain data. It interacts with various data access objects (DAOs) to perform these checks and load data into the tables if necessary.

Attributes:
- app (Application): An instance of the Application class representing the main application logic.
- log_writer (Log_writer): An instance of the Log_writer class for logging activities.
- flight_loader (File_loader): An instance of the File_loader class for loading flight data from files.
- plane_dao (PlaneDao): An instance of the PlaneDao class for plane-related database operations.
- pilot_dao (PilotDao): An instance of the PilotDao class for pilot-related database operations.
- destination_dao (DestinationDao): An instance of the DestinationDao class for destination-related database operations.
- flight_dao (FlightDao): An instance of the FlightDao class for flight-related database operations.

Methods:
- check_tables(self): Checks the existence of essential database tables and ensures they contain data.
- show_flights(self): Retrieves and returns flight data from the database.
"""

from src.data.dao.planeDao import PlaneDao
from src.data.dao.pilotDao import PilotDao
from src.data.dao.destinationDao import DestinationDao
from src.data.dao.flightDao import FlightDao
from src.logic.file_loader import File_loader
from src.logic.log_writter import Log_writter


class Database_checker:
    """
    Class responsible for checking the existence of essential database tables and ensuring they contain data.
    """

    def __init__(self, app, database):
        """
        Initializes a new Database_checker object.

        Parameters:
        - app (Application): An instance of the Application class representing the main application logic.
        - database (Database): An instance of the Database class for database interactions.
        """
        self.app = app
        self.log_writer = Log_writter()
        self.flight_loader = File_loader(app, database)
        self.plane_dao = PlaneDao(database)
        self.pilot_dao = PilotDao(database)
        self.destination_dao = DestinationDao(database)
        self.flight_dao = FlightDao(database)

    def check_tables(self):
        """
        Checks the existence of essential database tables and ensures they contain data.
        If the tables are empty, loads data into them from external files.
        """
        select_plane = "select count(*) from plane;"
        select_pilot = "select count(*) from pilot;"
        select_destination = "select count(*) from destination;"
        select_flight = "select count(*) from flight;"
        try:
            if (int(self.plane_dao.database.execute_for_agr(select_plane, None)) > 0) and (
                    int(self.pilot_dao.database.execute_for_agr(select_pilot, None)) > 0) and (
                    int(self.destination_dao.database.execute_for_agr(select_destination, None)) > 0) and (
                    int(self.flight_dao.database.execute_for_agr(select_flight, None)) > 0):
                return
            else:
                return self.flight_loader.loader()
        except Exception as e:
            self.log_writer.write_to_log(f"Error reading data from files: {str(e)}")

    def show_flights(self):
        """
        Retrieves flight data from the database.

        Returns:
        - list: A list containing flight data.
        """
        return self.flight_dao.read()
