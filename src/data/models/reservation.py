class Reservation:
    def __init__(self, pin, pass_id, flight_id, date, price):
        self.pin = pin
        self.passenger_id = pass_id
        self.flight_id = flight_id
        self.date = date
        self.price = price

    def get_pin(self):
        return self.pin

    def get_passenger_id(self):
        return self.passenger_id

    def get_flight_id(self):
        return self.flight_id

    def get_date(self):
        return self.date

    def get_price(self):
        return self.price
