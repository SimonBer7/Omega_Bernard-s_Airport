class Reservation:
    """
    The Reservation class represents a reservation made by a passenger for a specific flight, including details such as
    personal identification number (PIN), passenger ID, flight ID, reservation date, and price.

    ...

    Attributes
    ----------
    pin : int
        The personal identification number (PIN) associated with the reservation.
    passenger_id : int
        The unique identifier for the passenger making the reservation.
    flight_id : int
        The unique identifier for the flight being reserved.
    date : datetime
        The date and time when the reservation was made.
    price : int
        The price associated with the reservation.

    Methods
    -------
    get_pin()
        Returns the PIN attribute.
    get_passenger_id()
        Returns the passenger ID attribute.
    get_flight_id()
        Returns the flight ID attribute.
    get_date()
        Returns the reservation date attribute.
    get_price()
        Returns the price attribute.

    """

    def __init__(self, pin, pass_id, flight_id, date, price):
        """
        Initializes a new Reservation object with the provided attributes.

        Parameters
        ----------
        pin : int
            The personal identification number (PIN) associated with the reservation.
        pass_id : int
            The unique identifier for the passenger making the reservation.
        flight_id : int
            The unique identifier for the flight being reserved.
        date : datetime
            The date and time when the reservation was made.
        price : int
            The price associated with the reservation.
        """
        self.pin = pin
        self.passenger_id = pass_id
        self.flight_id = flight_id
        self.date = date
        self.price = price

    def get_pin(self):
        """
        Returns the PIN attribute.

        Returns
        -------
        int
            The personal identification number (PIN) associated with the reservation.
        """
        return self.pin

    def get_passenger_id(self):
        """
        Returns the passenger ID attribute.

        Returns
        -------
        int
            The unique identifier for the passenger making the reservation.
        """
        return self.passenger_id

    def get_flight_id(self):
        """
        Returns the flight ID attribute.

        Returns
        -------
        int
            The unique identifier for the flight being reserved.
        """
        return self.flight_id

    def get_date(self):
        """
        Returns the reservation date attribute.

        Returns
        -------
        datetime
            The date and time when the reservation was made.
        """
        return self.date

    def get_price(self):
        """
        Returns the price attribute.

        Returns
        -------
        int
            The price associated with the reservation.
        """
        return self.price
