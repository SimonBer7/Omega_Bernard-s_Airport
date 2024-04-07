class PilotDao:
    """
    The PilotDao class represents a Data Access Object (DAO) for managing Pilot objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(pilot)
        Inserts a Pilot object into the database.
    read_all_pilots()
        Reads all pilots from the database.
    read_by_name(name)
        Reads the ID of a pilot based on the last name.
    update(old_email, email_tmp, last_name)
        Updates the email of a pilot based on the provided values.
    delete(email)
        Deletes a pilot from the database based on the email.

    """

    def __init__(self, d):
        """
        Initializes a new PilotDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, pilot):
        """
        Inserts a Pilot object into the database.

        Parameters
        ----------
        pilot : Pilot
            The Pilot object to be inserted into the database.

        Returns
        -------
        str
            A message indicating the success or failure of the insertion.
        """
        try:
            if pilot is None:
                raise Exception("Invalid pilot object")

            sql_statement = "insert into pilot(first_name, last_name, age, email, phone_num) values(?, ?, ?, ?, ?);"
            values = (
                str(pilot.first_name), str(pilot.last_name), int(pilot.age), str(pilot.email), str(pilot.phone_num)
            )
            self.database.execute(sql_statement, values)
            return "Pilot was inserted"
        except Exception as e:
            print(f"Error inserting pilot into the database: {str(e)}")

    def read_all_pilots(self):
        """
        Reads all pilots from the database.

        Returns
        -------
        list
            A list of Pilot objects.
        """
        try:
            sql_statement = "select * from print_all_pilots;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading pilots from database"

    def read_by_name(self, name):
        """
        Reads the ID of a pilot based on the last name.

        Parameters
        ----------
        name : str
            The last name of the pilot.

        Returns
        -------
        int or str
            The ID of the pilot or an error message.
        """
        try:
            if name is None:
                raise ValueError("Invalid name object")

            sql_statement = "select pilot.id from pilot where last_name = ?;"
            values = (str(name),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            return "Error with reading id"

    def update(self, old_email, email_tmp, last_name):
        """
        Updates the email of a pilot based on the provided values.

        Parameters
        ----------
        old_email : str
            The old email value for authentication.
        email_tmp : str
            The new email value.
        last_name : str
            The last name of the pilot for authentication.

        Returns
        -------
        str
            A message indicating the success or failure of the update.
        """
        try:
            if last_name is None and email_tmp is None and old_email is None:
                raise ValueError()
            sql_statement = "UPDATE pilot SET email = ? where email = ? and last_name = ?;"
            values = (str(email_tmp), str(old_email), str(last_name))
            self.database.execute(sql_statement, values)
            return "Pilot's email was updated."
        except ValueError:
            return "Error Invalid values"
        except Exception as e:
            return f"Error updating pilot into the database: {str(e)}"

    def delete(self, email):
        """
        Deletes a pilot from the database based on the email.

        Parameters
        ----------
        email : str
            The email of the pilot to be deleted.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if email is None:
                raise ValueError()
            sql_statement = "delete from pilot where email = ?;"
            values = (str(email),)
            self.database.execute(sql_statement, values)
            return "Pilot was deleted."
        except ValueError:
            return "Error with deleting pilot"
