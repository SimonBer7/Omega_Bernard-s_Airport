from src.data.models.passenger import Passenger

class PassengerDao:
    """
    The PassengerDao class represents a Data Access Object (DAO) for managing Passenger objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(passenger)
        Inserts a Passenger object into the database.
    read_id(pin)
        Reads the ID of a passenger based on the PIN.
    read(pin)
        Reads all flights associated with a passenger based on the PIN.
    read_to_login(email, pas)
        Reads a passenger for login authentication based on email and password.
    read_all_passengers()
        Reads all passengers from the database.
    update(email_tmp, pas)
        Updates the email of a passenger based on the provided values.
    delete(passenger)
        Deletes a passenger from the database based on the provided Passenger object.
    admin_delete_by_id(id)
        Deletes a passenger from the database based on the passenger ID (admin operation).

    """

    def __init__(self, d):
        """
        Initializes a new PassengerDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, passenger):
        """
        Inserts a Passenger object into the database.

        Parameters
        ----------
        passenger : Passenger
            The Passenger object to be inserted into the database.

        Returns
        -------
        str
            A message indicating the success or failure of the insertion.
        """
        try:
            if passenger is None:
                raise Exception("Invalid passenger object")

            sql_statement = "INSERT INTO passenger(first_name, last_name, email, password, phone_num, pin) values(?, ?, ?, ?, ?, ?);"
            values = (
                str(passenger.get_first_name()), str(passenger.get_last_name()), str(passenger.get_email()),
                str(passenger.get_password()), str(passenger.get_phone_num()), str(passenger.get_pin())
            )
            self.database.execute(sql_statement, values)
            return "Passenger was inserted"
        except Exception as e:
            return f"Error inserting passenger into the database: {str(e)}"

    def read_id(self, pin):
        """
        Reads the ID of a passenger based on the PIN.

        Parameters
        ----------
        pin : str
            The PIN of the passenger.

        Returns
        -------
        int or str
            The ID of the passenger or an error message.
        """
        if pin is None:
            raise ValueError()

        sql_statement = "select passenger.id from passenger where pin = ?"
        values = (str(pin),)
        data = self.database.execute_for_agr(sql_statement, values)
        return data

    def read(self, pin):
        """
        Reads all flights associated with a passenger based on the PIN.

        Parameters
        ----------
        pin : str
            The PIN of the passenger.

        Returns
        -------
        list or str
            A list of flights associated with the passenger or an error message.
        """
        try:
            if pin is None:
                raise ValueError()
            sql_statement = "exec print_user_flights ?"
            values = (str(pin),)
            data = self.database.execute_with_data(sql_statement, values)
            return data
        except ValueError:
            return "Error with reading from database"

    def read_to_login(self, email, pas):
        """
        Reads a passenger for login authentication based on email and password.

        Parameters
        ----------
        email : str
            The email of the passenger.
        pas : str
            The password of the passenger.

        Returns
        -------
        Passenger or str
            The Passenger object or an error message.
        """
        try:
            if email is None or pas is None:
                raise ValueError()

            password = Passenger.hash_password(pas)
            sql_statement = "select name, email, password, phone_num, pin from passenger where email = ? and password = ?;"
            values = (str(email), str(password))
            data = self.database.execute_with_data(sql_statement, values)

            for id in data:
                passenger = Passenger(id[0], id[1], id[2], id[3], id[4], id[5])
            return passenger
        except ValueError:
            return "Error with reading from database"

    def read_all_passengers(self):
        """
        Reads all passengers from the database.

        Returns
        -------
        list
            A list of Passenger objects.
        """
        sql_statement = "select * from print_all_passengers;"
        data = self.database.execute_with_data(sql_statement, None)
        return data

    def update(self, email_tmp, pas):
        """
        Updates the email of a passenger based on the provided values.

        Parameters
        ----------
        email_tmp : str
            The new email value.
        pas : str
            The password of the passenger for authentication.

        Returns
        -------
        str
            A message indicating the success or failure of the update.
        """
        try:
            if pas is None and email_tmp is None:
                raise Exception("Invalid values")
            password = Passenger.hash_password(pas)
            sql_statement = "UPDATE passenger SET email = ? where password = ?;"
            values = (str(email_tmp), str(password))
            self.database.execute(sql_statement, values)
            return "Passenger's email was updated."
        except Exception as e:
            return f"Error updating passenger into the database: {str(e)}"

    def delete(self, passenger):
        """
        Deletes a passenger from the database based on the provided Passenger object.

        Parameters
        ----------
        passenger : Passenger
            The Passenger object to be deleted.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if passenger is None:
                raise ValueError("Invalid passenger object")
            sql_statement = "DELETE FROM passenger WHERE first_name = ? and last_name = ? and email = ? and password = ? and phone_num = ? and pin = ?;"
            values = (
                str(passenger.first_name),
                str(passenger.last_name),
                str(passenger.email),
                str(passenger.password),
                str(passenger.phone_num),
                str(passenger.pin)
            )
            self.database.execute(sql_statement, values)
            return "Passenger was deleted"
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error deleting passenger from the database: {str(e)}"

    def admin_delete_by_id(self, id):
        """
        Deletes a passenger from the database based on the passenger ID (admin operation).

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
            sql_statement = "delete from passenger where id = ?;"
            values = (int(id),)
            self.database.execute(sql_statement, values)
            return "Passenger was deleted"
        except ValueError:
            return "Error with deleting passenger"
