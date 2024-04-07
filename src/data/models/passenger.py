import hashlib

class Passenger:
    """
    The Passenger class represents information about an individual passenger, including personal details such as
    first name, last name, email, hashed password, phone number, and personal identification number (PIN).

    ...

    Attributes
    ----------
    first_name : str
        The first name of the passenger.
    last_name : str
        The last name of the passenger.
    email : str
        The email address of the passenger.
    password : str
        The hashed password of the passenger.
    phone_num : str
        The phone number of the passenger.
    pin : str
        The personal identification number (PIN) of the passenger.

    Methods
    -------
    get_first_name()
        Returns the first name attribute.
    get_last_name()
        Returns the last name attribute.
    get_email()
        Returns the email attribute.
    get_password()
        Returns the hashed password attribute.
    get_phone_num()
        Returns the phone number attribute.
    get_pin()
        Returns the PIN attribute.
    hash_password(cls, password)
        Class method that hashes the provided password using SHA-256 algorithm and returns the hashed result.
    to_string()
        Returns a string representation of the passenger.

    """

    def __init__(self, f_name, l_name, email, password, phone_num, pin):
        """
        Initializes a new Passenger object with the provided attributes.

        Parameters
        ----------
        f_name : str
            The first name of the passenger.
        l_name : str
            The last name of the passenger.
        email : str
            The email address of the passenger.
        password : str
            The hashed password of the passenger.
        phone_num : str
            The phone number of the passenger.
        pin : str
            The personal identification number (PIN) of the passenger.
        """
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.password = password
        self.phone_num = phone_num
        self.pin = pin

    def get_first_name(self):
        """
        Returns the first name attribute.

        Returns
        -------
        str
            The first name of the passenger.
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns the last name attribute.

        Returns
        -------
        str
            The last name of the passenger.
        """
        return self.last_name

    def get_email(self):
        """
        Returns the email attribute.

        Returns
        -------
        str
            The email address of the passenger.
        """
        return self.email

    def get_password(self):
        """
        Returns the hashed password attribute.

        Returns
        -------
        str
            The hashed password of the passenger.
        """
        return self.password

    def get_phone_num(self):
        """
        Returns the phone number attribute.

        Returns
        -------
        str
            The phone number of the passenger.
        """
        return self.phone_num

    def get_pin(self):
        """
        Returns the PIN attribute.

        Returns
        -------
        str
            The personal identification number (PIN) of the passenger.
        """
        return self.pin

    @classmethod
    def hash_password(cls, password):
        """
        Class method that hashes the provided password using SHA-256 algorithm and returns the hashed result.

        Parameters
        ----------
        password : str
            The password to be hashed.

        Returns
        -------
        str
            The hashed password.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def to_string(self):
        """
        Returns a string representation of the passenger.

        Returns
        -------
        str
            A string representation of the passenger.
        """
        return f"Passeger {self.first_name} {self.last_name}, email: {self.email}, " \
               f"password: {self.password}, phone: {self.phone_num}, pin: {self.pin}"
