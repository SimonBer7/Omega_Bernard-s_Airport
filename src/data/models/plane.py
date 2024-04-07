class Plane:
    """
    The Plane class represents information about an aircraft, including details such as name, type, capacity, range,
    and active status.

    ...

    Attributes
    ----------
    name : str
        The name of the aircraft.
    type : str
        The type of the aircraft (public or private).
    capacity : int
        The passenger capacity of the aircraft.
    range : int
        The maximum range the aircraft can fly in kilometers.
    active : int
        The status indicating whether the aircraft is active (1) or inactive (0).

    Methods
    -------
    get_name()
        Returns the name attribute.
    get_type()
        Returns the type attribute.
    get_capacity()
        Returns the capacity attribute.
    get_range()
        Returns the range attribute.
    get_active()
        Returns the active attribute.

    """

    def __init__(self, name, type, capacity, range, active):
        """
        Initializes a new Plane object with the provided attributes.

        Parameters
        ----------
        name : str
            The name of the aircraft.
        type : str
            The type of the aircraft (public or private).
        capacity : int
            The passenger capacity of the aircraft.
        range : int
            The maximum range the aircraft can fly in kilometers.
        active : int
            The status indicating whether the aircraft is active (1) or inactive (0).
        """
        self.name = name
        self.type = type
        self.capacity = capacity
        self.range = range
        self.active = active

    def get_name(self):
        """
        Returns the name attribute.

        Returns
        -------
        str
            The name of the aircraft.
        """
        return self.name

    def get_type(self):
        """
        Returns the type attribute.

        Returns
        -------
        str
            The type of the aircraft (public or private).
        """
        return self.type

    def get_capacity(self):
        """
        Returns the capacity attribute.

        Returns
        -------
        int
            The passenger capacity of the aircraft.
        """
        return self.capacity

    def get_range(self):
        """
        Returns the range attribute.

        Returns
        -------
        int
            The maximum range the aircraft can fly in kilometers.
        """
        return self.range

    def get_active(self):
        """
        Returns the active attribute.

        Returns
        -------
        int
            The status indicating whether the aircraft is active (1) or inactive (0).
        """
        return self.active
