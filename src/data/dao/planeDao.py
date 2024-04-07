class PlaneDao:
    """
    The PlaneDao class represents a Data Access Object (DAO) for managing Plane objects in a database.

    ...

    Attributes
    ----------
    database : Database
        The Database object representing the connection to the underlying database.

    Methods
    -------
    insert(plane)
        Inserts a Plane object into the database.
    read_all_planes()
        Reads all planes from the database.
    read_by_name(name)
        Reads the ID of a plane based on the name.
    update(name, active)
        Updates the active status of a plane based on the provided values.
    delete(name)
        Deletes a plane from the database based on the name.

    """

    def __init__(self, d):
        """
        Initializes a new PlaneDao object with the provided Database object.

        Parameters
        ----------
        d : Database
            The Database object representing the connection to the underlying database.
        """
        self.database = d

    def insert(self, plane):
        """
        Inserts a Plane object into the database.

        Parameters
        ----------
        plane : Plane
            The Plane object to be inserted into the database.

        Returns
        -------
        str
            A message indicating the success or failure of the insertion.
        """
        try:
            if plane is None:
                raise Exception("Invalid plane object")

            sql_statement = "insert into plane(name, type, capacity, range, active) values(?, ?, ?, ?, ?);"
            values = (
                str(plane.get_name()), str(plane.get_type()), int(plane.get_capacity()),
                int(plane.get_range()), int(plane.get_active())
            )
            self.database.execute(sql_statement, values)
            return "Plane was inserted"
        except Exception as e:
            print(f"Error inserting plane into the database: {str(e)}")

    def read_all_planes(self):
        """
        Reads all planes from the database.

        Returns
        -------
        list
            A list of Plane objects.
        """
        try:
            sql_statement = "select * from print_all_planes;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading from database"

    def read_by_name(self, name):
        """
        Reads the ID of a plane based on the name.

        Parameters
        ----------
        name : str
            The name of the plane.

        Returns
        -------
        int or str
            The ID of the plane or an error message.
        """
        try:
            if name is None:
                raise ValueError("Invalid name object")

            sql_statement = "select plane.id from plane where name = ?;"
            values = (str(name),)
            data = self.database.execute_for_agr(sql_statement, values)
            return data
        except ValueError:
            return "Error with reading id"

    def update(self, name, active):
        """
        Updates the active status of a plane based on the provided values.

        Parameters
        ----------
        name : str
            The name of the plane.
        active : int
            The new active status (1 for active, 0 for inactive).

        Returns
        -------
        str
            A message indicating the success or failure of the update.
        """
        try:
            if name is None and active is None:
                raise ValueError()
            sql_statement = "update plane set active = ? where name = ?;"
            values = (int(active), str(name))
            self.database.execute(sql_statement, values)
            return "Plane status was updated."
        except ValueError:
            return "Invalid object"
        except Exception:
            return "Error with updating"

    def delete(self, name):
        """
        Deletes a plane from the database based on the name.

        Parameters
        ----------
        name : str
            The name of the plane to be deleted.

        Returns
        -------
        str
            A message indicating the success or failure of the deletion.
        """
        try:
            if name is None:
                raise ValueError()
            sql_statement = "delete from plane where name = ?;"
            values = (str(name),)
            self.database.execute(sql_statement, values)
            return "Plane was deleted."
        except ValueError:
            return "Invalid object"
        except Exception:
            return "Error with deleting"
