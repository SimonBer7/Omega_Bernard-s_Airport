import hashlib
import re

class Passenger:
    def __init__(self, name, email, password, phone_num, pin):
        self.name = None
        self.email = None
        self.password = None
        self.phone_num = None
        self.pin = None
        self.setup(name, email, password, phone_num, pin)

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_phone_num(self):
        return self.phone_num

    def get_pin(self):
        return self.pin

    def setup(self, name, email, password, phone_num, pin):
        if self.check_info(email, phone_num, pin):
            self.name = name
            self.email = email
            self.password = self.hash_password(password)
            self.phone_num = phone_num
            self.pin = pin

    @classmethod
    def hash_password(cls, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @classmethod
    def check_info(cls, email, phone_num, pin):
        email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(email):
            return False

        phone_pattern = re.compile(r'^\d{9}$')
        if not phone_pattern.match(phone_num):
            return False

        pin_pattern = re.compile(r'^\d{6}/\d{4}$')
        if not pin_pattern.match(pin):
            return False

        return True


    def to_string(self):
        return f"Passeger {self.name}, email: {self.email}, " \
            f"password: {self.password}, phone: {self.phone_num}, pin: {self.pin}"
