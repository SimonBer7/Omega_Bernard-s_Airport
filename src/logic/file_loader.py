"""
Class: File_loader

This class is responsible for loading data from CSV files into the database.

Attributes:
- paths (list): List of file paths for the CSV files containing data to be loaded.
- passenger_dao (PassengerDao): Data Access Object for managing passenger data in the database.
- plane_dao (PlaneDao): Data Access Object for managing plane data in the database.
- pilot_dao (PilotDao): Data Access Object for managing pilot data in the database.
- destination_dao (DestinationDao): Data Access Object for managing destination data in the database.
- flight_dao (FlightDao): Data Access Object for managing flight data in the database.
- app: Application instance.
- log_writter (Log_writter): Log writer instance.

Methods:
- loader(self): Loads data from CSV files into the database.
"""

import csv
from src.data.models.passenger import Passenger
from src.data.models.pilot import Pilot
from src.data.models.plane import Plane
from src.data.models.destination import Destination
from src.data.models.flight import Flight
from src.logic.log_writter import Log_writter
from src.data.dao.passengerDao import PassengerDao
from src.data.dao.planeDao import PlaneDao
from src.data.dao.pilotDao import PilotDao
from src.data.dao.destinationDao import DestinationDao
from src.data.dao.flightDao import FlightDao

class File_loader:
    """
    Class responsible for loading data from CSV files into the database.
    """

    def __init__(self, app, database):
        """
        Initializes a new File_loader object.

        Parameters:
        - app: Application instance.
        - database: Database connection.
        """
        self.paths = ["./data/import/pilots.csv", "./data/import/planes.csv", "./data/import/destinations.csv", "./data/import/flights.csv"]
        self.passenger_dao = PassengerDao(database)
        self.plane_dao = PlaneDao(database)
        self.pilot_dao = PilotDao(database)
        self.destination_dao = DestinationDao(database)
        self.flight_dao = FlightDao(database)
        self.app = app
        self.log_writter = Log_writter()

    def loader(self):
        """
        Loads data from CSV files into the database.
        """
        try:
            for path in self.paths:
                with open(path, "r") as file:
                    csv_reader = csv.reader(file, delimiter=",")
                    if path == self.paths[0]:
                        for row in csv_reader:
                            pilot = Pilot(*row)
                            self.pilot_dao.insert(pilot)
                    elif path == self.paths[1]:
                        for row in csv_reader:
                            plane = Plane(*row)
                            self.plane_dao.insert(plane)
                    elif path == self.paths[2]:
                        for row in csv_reader:
                            destination = Destination(*row)
                            self.destination_dao.insert(destination)
                    elif path == self.paths[3]:
                        for row in csv_reader:
                            flight = Flight(*row)
                            self.flight_dao.insert(flight)

            self.passenger_dao.insert(
                Passenger("Admin", "admin@gmail.com", "admin", "111111111", "111111/1111"))
            self.app.admin = Passenger("Admin", "admin@gmail.com", "admin", "111111111", "111111/1111")
            return True
        except Exception as e:
            self.log_writter.write_to_log(f"Error, while loading data {e}")
            return False
