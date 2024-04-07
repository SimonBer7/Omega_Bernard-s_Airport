class DestinationDao:
    """
    The DestinationDao class represents a Data Access Object (DAO) for managing Destination objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(destination)
        Inserts a Destination object into the database.
    read_by_country(name)
        Reads the ID of a destination based on the country name.
    read_all_destinations()
        Reads all destinations from the database.
    update(name_of_country, avg_temp)
        Updates the average temperature of a destination based on the country name.
    delete(name_of_country)
        Deletes a destination from the database based on the country name.

    """

    def __init__(self, d):
        """
        Initializes a new DestinationDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, destination):
        """
        Inserts a Destination object into the database.

        Parameters
        ----------
        destination : Destination
            The Destination object to be inserted into the database.

        Returns
        -------
        str
            A message indicating the success or failure of the insertion.
        """
        try:
            if destination is None:
                raise Exception("Invalid destination object")

            sql_statement = "insert into destination(country, capital, language, avg_temp) values(?, ?, ?, ?);"
            values = (str(destination.country), str(destination.capital), str(destination.language), float(destination.avg_temp))
            self.database.execute(sql_statement, values)
            return "Destination inserted successfully."
        except Exception as e:
            return f"Error inserting destination into the database: {str(e)}"

    def read_by_country(self, name):
        """
        Reads the ID of a destination based on the country name.

        Parameters
        ----------
        name : str
            The name of the country.

        Returns
        -------
        int or str
            The ID of the destination or an error message.
        """
        try:
            if name is None:
                raise ValueError("Invalid destination object")

            sql_statement = "select destination.id from destination where country = ?;"
            values = (str(name),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            return "Error with reading id"

    def read_all_destinations(self):
        """
        Reads all destinations from the database.

        Returns
        -------
        list or str
            A list of Destination objects or an error message.
        """
        try:
            sql_statement = "select * from print_all_destinations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading destinations from the database"

    def update(self, name_of_country, avg_temp):
        """
        Updates the average temperature of a destination based on the country name.

        Parameters
        ----------
        name_of_country : str
            The name of the country.
        avg_temp : float
            The new average temperature value.

        Returns
        -------
        str
            A message indicating the success or failure of the update.
        """
        try:
            if name_of_country is None or avg_temp is None:
                raise ValueError()
            sql_statement = "UPDATE destination SET avg_temp = ? where country = ?;"
            values = (float(avg_temp), str(name_of_country))
            self.database.execute(sql_statement, values)
            return "Destination updated successfully."
        except ValueError:
            return "Error with updating"

    def delete(self, name_of_country):
        """
        Deletes a destination from the database based on the country name.

        Parameters
        ----------
        name_of_country : str
            The name of the country.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if name_of_country is None:
                raise ValueError()

            sql_statement = "DELETE FROM destination WHERE country = ?;"
            values = (str(name_of_country),)
            self.database.execute(sql_statement, values)
            return "Destination deleted successfully."
        except ValueError:
            return "Error with deleting"
