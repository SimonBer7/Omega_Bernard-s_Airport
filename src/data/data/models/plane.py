"""
Class: Plane

This class represents a plane with attributes such as name, type, capacity, and active status.

Attributes:
- name (str): The name of the plane.
- type (str): The type of the plane.
- capacity (int): The capacity of the plane.
- active (bool): The status of the plane (active/inactive).

Methods:
- __init__(self, name, type, capacity, active): Initializes a new Plane object with the given attributes.
- get_name(self): Returns the name of the plane.
- get_type(self): Returns the type of the plane.
- get_capacity(self): Returns the capacity of the plane.
- get_active(self): Returns the active status of the plane.
"""

class Plane:
    """
    A class representing a plane.

    Attributes:
    - name (str): The name of the plane.
    - type (str): The type of the plane.
    - capacity (int): The capacity of the plane.
    - active (bool): The status of the plane (active/inactive).
    """

    def __init__(self, name, type, capacity, active):
        """
        Initializes a new Plane object with the given attributes.

        Parameters:
        - name (str): The name of the plane.
        - type (str): The type of the plane.
        - capacity (int): The capacity of the plane.
        - active (bool): The status of the plane (active/inactive).
        """
        self.name = name
        self.type = type
        self.capacity = capacity
        self.active = active

    def get_name(self):
        """
        Returns the name of the plane.

        Returns:
        - str: The name of the plane.
        """
        return self.name

    def get_type(self):
        """
        Returns the type of the plane.

        Returns:
        - str: The type of the plane.
        """
        return self.type

    def get_capacity(self):
        """
        Returns the capacity of the plane.

        Returns:
        - int: The capacity of the plane.
        """
        return self.capacity

    def get_active(self):
        """
        Returns the active status of the plane.

        Returns:
        - bool: The active status of the plane.
        """
        return self.active
