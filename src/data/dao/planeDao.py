class PlaneDao:
    def __init__(self, d):
        self.database = d

    def insert(self, plane):
        try:
            if plane is None:
                raise Exception("Invalid plane object")

            sql_statement = "insert into plane(name, type, capacity, active) values(?, ?, ?, ?);"
            values = (
                str(plane.get_name()), str(plane.get_type()), int(plane.get_capacity()),
                int(plane.get_active())
            )
            self.database.execute(sql_statement, values)
            return "Plane was inserted"
        except Exception as e:
            print(f"Error inserting plane into the database: {str(e)}")

    def read_all_planes(self):
        try:
            sql_statement = "select * from print_all_planes;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading from database"

    def read_by_name(self, name):
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
