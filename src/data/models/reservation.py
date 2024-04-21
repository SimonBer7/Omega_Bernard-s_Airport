"""
Class: Reservation

This class represents a flight reservation with attributes such as PIN, passenger ID, flight ID, date, and price.

Attributes:
- pin (str): The unique PIN associated with the reservation.
- passenger_id (int): The ID of the passenger making the reservation.
- flight_id (int): The ID of the flight being reserved.
- date (datetime): The date and time of the reservation.
- price (float): The price of the reservation.

Methods:
- __init__(self, pin, pass_id, flight_id, date, price): Initializes a new Reservation object with the given attributes.
- get_pin(self): Returns the PIN of the reservation.
- get_passenger_id(self): Returns the ID of the passenger associated with the reservation.
- get_flight_id(self): Returns the ID of the flight being reserved.
- get_date(self): Returns the date and time of the reservation.
- get_price(self): Returns the price of the reservation.
"""

class Reservation:
    """
    A class representing a flight reservation.

    Attributes:
    - pin (str): The unique PIN associated with the reservation.
    - passenger_id (int): The ID of the passenger making the reservation.
    - flight_id (int): The ID of the flight being reserved.
    - date (datetime): The date and time of the reservation.
    - price (float): The price of the reservation.
    """

    def __init__(self, pin, pass_id, flight_id, date, price):
        """
        Initializes a new Reservation object with the given attributes.

        Parameters:
        - pin (str): The unique PIN associated with the reservation.
        - pass_id (int): The ID of the passenger making the reservation.
        - flight_id (int): The ID of the flight being reserved.
        - date (datetime): The date and time of the reservation.
        - price (float): The price of the reservation.
        """
        self.pin = pin
        self.passenger_id = pass_id
        self.flight_id = flight_id
        self.date = date
        self.price = price

    def get_pin(self):
        """
        Returns the PIN of the reservation.

        Returns:
        - str: The PIN of the reservation.
        """
        return self.pin

    def get_passenger_id(self):
        """
        Returns the ID of the passenger associated with the reservation.

        Returns:
        - int: The ID of the passenger.
        """
        return self.passenger_id

    def get_flight_id(self):
        """
        Returns the ID of the flight being reserved.

        Returns:
        - int: The ID of the flight.
        """
        return self.flight_id

    def get_date(self):
        """
        Returns the date and time of the reservation.

        Returns:
        - datetime: The date and time of the reservation.
        """
        return self.date

    def get_price(self):
        """
        Returns the price of the reservation.

        Returns:
        - float: The price of the reservation.
        """
        return self.price
