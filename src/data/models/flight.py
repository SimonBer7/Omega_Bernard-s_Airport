class Flight:
    """
    The Flight class represents information about a specific flight, including flight number, destination, plane, pilot,
    departure and arrival dates, and the price of the flight.

    ...

    Attributes
    ----------
    fly_number : int
        The unique identifier for the flight.
    destination_id : int
        The identifier for the destination associated with the flight.
    plane_id : int
        The identifier for the plane assigned to the flight.
    pilot_id : int
        The identifier for the pilot assigned to the flight.
    date_leaving : str
        The date and time when the flight is scheduled to depart.
    date_arriving : str
        The date and time when the flight is scheduled to arrive.
    price : int
        The price of the flight.

    Methods
    -------
    get_fly_number()
        Returns the flight number attribute.
    get_destination_id()
        Returns the destination ID attribute.
    get_plane_id()
        Returns the plane ID attribute.
    get_pilot_id()
        Returns the pilot ID attribute.
    get_date_leaving()
        Returns the departure date attribute.
    get_date_arriving()
        Returns the arrival date attribute.
    get_price()
        Returns the price attribute.
    """

    def __init__(self, fly_num, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price):
        """
        Initializes a new Flight object with the provided attributes.

        Parameters
        ----------
        fly_num : int
            The unique identifier for the flight.
        destination_id : int
            The identifier for the destination associated with the flight.
        plane_id : int
            The identifier for the plane assigned to the flight.
        pilot_id : int
            The identifier for the pilot assigned to the flight.
        date_leaving : str
            The date and time when the flight is scheduled to depart.
        date_arriving : str
            The date and time when the flight is scheduled to arrive.
        price : int
            The price of the flight.
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
        Returns the flight number attribute.

        Returns
        -------
        int
            The flight number.

        """
        return self.fly_number

    def get_destination_id(self):
        """
        Returns the destination ID attribute.

        Returns
        -------
        int
            The destination ID.

        """
        return self.destination_id

    def get_plane_id(self):
        """
        Returns the plane ID attribute.

        Returns
        -------
        int
            The plane ID.

        """
        return self.plane_id

    def get_pilot_id(self):
        """
        Returns the pilot ID attribute.

        Returns
        -------
        int
            The pilot ID.

        """
        return self.pilot_id

    def get_date_leaving(self):
        """
        Returns the departure date attribute.

        Returns
        -------
        str
            The date and time when the flight is scheduled to depart.

        """
        return self.date_leaving

    def get_date_arriving(self):
        """
        Returns the arrival date attribute.

        Returns
        -------
        str
            The date and time when the flight is scheduled to arrive.

        """
        return self.date_arriving

    def get_price(self):
        """
        Returns the price attribute.

        Returns
        -------
        int
            The price of the flight.

        """
        return self.price
