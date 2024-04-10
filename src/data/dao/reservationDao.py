class ReservationDao:
    def __init__(self, d):
        self.database = d

    def insert(self, res):
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
        try:
            sql_statement = "select * from print_all_reservations;"
            data = self.database.execute_with_data(sql_statement, None)
            return data
        except Exception:
            return "Error with reading destinations from database"

    def update(self, pin, new_price):
        try:
            if pin is None or new_price is None:
                raise ValueError()

            sql_statement = "update reservation set price = ? where pin = ?"
            values = (int(new_price), int(pin))
            self.database.execute(sql_statement, values)
        except ValueError:
            print("Error with updating price")

    def delete(self, pin):
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
        try:
            if id is None:
                raise ValueError()
            sql_statement = "delete from reservation where passenger_id = ?"
            values = (int(id),)
            self.database.execute(sql_statement, values)
            return "Reservation was deleted"
        except ValueError:
            return "Error with deleting reservation"
