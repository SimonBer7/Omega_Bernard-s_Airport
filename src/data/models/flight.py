class Flight:
    def __init__(self, fly_num, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price):
        self.fly_number = fly_num
        self.destination_id = destination_id
        self.plane_id = plane_id
        self.pilot_id = pilot_id
        self.date_leaving = date_leaving
        self.date_arriving = date_arriving
        self.price = price

    def get_fly_number(self):
        return self.fly_number

    def get_destination_id(self):
        return self.destination_id

    def get_plane_id(self):
        return self.plane_id

    def get_pilot_id(self):
        return self.pilot_id

    def get_date_leaving(self):
        return self.date_leaving

    def get_date_arriving(self):
        return self.date_arriving

    def get_price(self):
        return self.price
