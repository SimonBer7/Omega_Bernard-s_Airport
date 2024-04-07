class FlightDao:
    """
    The FlightDao class represents a Data Access Object (DAO) for managing Flight objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(flight)
        Inserts a Flight object into the database.
    read()
        Reads all flights from the database.
    read_flight_id(fly_num)
        Reads the ID of a flight based on the flight number.
    read_flight_price(fly_num)
        Reads the price of a flight based on the flight number.
    update(fly_num, new_price)
        Updates the price of a flight based on the flight number.
    delete(fly_num)
        Deletes a flight from the database based on the flight number.

    """

    def __init__(self, d):
        """
        Initializes a new FlightDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, flight):
        """
        Inserts a Flight object into the database.

        Parameters
        ----------
        flight : Flight
            The Flight object to be inserted into the database.

        Returns
        -------
        None
            No return value.
        """
        try:
            if flight is None:
                raise Exception("Invalid pilot object")

            sql_statement = "insert into flight(fly_number, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price) values(?, ?, ?, ?, ?, ?, ?);"
            values = (
                int(flight.get_fly_number()), int(flight.get_destination_id()), int(flight.get_plane_id()),
                int(flight.get_pilot_id()), datetime.datetime.strptime(flight.get_date_leaving(), "%Y-%m-%d").date(),
                datetime.datetime.strptime(flight.get_date_arriving(), "%Y-%m-%d").date(), int(flight.get_price())
            )
            self.database.execute(sql_statement, values)
        except Exception as e:
            print(f"Error inserting flight into the database: {str(e)}")

    def read(self):
        """
        Reads all flights from the database.

        Returns
        -------
        list or str
            A list of Flight objects or an error message.
        """
        try:
            sql_statement = "SELECT * FROM print_all_flights;"
            result = self.database.execute_with_data(sql_statement, None)
            if result:
                return result
            else:
                return "No flights available."
        except Exception as e:
            raise f"Error with printing flights from the database: {str(e)}"

    def read_flight_id(self, fly_num):
        """
        Reads the ID of a flight based on the flight number.

        Parameters
        ----------
        fly_num : int
            The flight number.

        Returns
        -------
        int or str
            The ID of the flight or an error message.
        """
        try:
            if fly_num is None:
                raise ValueError()
            sql_statement = "select flight.id from flight where fly_number = ?"
            values = (int(fly_num),)
            flight_id = self.database.execute_for_agr(sql_statement, values)
            if flight_id:
                return flight_id
            else:
                return "There isn't a flight with this number"
        except ValueError:
            print("Error invalid format")
        except Exception:
            print("Error with reading from the database")

    def read_flight_price(self, fly_num):
        """
        Reads the price of a flight based on the flight number.

        Parameters
        ----------
        fly_num : int
            The flight number.

        Returns
        -------
        int or str
            The price of the flight or an error message.
        """
        try:
            if fly_num is None:
                raise ValueError()

            sql_statement = "select flight.price from flight where fly_number = ?;"
            values = (int(fly_num),)
            price = self.database.execute_for_agr(sql_statement, values)
            return price
        except ValueError:
            print("Error with reading price from the database")

    def update(self, fly_num, new_price):
        """
        Updates the price of a flight based on the flight number.

        Parameters
        ----------
        fly_num : int
            The flight number.
        new_price : int
            The new price value.

        Returns
        -------
        None
            No return value.
        """
        try:
            if fly_num is None or new_price is None:
                raise ValueError()

            sql_statement = "update flight set price = ? where fly_number = ?"
            values = (int(new_price), int(fly_num))
            self.database.execute(sql_statement, values)
        except ValueError:
            print("Error with updating price")

    def delete(self, fly_num):
        """
        Deletes a flight from the database based on the flight number.

        Parameters
        ----------
        fly_num : int
            The flight number.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if fly_num is None:
                raise ValueError()

            sql_statement = "delete from flight where fly_number = ?"
            values = (int(fly_num),)
            self.database.execute(sql_statement, values)
            return "Flight was deleted"
        except ValueError:
            return "Error with deleting flight"
