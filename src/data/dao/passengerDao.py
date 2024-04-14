from src.data.models.passenger import Passenger
import re

class PassengerDao:
    def __init__(self, d):
        self.database = d

    def insert(self, passenger):
        try:
            if passenger is None:
                raise Exception("Invalid passenger object")

            sql_statement = "INSERT INTO passenger(name, email, password, phone_num, pin) values(?, ?, ?, ?, ?);"
            values = (
                str(passenger.get_name()), str(passenger.get_email()),
                str(passenger.get_password()), str(passenger.get_phone_num()), str(passenger.get_pin())
            )
            self.database.execute(sql_statement, values)
            return True
        except Exception as e:
            print(f"Error inserting passenger into the database: {str(e)}")
            return False

    def read_id(self, pin):
        if pin is None:
            raise ValueError()

        sql_statement = "select passenger.id from passenger where pin = ?"
        values = (str(pin),)
        data = self.database.execute_for_agr(sql_statement, values)
        return data

    def read(self, pin):
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
        try:
            if email is None or pas is None:
                raise ValueError("Email and password are required for login")

            password = Passenger.hash_password(pas)
            sql_statement = "SELECT name, email, password, phone_num, pin FROM passenger WHERE email = ? AND password = ?;"
            values = (str(email), str(password))
            data = self.database.execute_with_data(sql_statement, values)

            if data:
                id = data[0]
                passenger = Passenger(id[0], id[1], id[2], id[3], id[4])
                return passenger
            else:
                return None
        except Exception as e:
            print(f"Error with reading from database: {e}")
            return None

    def read_all_passengers(self):
        sql_statement = "select * from print_all_passengers;"
        data = self.database.execute_with_data(sql_statement, None)
        return data

    def update(self, new_email, old_email, pas):
        try:
            if pas is None and new_email is None and old_email is None:
                raise Exception("Invalid values")

            if self.is_valid_email(new_email):
                password = Passenger.hash_password(pas)
                sql_statement = "UPDATE passenger SET email = ? where email = ? and password = ?;"
                values = (str(new_email), str(old_email), str(password))
                self.database.execute(sql_statement, values)
                return "Passenger's email was updated."
        except Exception as e:
            return f"Error updating passenger into the database: {str(e)}"

    def delete(self, passenger):
        try:
            if passenger is None:
                raise ValueError("Invalid passenger object")
            sql_statement = "DELETE FROM passenger WHERE name = ? and email = ? and password = ? and phone_num = ? and pin = ?;"
            values = (
                str(passenger.name),
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
        try:
            if id is None:
                raise ValueError()
            sql_statement = "delete from passenger where id = ?;"
            values = (int(id),)
            self.database.execute(sql_statement, values)
            return "Passenger was deleted"
        except ValueError:
            return "Error with deleting passenger"

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return True
        else:
            return False
