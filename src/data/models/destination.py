class Destination:
    """
    The Destination class represents information about a specific travel destination, encapsulating key attributes such as country,
    capital, language, and average temperature.

    ...

    Attributes
    ----------
    country : str
        The name of the country associated with the destination.
    capital : str
        The capital city of the destination country.
    language : str
        The predominant language spoken in the destination country.
    avg_temp : float
        The average temperature of the destination.

    Methods
    -------
    get_country()
        Returns the country attribute.
    get_capital()
        Returns the capital attribute.
    get_language()
        Returns the language attribute.
    get_avg_temp()
        Returns the average temperature attribute.
    """

    def __init__(self, country, capital, language, avg_temp):
        """
        Initializes a new Destination object with the provided attributes.

        Parameters
        ----------
        country : str
            The name of the country.
        capital : str
            The capital city.
        language : str
            The predominant language.
        avg_temp : float
            The average temperature.

        """
        self.country = country
        self.capital = capital
        self.language = language
        self.avg_temp = avg_temp

    def get_country(self):
        """
        Returns the country attribute.

        Returns
        -------
        str
            The name of the country.

        """
        return self.country

    def get_capital(self):
        """
        Returns the capital attribute.

        Returns
        -------
        str
            The capital city.

        """
        return self.capital

    def get_language(self):
        """
        Returns the language attribute.

        Returns
        -------
        str
            The predominant language.

        """
        return self.language

    def get_avg_temp(self):
        """
        Returns the average temperature attribute.

        Returns
        -------
        float
            The average temperature.

        """
        return self.avg_temp
