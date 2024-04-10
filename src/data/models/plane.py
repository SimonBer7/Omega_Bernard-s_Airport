class Plane:
    def __init__(self, name, type, capacity, active):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.active = active

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_capacity(self):
        return self.capacity

    def get_active(self):
        return self.active
