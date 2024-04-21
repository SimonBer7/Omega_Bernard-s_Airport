"""
Class: Pilot

This class represents a pilot with attributes such as name, age, email, and phone number.

Attributes:
- name (str): The name of the pilot.
- age (int): The age of the pilot.
- email (str): The email address of the pilot.
- phone_num (str): The phone number of the pilot.

Methods:
- __init__(self, name, age, email, phone_num): Initializes a new Pilot object with the given attributes.
- get_name(self): Returns the name of the pilot.
- get_age(self): Returns the age of the pilot.
- get_email(self): Returns the email address of the pilot.
- get_phone_num(self): Returns the phone number of the pilot.
"""

class Pilot:
    """
    A class representing a pilot.

    Attributes:
    - name (str): The name of the pilot.
    - age (int): The age of the pilot.
    - email (str): The email address of the pilot.
    - phone_num (str): The phone number of the pilot.
    """

    def __init__(self, name, age, email, phone_num):
        """
        Initializes a new Pilot object with the given attributes.

        Parameters:
        - name (str): The name of the pilot.
        - age (int): The age of the pilot.
        - email (str): The email address of the pilot.
        - phone_num (str): The phone number of the pilot.
        """
        self.name = name
        self.age = age
        self.email = email
        self.phone_num = phone_num

    def get_name(self):
        """
        Returns the name of the pilot.

        Returns:
        - str: The name of the pilot.
        """
        return self.name

    def get_age(self):
        """
        Returns the age of the pilot.

        Returns:
        - int: The age of the pilot.
        """
        return self.age

    def get_email(self):
        """
        Returns the email address of the pilot.

        Returns:
        - str: The email address of the pilot.
        """
        return self.email

    def get_phone_num(self):
        """
        Returns the phone number of the pilot.

        Returns:
        - str: The phone number of the pilot.
        """
        return self.phone_num
