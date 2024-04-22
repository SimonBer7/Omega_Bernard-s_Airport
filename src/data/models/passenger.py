"""
Class: Passenger

This class represents a passenger with attributes such as name, email, password, phone number, and PIN.

Attributes:
- name (str): The name of the passenger.
- email (str): The email address of the passenger.
- password (str): The password of the passenger.
- phone_num (str): The phone number of the passenger.
- pin (str): The PIN of the passenger.

Methods:
- __init__(self, name, email, password, phone_num, pin): Initializes a new Passenger object with the given attributes.
- get_name(self): Returns the name of the passenger.
- get_email(self): Returns the email address of the passenger.
- get_password(self): Returns the password of the passenger.
- get_phone_num(self): Returns the phone number of the passenger.
- get_pin(self): Returns the PIN of the passenger.
- setup(self, name, email, password, phone_num, pin): Sets up the passenger object with the provided information.
- hash_password(cls, password): Class method that hashes the given password using SHA-256 algorithm.
- check_info(cls, email, phone_num, pin): Class method that checks if the provided email, phone number, and PIN are valid.
- to_string(self): Returns a string representation of the passenger object.
"""

import hashlib
import re

class Passenger:
    """
    A class representing a passenger.

    Attributes:
    - name (str): The name of the passenger.
    - email (str): The email address of the passenger.
    - password (str): The password of the passenger.
    - phone_num (str): The phone number of the passenger.
    - pin (str): The PIN of the passenger.
    """

    def __init__(self, name, email, password, phone_num, pin):
        """
        Initializes a new Passenger object with the given attributes.

        Parameters:
        - name (str): The name of the passenger.
        - email (str): The email address of the passenger.
        - password (str): The password of the passenger.
        - phone_num (str): The phone number of the passenger.
        - pin (str): The PIN of the passenger.
        """
        self.name = None
        self.email = None
        self.password = None
        self.phone_num = None
        self.pin = None
        self.setup(name, email, password, phone_num, pin)

    def get_name(self):
        """
        Returns the name of the passenger.

        Returns:
        - str: The name of the passenger.
        """
        return self.name

    def get_email(self):
        """
        Returns the email address of the passenger.

        Returns:
        - str: The email address of the passenger.
        """
        return self.email

    def get_password(self):
        """
        Returns the password of the passenger.

        Returns:
        - str: The password of the passenger.
        """
        return self.password

    def get_phone_num(self):
        """
        Returns the phone number of the passenger.

        Returns:
        - str: The phone number of the passenger.
        """
        return self.phone_num

    def get_pin(self):
        """
        Returns the PIN of the passenger.

        Returns:
        - str: The PIN of the passenger.
        """
        return self.pin

    def setup(self, name, email, password, phone_num, pin):
        """
        Sets up the passenger object with the provided information.

        Parameters:
        - name (str): The name of the passenger.
        - email (str): The email address of the passenger.
        - password (str): The password of the passenger.
        - phone_num (str): The phone number of the passenger.
        - pin (str): The PIN of the passenger.
        """
        if self.check_info(name, email, phone_num, pin):
            self.name = name
            self.email = email
            self.password = password
            self.phone_num = phone_num
            self.pin = pin

    @classmethod
    def hash_password(cls, password):
        """
        Class method that hashes the given password using SHA-256 algorithm.

        Parameters:
        - password (str): The password to be hashed.

        Returns:
        - str: The hashed password.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @classmethod
    def check_info(cls, name, email, phone_num, pin):
        """
        Class method that checks if the provided email, phone number, and PIN are valid.

        Parameters:
        - email (str): The email address to be checked.
        - phone_num (str): The phone number to be checked.
        - pin (str): The PIN to be checked.

        Returns:
        - bool: True if all information is valid, False otherwise.
        """

        name_pattern = re.compile(r'^[a-zA-Z\s.]{3,}$')
        if not name_pattern.match(name):
            return False

        email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(email):
            return False

        phone_pattern = re.compile(r'^\d{9}$')
        if not phone_pattern.match(phone_num):
            return False

        pin_pattern = re.compile(r'^\d{6}/\d{4}$')
        if not pin_pattern.match(pin):
            return False

        return True

    def to_string(self):
        """
        Returns a string representation of the passenger object.

        Returns:
        - str: A string representation of the passenger object.
        """
        return f"Passeger {self.name}, email: {self.email}, " \
            f"password: {self.password}, phone: {self.phone_num}, pin: {self.pin}"
