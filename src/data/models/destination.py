class Destination:
    def __init__(self, country, capital, avg_temp):
        self.country = country
        self.capital = capital
        self.avg_temp = avg_temp

    def get_country(self):
        return self.country

    def get_capital(self):
        return self.capital

    def get_avg_temp(self):
        return self.avg_temp
