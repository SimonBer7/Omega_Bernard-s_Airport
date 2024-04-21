"""
Class: Destination

This class represents a destination with attributes such as country, capital, and average temperature.

Attributes:
- country (str): The name of the country.
- capital (str): The name of the capital city.
- avg_temp (float): The average temperature of the destination.

Methods:
- __init__(self, country, capital, avg_temp): Initializes a new Destination object with the given attributes.
- get_country(self): Returns the name of the country.
- get_capital(self): Returns the name of the capital city.
- get_avg_temp(self): Returns the average temperature of the destination.
"""

class Destination:
    """
    A class representing a destination.

    Attributes:
    - country (str): The name of the country.
    - capital (str): The name of the capital city.
    - avg_temp (float): The average temperature of the destination.
    """

    def __init__(self, country, capital, avg_temp):
        """
        Initializes a new Destination object with the given attributes.

        Parameters:
        - country (str): The name of the country.
        - capital (str): The name of the capital city.
        - avg_temp (float): The average temperature of the destination.
        """
        self.country = country
        self.capital = capital
        self.avg_temp = avg_temp

    def get_country(self):
        """
        Returns the name of the country.

        Returns:
        - str: The name of the country.
        """
        return self.country

    def get_capital(self):
        """
        Returns the name of the capital city.

        Returns:
        - str: The name of the capital city.
        """
        return self.capital

    def get_avg_temp(self):
        """
        Returns the average temperature of the destination.

        Returns:
        - float: The average temperature of the destination.
        """
        return self.avg_temp
