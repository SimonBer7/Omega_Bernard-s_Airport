class ReservationDao:
    """
    The ReservationDao class represents a Data Access Object (DAO) for managing Reservation objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(reservation)
        Inserts a Reservation object into the database.
    read()
        Reads all reservations from the database.
    update(pin, new_price)
        Updates the price of a reservation based on the provided values.
    delete(pin)
        Deletes a reservation from the database based on the PIN.
    delete_by_pas_id(id)
        Deletes all reservations associated with a passenger based on the passenger ID.

    """

    def __init__(self, d):
        """
        Initializes a new ReservationDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, res):
        """
        Inserts a Reservation object into the database.

        Parameters
        ----------
        res : Reservation
            The Reservation object to be inserted into the database.

        Returns
        -------
        str
            A message indicating the success or failure of the insertion.
        """
        try:
            if res is None:
                raise ValueError()
            sql_statement = "insert into reservation(pin, passenger_id, flight_id, date, price) values(?, ?, ?, ?, ?);"
            date_str = res.date.strftime('%Y-%m-%d %H:%M:%S')
            values = (int(res.pin), int(res.passenger_id), int(res.flight_id), date_str, int(res.price))
            self.database.execute(sql_statement, values)
            return "Reservation was created :)"
        except ValueError:
            return "Error with creating reservation"

    def read(self):
        """
        Reads all reservations from the database.

        Returns
        -------
        list
            A list of Reservation objects.
        """
        try:
            sql_statement = "select * from print_all_reservations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading destinations from database"

    def update(self, pin, new_price):
        """
        Updates the price of a reservation based on the provided values.

        Parameters
        ----------
        pin : int
            The PIN of the reservation.
        new_price : int
            The new price for the reservation.

        Returns
        -------
        str
            A message indicating the success or failure of the update.
        """
        try:
            if pin is None or new_price is None:
                raise ValueError()

            sql_statement = "update reservation set price = ? where pin = ?"
            values = (int(new_price), int(pin))
            self.database.execute(sql_statement, values)
        except ValueError:
            print("Error with updating price")

    def delete(self, pin):
        """
        Deletes a reservation from the database based on the PIN.

        Parameters
        ----------
        pin : int
            The PIN of the reservation to be deleted.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if pin is None:
                raise ValueError()
            sql_statement = "delete from reservation where pin = ?"
            values = (int(pin),)
            self.database.execute(sql_statement, values)
            return "Reservation was deleted"
        except ValueError:
            return "Error with deleting reservation"

    def delete_by_pas_id(self, id):
        """
        Deletes all reservations associated with a passenger based on the passenger ID.

        Parameters
        ----------
        id : int
            The ID of the passenger.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if id is None:
                raise ValueError()
            sql_statement = "delete from reservation where passenger_id = ?"
            values = (int(id),)
            self.database.execute(sql_statement, values)
            return "Reservation was deleted"
        except ValueError:
            return "Error with deleting reservation"
