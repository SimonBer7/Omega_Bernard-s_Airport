class Pilot:
    """
    The Pilot class represents information about a pilot, including details such as first name, last name, age, email,
    and phone number.

    ...

    Attributes
    ----------
    first_name : str
        The first name of the pilot.
    last_name : str
        The last name of the pilot.
    age : int
        The age of the pilot.
    email : str
        The email address of the pilot.
    phone_num : str
        The phone number of the pilot.

    Methods
    -------
    get_first_name()
        Returns the first name attribute.
    get_last_name()
        Returns the last name attribute.
    get_age()
        Returns the age attribute.
    get_email()
        Returns the email attribute.
    get_phone_num()
        Returns the phone number attribute.

    """

    def __init__(self, f_name, l_name, age, email, phone_num):
        """
        Initializes a new Pilot object with the provided attributes.

        Parameters
        ----------
        f_name : str
            The first name of the pilot.
        l_name : str
            The last name of the pilot.
        age : int
            The age of the pilot.
        email : str
            The email address of the pilot.
        phone_num : str
            The phone number of the pilot.
        """
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.email = email
        self.phone_num = phone_num

    def get_first_name(self):
        """
        Returns the first name attribute.

        Returns
        -------
        str
            The first name of the pilot.
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns the last name attribute.

        Returns
        -------
        str
            The last name of the pilot.
        """
        return self.last_name

    def get_age(self):
        """
        Returns the age attribute.

        Returns
        -------
        int
            The age of the pilot.
        """
        return self.age

    def get_email(self):
        """
        Returns the email attribute.

        Returns
        -------
        str
            The email address of the pilot.
        """
        return self.email

    def get_phone_num(self):
        """
        Returns the phone number attribute.

        Returns
        -------
        str
            The phone number of the pilot.
        """
        return self.phone_num
