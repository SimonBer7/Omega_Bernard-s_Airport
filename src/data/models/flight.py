"""
Class: Flight

This class represents a flight with attributes such as flight number, destination ID, plane ID, pilot ID, departure date, arrival date, and price.

Attributes:
- fly_number (str): The flight number.
- destination_id (int): The ID of the destination.
- plane_id (int): The ID of the plane.
- pilot_id (int): The ID of the pilot.
- date_leaving (str): The departure date and time of the flight.
- date_arriving (str): The arrival date and time of the flight.
- price (float): The price of the flight.

Methods:
- __init__(self, fly_num, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price): Initializes a new Flight object with the given attributes.
- get_fly_number(self): Returns the flight number.
- get_destination_id(self): Returns the destination ID.
- get_plane_id(self): Returns the plane ID.
- get_pilot_id(self): Returns the pilot ID.
- get_date_leaving(self): Returns the departure date and time.
- get_date_arriving(self): Returns the arrival date and time.
- get_price(self): Returns the price of the flight.
"""

class Flight:
    """
    A class representing a flight.

    Attributes:
    - fly_number (str): The flight number.
    - destination_id (int): The ID of the destination.
    - plane_id (int): The ID of the plane.
    - pilot_id (int): The ID of the pilot.
    - date_leaving (str): The departure date and time of the flight.
    - date_arriving (str): The arrival date and time of the flight.
    - price (float): The price of the flight.
    """

    def __init__(self, fly_num, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price):
        """
        Initializes a new Flight object with the given attributes.

        Parameters:
        - fly_num (str): The flight number.
        - destination_id (int): The ID of the destination.
        - plane_id (int): The ID of the plane.
        - pilot_id (int): The ID of the pilot.
        - date_leaving (str): The departure date and time of the flight.
        - date_arriving (str): The arrival date and time of the flight.
        - price (float): The price of the flight.
        """
        self.fly_number = fly_num
        self.destination_id = destination_id
        self.plane_id = plane_id
        self.pilot_id = pilot_id
        self.date_leaving = date_leaving
        self.date_arriving = date_arriving
        self.price = price

    def get_fly_number(self):
        """
        Returns the flight number.

        Returns:
        - str: The flight number.
        """
        return self.fly_number

    def get_destination_id(self):
        """
        Returns the ID of the destination.

        Returns:
        - int: The ID of the destination.
        """
        return self.destination_id

    def get_plane_id(self):
        """
        Returns the ID of the plane.

        Returns:
        - int: The ID of the plane.
        """
        return self.plane_id

    def get_pilot_id(self):
        """
        Returns the ID of the pilot.

        Returns:
        - int: The ID of the pilot.
        """
        return self.pilot_id

    def get_date_leaving(self):
        """
        Returns the departure date and time.

        Returns:
        - str: The departure date and time.
        """
        return self.date_leaving

    def get_date_arriving(self):
        """
        Returns the arrival date and time.

        Returns:
        - str: The arrival date and time.
        """
        return self.date_arriving

    def get_price(self):
        """
        Returns the price of the flight.

        Returns:
        - float: The price of the flight.
        """
        return self.price
