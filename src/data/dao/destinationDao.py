class DestinationDao:
    def __init__(self, d):
        self.database = d

    def insert(self, destination):
        try:
            if destination is None:
                raise Exception("Invalid destination object")

            sql_statement = "insert into destination(country, capital, avg_temp) values(?, ?, ?);"
            values = (str(destination.country), str(destination.capital), float(destination.avg_temp))
            self.database.execute(sql_statement, values)
            return "Destination inserted successfully."
        except Exception as e:
            return f"Error inserting destination into the database: {str(e)}"

    def read_by_country(self, name):
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
        try:
            sql_statement = "select * from print_all_destinations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading destinations from the database"

    def update(self, name_of_country, avg_temp):
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
        try:
            if name_of_country is None:
                raise ValueError()

            sql_statement = "DELETE FROM destination WHERE country = ?;"
            values = (str(name_of_country),)
            self.database.execute(sql_statement, values)
            return "Destination deleted successfully."
        except ValueError:
            return "Error with deleting"
