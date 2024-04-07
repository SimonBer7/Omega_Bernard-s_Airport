from src.data.models.passenger import Passenger
from src.data.models.pilot import Pilot
from src.data.models.plane import Plane
from src.data.models.destination import Destination
from src.data.models.flight import Flight
from src.data.models.reservation import Reservation
import csv
import re
import random
import datetime
from prettytable import PrettyTable
from src.logic.emailSender import EmailSender
from src.data.dao.passengerDao import PassengerDao
from src.data.dao.planeDao import PlaneDao
from src.data.dao.pilotDao import PilotDao
from src.data.dao.destinationDao import DestinationDao
from src.data.dao.flightDao import FlightDao
from src.data.dao.reservationDao import ReservationDao

"""
Airport Management User Interface

This class represents the User Interface for the Airport Management System. It handles user interactions, displays
information, and communicates with the application's logic. The UserInterface class uses data access objects (DAOs) to
communicate with the database for various operations related to passengers, planes, pilots, destinations, flights,
and reservations.
"""

class UserInterface:
    def __init__(self, database):
        """
                Initializes the UserInterface with necessary dependencies.

                Attributes:
                    lenght_of_line (int): Represents the length of a line in the output.
                    passenger_dao (PassengerDao): Data Access Object for passenger entities.
                    plane_dao (PlaneDao): Data Access Object for plane entities.
                    pilot_dao (PilotDao): Data Access Object for pilot entities.
                    destination_dao (DestinationDao): Data Access Object for destination entities.
                    flight_dao (FlightDao): Data Access Object for flight entities.
                    reservation_dao (ReservationDao): Data Access Object for reservation entities.
                    app (Application): Reference to the main Application class.
                    paths (List[str]): List of file paths for importing initial data.
                    email_sender (EmailSender): Handles sending reservation-related emails.
                    users_flights (List): List to store information about flights booked by the currently logged-in user.
                    database: Reference to the main Database.

                """
        self.lenght_of_line = 115
        self.passenger_dao = PassengerDao(database)
        self.plane_dao = PlaneDao(database)
        self.pilot_dao = PilotDao(database)
        self.destination_dao = DestinationDao(database)
        self.flight_dao = FlightDao(database)
        self.reservation_dao = ReservationDao(database)
        self.app = None
        self.paths = ["./data/import/pilots.csv", "./data/import/planes.csv", "./data/import/destinations.csv", "./data/import/flights.csv"]
        self.email_sender = None
        self.users_flights = []
        self.database = database


    def print_line(self):
        """
        Prints a horizontal line of dashes to the console.

        """
        print("-" * self.lenght_of_line)

    def new_line(self):
        """
        Returns a newline character.

        Returns:
            str: A newline character.

        """
        return "\n"

    def print_message(self, message):
        """
        Prints a formatted message to the console.

        Parameters:
            message (str): The message to be printed.

        """
        self.print_line()
        print(str(message))

    def check_tables(self):
        """
        Checks the existence of essential tables in the database.

        Returns:
            str: A message indicating the status of the essential tables.

        """
        select_plane = "select count(*) from plane;"
        select_pilot = "select count(*) from pilot;"
        select_destination = "select count(*) from destination;"
        select_flight = "select count(*) from flight;"
        try:
            if (int(self.plane_dao.database.execute_for_agr(select_plane, None)) > 0) and (
                    int(self.pilot_dao.database.execute_for_agr(select_pilot, None)) > 0) and (
                    int(self.destination_dao.database.execute_for_agr(select_destination, None)) > 0) and (
                    int(self.flight_dao.database.execute_for_agr(select_flight, None)) > 0):
                return "The best flights that you can find :D"
            else:
                return str(self.get_data_from_files())
        except Exception as e:
            self.print_message(f"Error reading data from files: {str(e)}")

    def get_data_from_files(self):
        """
        Reads data from CSV files and inserts it into the database.

        Returns:
            str: A message indicating the success of the operation.

        """
        try:
            with open(self.paths[0], "r") as file:
                csv_reader = csv.reader(file, delimiter=";")
                for i in csv_reader:
                    row = i[0].split(",")
                    pilot = Pilot(row[0], row[1], row[2], row[3], row[4])
                    self.pilot_dao.insert(pilot)

            with open(self.paths[1], "r") as file:
                csv_reader = csv.reader(file, delimiter=";")
                for i in csv_reader:
                    row = i[0].split(",")
                    plane = Plane(row[0], row[1], row[2], row[3], row[4])
                    self.plane_dao.insert(plane)

            with open(self.paths[2], "r") as file:
                csv_reader = csv.reader(file, delimiter=";")
                for i in csv_reader:
                    row = i[0].split(",")
                    destination = Destination(row[0], row[1], row[2], row[3])
                    self.destination_dao.insert(destination)

            with open(self.paths[3], "r") as file:
                csv_reader = csv.reader(file, delimiter=";")
                for i in csv_reader:
                    row = i[0].split(",")
                    flight = Flight(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    self.flight_dao.insert(flight)
            self.passenger_dao.insert(
                Passenger("Admin", "Admin", "admin@gmail.com", Passenger.hash_password("admin"), "111111111",
                          "111111/1111"))
            self.app.admin = Passenger("Admin", "Admin", "admin@gmail.com", Passenger.hash_password("admin"),
                                       "111111111", "111111/1111")
            return "The best flights that you can find :D"
        except Exception as e:
            self.print_message(f"Error reading data from files: {str(e)}")

    def print_login(self):
        """
        Displays the login menu and handles user input.

        Returns:
            None or result of the chosen command.

        """
        commands = [("Log In", self.app.login), ("Sign Up", self.app.signup), ("Exit", self.app.exit)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                self.print_message("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()

    def login(self):
        """
        Handles the user login process.

        Returns:
            Passenger or None: The logged-in user or None if login fails.

        """
        try:
            self.print_line()
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            logged_user = self.passenger_dao.read_to_login(email, password)
            return logged_user
        except Exception:
            self.print_message("Error, check your email or password:(")

    def signup(self):
        """
        Handles the user signup process.

        Returns:
            str: A message indicating the success or failure of the signup process.

        """
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last_name: ")
            email = input("Enter your email: ")
            phone_num = input("Enter your phone number: ")
            pin = input("Enter your personal identification number: ")
            password = input("Enter your password: ")
            re_password = input("Enter your password again: ")

            pattern_for_email = "^\S+@\S+\.\S+$"
            reg_obj_for_email = re.search(pattern_for_email, email)

            if reg_obj_for_email:
                pattern_for_phone = "^\d{9}$"
                reg_obj_for_phone = re.search(pattern_for_phone, phone_num)

                if reg_obj_for_phone:
                    pattern_for_pin = "^[0-9]{6}/[0-9]{4}$"
                    reg_obj_fro_pin = re.search(pattern_for_pin, pin)

                    if reg_obj_fro_pin:
                        if password != re_password:
                            raise Exception()
                        else:
                            passenger = Passenger(first_name, last_name, email, Passenger.hash_password(password),
                                                  phone_num, pin)
                            self.print_message(self.passenger_dao.insert(passenger))
                    else:
                        raise ValueError()
                else:
                    raise ValueError()
            else:
                raise ValueError()

        except ValueError:
            self.print_message("Error, wrong format of email, phone number, or pin :(")
        except Exception:
            self.print_message("Error with passwords, they don't match :(")

    def exit(self):
        """
        Exits the application.

        Returns:
            bool: False to indicate the exit of the application.

        """
        return False

    def print_menu(self):
        """
        Displays the main menu and handles user input.

        Returns:
            None or result of the chosen command.

        """
        commands = [("Show profile", self.app.show_profile), ("Change email", self.app.change_email),
                    ("Show my flights", self.app.show_my_flights), ("Book flight", self.app.book_flight),
                    ("Delete my flight", self.app.delete_my_flight), ("Delete account", self.app.delete_acount),
                    ("Log Out", self.app.log_out)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                self.print_message("Error, you have to enter a number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()

    def print_name(self, pas):
        """
        Prints a welcome message with the user's first name.

        Parameters:
            pas (Passenger): The passenger object.

        """
        name = "Hello " + pas.get_first_name()
        return self.print_message(name)

    def show_profile(self, user):
        """
        Displays the profile information of the user.

        Parameters:
            user (Passenger): The passenger object.

        """
        profile = "First name: " + user.first_name + self.new_line() + "Last name: " + user.last_name + self.new_line() + "Email: " + user.email + self.new_line() + "Phone number: " + user.phone_num + self.new_line() + "Personal identification number: " + user.pin
        return self.print_message(profile)

    def change_email(self):
        """
        Handles the process of changing the user's email address.

        Returns:
            str: A message indicating the success or failure of the email change.

        """
        try:
            old_email = input("Enter your email: ")
            password = input("Enter your password: ")
            new_email = input("Enter new email: ")
            if old_email == self.app.logged_user.email and Passenger.hash_password(
                    password) == self.app.logged_user.password:
                pattern = "^\S+@\S+\.\S+$"
                reg_object = re.search(pattern, new_email)
                if reg_object:
                    result = self.passenger_dao.update(new_email, password)
                    self.app.logged_user.email = new_email
                    return result
            if self.app.logged_user.pin == self.app.admin.pin and self.app.logged_user.password == self.app.admin.password:
                pattern = "^\S+@\S+\.\S+$"
                reg_object = re.search(pattern, new_email)
                if reg_object:
                    result = self.passenger_dao.update(new_email, password)
                    return result
        except Exception:
            return "Error, check your email or password:("

    def show_my_flights(self, user):
        """
        Displays the flights booked by the currently logged-in user.

        Parameters:
            user (Passenger): The currently logged-in passenger.

        """
        try:
            if user is None:
                raise ValueError("Invalid user object")
            user_pin = user.get_pin()
            data = self.passenger_dao.read(user_pin)
            if data:
                my_table = PrettyTable()
                my_table.field_names = ["Pin", "Fly number", "Country", "Capital city", "Plane", "Pilot",
                                        "Date leaving", "Date arriving", "Price"]
                for flight in data:
                    my_table.add_row(flight)
                    self.users_flights.append(flight)
                self.print_message(my_table)
            else:
                self.print_message("No flights on your account")
        except ValueError as ve:
            self.print_message(f"Error with showing flights: {ve}")
        except Exception as e:
            self.print_message(f"Error with printing your flights: {e}")

    def book_flight(self):
        """
        Initiates the process of booking a flight.

        """
        flight_table = PrettyTable()
        flight_table.field_names = ["Fly number", "Destination", "Plane", "Pilot", "Date leaving", "Date arriving",
                                    "Price (KC)"]
        try:
            flights = self.flight_dao.read()
            for flight in flights:
                flight_table.add_row(flight)
            self.print_message(flight_table)
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct fly number: ").strip()
                choosen_num = int(choosen_num)
                for flight in flights:
                    if choosen_num == flight[0]:
                        choice = flight[0]

            for flight in flights:
                if flight[0] == choice:
                    choosen_flight = flight

            res_pin = random.randint(1, 1000)
            reservation = Reservation(int(res_pin), self.passenger_dao.read_id(self.app.logged_user.pin),
                                      self.flight_dao.read_flight_id(choice), datetime.datetime.now(),
                                      self.flight_dao.read_flight_price(choice))
            self.print_message(self.reservation_dao.insert(reservation))
            self.email_sender = EmailSender(reservation, choosen_flight)
            self.email_sender.send_reservation_email(self.app.logged_user)
        except Exception as e:
            self.print_message("Error with reading from database")

    def delete_my_flight(self):
        """
        Deletes a booked flight for the currently logged-in user.

        """
        self.show_my_flights(self.app.logged_user)
        choice = None
        while (choice == None):
            choosen_num = input("Enter correct pin: ").strip()
            choosen_num = int(choosen_num)
            for flight in self.users_flights:
                if choosen_num == flight[0]:
                    choice = flight[0]
        self.print_message(self.reservation_dao.delete(choice))

    def delete_acount(self):
        """
        Initiates the process of deleting the user's account.

        """
        try:
            pin = input("Enter your personal identification number: ")
            choice = None
            while (choice == None):
                choosen_num = input("Are you sure that you want to delete this account? (0/1): ").strip()
                try:
                    choosen_num = int(choosen_num)
                    if (not 0 <= choosen_num <= 1):
                        raise Exception()
                    else:
                        break
                except:
                    self.print_message("Error, you have to enter 0 or 1")
                    choosen_num = None
            if choosen_num == 1:
                if pin == self.app.logged_user.pin and pin != self.app.admin.pin:
                    self.reservation_dao.delete(self.passenger_dao.read_id(self.app.logged_user.pin))
                    self.print_message(self.passenger_dao.delete(self.app.logged_user))
                    self.app.logged_user = None
                elif self.app.logged_user.password == self.app.admin.password and pin != self.app.admin.pin:
                    self.reservation_dao.delete_by_pas_id(self.passenger_dao.read_id(pin))
                    self.print_message(self.passenger_dao.admin_delete_by_id(self.passenger_dao.read_id(pin)))
                else:
                    self.print_message("You can not delete the admin account")
            else:
                return
        except Exception:
            self.print_message("Error, check your email or password:(")

    def print_admin_menu(self):
        """
                Prints the menu for the admin console and handles user input to execute corresponding actions.

                Returns
                -------
                str
                    The result of the chosen admin action.
        """
        commands = [("Passenger", self.passenger_crud), ("Pilot", self.app.pilot_crud), ("Plane", self.app.plane_crud), ("Destination", self.app.destination_crud), ("Flight", self.app.flight_crud), ("Reservation", self.app.reservation_crud), ("Reset DB", self.reset_db), ("Log Out", self.app.log_out)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                self.print_message("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()



    def passenger_crud(self):
        """
                Manages passenger-related operations such as insertion, reading, updating, and deletion.

                Returns
                -------
                str
                    The result of the chosen passenger operation.
                """
        commands = [("Insert", self.signup), ("Read", self.print_all_passengers), ("Update", self.change_email), ("Delete", self.delete_acount)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                self.print_message("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()


    def print_all_passengers(self):
        """
                Prints information about all passengers in a tabular format.

                Returns
                -------
                str
                    The formatted table of passenger information.
                """
        data = self.passenger_dao.read_all_passengers()
        table = PrettyTable()
        table.field_names = ["First name", "Last name", "Email", "Phone number", "Personal identification number"]
        for passenger in data:
            table.add_row(passenger)
        self.print_message(table)


    def pilot_crud(self):
        """
                Manages pilot-related operations such as insertion, reading, updating, and deletion.

                Returns
                -------
                str
                    The result of the chosen pilot operation.
                """
        commands = [("Insert", self.get_pilot), ("Read", self.print_pilots), ("Update", self.update_pilots_email), ("Delete", self.delete_pilot)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                self.print_message("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()

    def get_pilot(self):
        """
               Collects information to insert a new pilot.

               Returns
               -------
               str
                   The result of the pilot insertion operation.
               """
        try:
            first_name = input("Enter pilot's first name: ")
            last_name = input("Enter pilot's last_name: ")
            age = input("Enter pilot's age: ")
            email = input("Enter pilot's email: ")
            phone_num = input("Enter pilot's phone number: ")

            pattern_for_email = "^\S+@\S+\.\S+$"
            reg_obj_for_email = re.search(pattern_for_email, email)

            if reg_obj_for_email:
                pattern_for_phone = "^\d{9}$"
                reg_obj_for_phone = re.search(pattern_for_phone, phone_num)

                if reg_obj_for_phone:
                    pilot = Pilot(first_name, last_name, age, email, phone_num)
                    self.print_message(self.pilot_dao.insert(pilot))
            else:
                self.print_message("Error you have to fill email and phone in correct format")
        except Exception:
            self.print_message("Error with inserting pilot")


    def print_pilots(self):
        """
                Prints information about all pilots in a tabular format.

                Returns
                -------
                str
                    The formatted table of pilot information.
                """
        table = PrettyTable()
        table.field_names = ["First name", "Last name", "Age", "Email", "Phone number"]
        data = self.pilot_dao.read_all_pilots()
        for pilot in data:
            table.add_row(pilot)
        self.print_message(table)

    def update_pilots_email(self):
        """
                Updates the email of a pilot.

                Returns
                -------
                str
                    The result of the pilot email update operation.
                """
        try:
            last_name = input("Enter pilot's last name: ")
            old_email = input("Enter pilot's email: ")
            new_email = input("Enter pilot's  new email: ")
            pilots = self.pilot_dao.read_all_pilots()
            for pilot in pilots:
                if old_email == pilot[3] and last_name == pilot[1]:
                    pattern = "^\S+@\S+\.\S+$"
                    reg_object = re.search(pattern, new_email)
                    if reg_object:
                        result = self.pilot_dao.update(old_email, new_email, last_name)
                        self.print_message(result)
        except Exception:
            self.print_message("Error, check your email or password:(")


    def delete_pilot(self):
        """
                Deletes a pilot.

                Returns
                -------
                str
                    The result of the pilot deletion operation.
                """
        try:
            email = input("Enter email: ")
            tmp = input("Are you sure that you want to delete this pilot? (1/0): ")
            if int(tmp) == 1:
                pilots = self.pilot_dao.read_all_pilots()
                for pilot in pilots:
                    if email == pilot[3]:
                        self.print_message(self.pilot_dao.delete(email))
        except Exception:
            self.print_message("Error with deleting pilot")

    def plane_crud(self):
        """
                Manages plane-related operations such as insertion, reading, updating, and deletion.

                Returns
                -------
                str
                    The result of the chosen plane operation.
                """
        commands = [("Insert", self.get_plane), ("Read", self.print_planes), ("Update", self.update_plane_active),
                    ("Delete", self.delete_plane)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                print("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()


    def get_plane(self):
        """
                Collects information to insert a new plane.

                Returns
                -------
                str
                    The result of the plane insertion operation.
                """
        try:
            name = input("Enter name of the plane: ")
            type = input("Enter type (public/private): ")
            capacity = int(input("Enter capacity: "))
            range = int(input("Enter range it can fly (km): "))
            active = int(input("Enter if it's active (1/0): "))

            if isinstance(capacity, int) and isinstance(range, int) and (active == 1 or active == 2):
                plane = Plane(name, type, capacity, range, active)
                self.print_message(self.plane_dao.insert(plane))
            else:
                raise Exception()
        except Exception:
            self.print_message("Error with inserting plane")

    def print_planes(self):
        """
                Prints information about all planes in a tabular format.

                Returns
                -------
                str
                    The formatted table of plane information.
                """
        table = PrettyTable()
        table.field_names = ["Name", "Type", "Capacity", "Range", "Active"]
        data = self.plane_dao.read_all_planes()
        for plane in data:
            table.add_row(plane)
        self.print_message(table)

    def update_plane_active(self):
        """
                Updates the active status of a plane.

                Returns
                -------
                str
                    The result of the plane active status update operation.
                """
        try:
            name = input("Enter name of the plane: ")
            active = input("Is it active? (1/0): ")
            self.plane_dao.update(name, active)
        except Exception:
            self.print_message("Error with updating")


    def delete_plane(self):
        """
               Deletes a plane.

               Returns
               -------
               str
                   The result of the plane deletion operation.
               """
        try:
            name = input("Enter name of the plane: ")
            self.plane_dao.delete(name)
        except Exception:
            self.print_message("Error with deleting")


    def destination_crud(self):
        """
               Manages destination-related operations such as insertion, reading, updating, and deletion.

               Returns
               -------
               str
                   The result of the chosen destination operation.
               """
        commands = [("Insert", self.get_destination), ("Read", self.print_destinations), ("Update", self.update_avg_temp),
                    ("Delete", self.delete_destination)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                print("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()


    def get_destination(self):
        """
                Collects information to insert a new destination.

                Returns
                -------
                str
                    The result of the destination insertion operation.
                """
        try:
            country = input("Enter country: ")
            capital = input("Enter capital city: ")
            language = input("Enter language: ")
            avg_temp = input("Enter average temperature: ")

            destination = Destination(country, capital, language, avg_temp)
            self.destination_dao.insert(destination)
        except Exception:
            self.print_message("Error with inserting")


    def print_destinations(self):
        """
               Prints information about all destinations in a tabular format.

               Returns
               -------
               str
                   The formatted table of destination information.
               """
        table = PrettyTable()
        table.field_names = ["Country", "Capital", "Language", "Avg_temp"]
        data = self.destination_dao.read_all_destinations()
        for destination in data:
            table.add_row(destination)
        self.print_message(table)


    def update_avg_temp(self):
        """
                Updates the average temperature of a destination.

                Returns
                -------
                str
                    The result of the destination average temperature update operation.
                """
        try:
            country = input("Enter country: ")
            avg_temp = input("Enter average temperature: ")
            self.print_line()
            self.destination_dao.update(country, avg_temp)
        except Exception:
            self.print_message("Error with updating")

    def delete_destination(self):
        """
                Deletes a destination.

                Returns
                -------
                str
                    The result of the destination deletion operation.
                """
        try:
            name = input("Enter name of the destination: ")
            self.destination_dao.delete(name)
        except Exception:
            self.print_message("Error with deleting")

    def flight_crud(self):
        """
                Manages flight-related operations such as insertion, reading, updating, and deletion.

                Returns
                -------
                str
                    The result of the chosen flight operation.
                """
        commands = [("Insert", self.get_flight), ("Read", self.print_flights),
                    ("Update", self.update_flight_price),
                    ("Delete", self.delete_flight)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                print("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()


    def get_flight(self):
        """
                Collects information to insert a new flight.

                Returns
                -------
                str
                    The result of the flight insertion operation.
                """
        try:
            fly_num = random.randint(1,1000)

            self.print_destinations()
            choice = None
            while (choice == None):
                choosen_name = input("Enter correct name of country: ").strip()
                choosen_name = str(choosen_name)
                for destination in self.destination_dao.read_all_destinations():
                    if destination[0] == choosen_name:
                        choice = destination[0]

            destination_id = self.destination_dao.read_by_country(choice)

            self.print_planes()
            choice = None
            while (choice == None):
                choosen_name = input("Enter correct name of plane: ").strip()
                choosen_name = str(choosen_name)
                for plane in self.plane_dao.read_all_planes():
                    if plane[0] == choosen_name:
                        choice = plane[0]

            plane_id = self.plane_dao.read_by_name(choice)

            self.print_pilots()
            choice = None
            while (choice == None):
                choosen_name = input("Enter correct last name of pilot: ").strip()
                choosen_name = str(choosen_name)
                for pilot in self.pilot_dao.read_all_pilots():
                    if pilot[1] == choosen_name:
                        choice = pilot[1]

            pilot_id = self.pilot_dao.read_by_name(choice)
            date_leaving = input("Enter date of leaving (yyyy-mm-dd): ")
            date_arriving = input("Enter date of arriving (yyyy-mm-dd): ")
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if date_pattern.match(date_leaving) and date_pattern.match(date_arriving):
                price = int(input("Enter price: "))
                if isinstance(price, int) and int(price) > 0:
                    flight = Flight(fly_num, destination_id, plane_id, pilot_id, date_leaving, date_arriving, price)
                    self.flight_dao.insert(flight)
                    self.print_message("Flight was created")
        except Exception:
            self.print_message("Error with creating flight")


    def print_flights(self):
        """
                Prints information about all flights in a tabular format.

                Returns
                -------
                str
                    The formatted table of flight information.
                """
        flight_table = PrettyTable()
        flight_table.field_names = ["Fly nmuber", "Destination", "PLane", "Pilot", "Date leaving", "Date arriving",
                                    "Price (KC)"]
        try:
            flights = self.flight_dao.read()
            for flight in flights:
                flight_table.add_row(flight)
            self.print_message(flight_table)
        except Exception:
            self.print_message("Error with printing flights from database")
    def update_flight_price(self):
        """
                Updates the price of a flight.

                Returns
                -------
                str
                    The result of the flight price update operation.
                """
        try:
            self.print_flights()
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct fly number: ").strip()
                choosen_num = int(choosen_num)
                for flight in self.flight_dao.read():
                    if flight[0] == choosen_num:
                        choice = flight[0]

            new_price = int(input("Enter new price: "))
            if isinstance(new_price, int) and int(new_price) > 0:
                self.flight_dao.update(choice, new_price)

        except Exception:
            self.print_message("Error with updating flights")

    def delete_flight(self):
        """
                Deletes a flight.

                Returns
                -------
                str
                    The result of the flight deletion operation.
                """
        try:
            self.print_flights()
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct fly number: ").strip()
                choosen_num = int(choosen_num)
                for flight in self.flight_dao.read():
                    if choosen_num == flight[0]:
                        choice = flight[0]
            self.print_message(self.flight_dao.delete(choice))
        except Exception:
            self.print_message("Error with deleting flights")

    def reservation_crud(self):
        """
                Manages reservation-related operations such as insertion, reading, updating, and deletion.

                Returns
                -------
                str
                    The result of the chosen reservation operation.
                """
        commands = [("Insert", self.get_reservation), ("Read", self.print_reservations),
                    ("Update", self.update_reservation_price),
                    ("Delete", self.delete_reservation)]
        i = 1
        self.print_line()
        for command in commands:
            print("\t" + str(i) + ". " + command[0])
            i += 1
        self.print_line()
        choice = None
        while (choice == None):
            choosen_num = input("Enter number (1-" + str(len(commands)) + "): ").strip()
            self.print_line()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
                else:
                    break
            except:
                print("Error, you have to enter number between 1 and " + str(len(commands)))
                choosen_num = None
        return commands[choosen_num - 1][1]()

    def get_reservation(self):
        """
                Collects information to insert a new reservation.

                Returns
                -------
                str
                    The result of the reservation insertion operation.
                """
        try:
            self.print_all_passengers()
            pin = random.randint(1, 1000)
            choice = None
            while (choice == None):
                choosen_pin = input("Enter correct pin of passenger: ").strip()
                choosen_pin = str(choosen_pin)
                for passenger in self.passenger_dao.read_all_passengers():
                    if passenger[4] == choosen_pin:
                        choice = passenger[4]

            passenger_id = self.passenger_dao.read_id(choice)
            self.print_flights()
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct fly nmuber: ").strip()
                choosen_num = int(choosen_num)
                for flight in self.flight_dao.read():
                    if choosen_num == flight[0]:
                        choice = flight[0]
            flight_id = self.flight_dao.read_flight_id(choice)
            date = datetime.datetime.now()
            price = self.flight_dao.read_flight_price(choice)
            reservation = Reservation(pin, passenger_id, flight_id, date, price)
            self.print_message(self.reservation_dao.insert(reservation))
        except Exception:
            self.print_message("Error with creating flights")

    def print_reservations(self):
        """
                Prints information about all reservations in a tabular format.

                Returns
                -------
                str
                    The formatted table of reservation information.
                """
        table = PrettyTable()
        table.field_names = ["Pin", "Fly number", "Passenger", "Country", "Plane", "Pilot", "Date leaving", "Date arriving", "Price (KC)"]
        try:
            reservations = self.reservation_dao.read()
            for res in reservations:
                table.add_row(res)
            self.print_message(table)
        except Exception:
            self.print_message("Error with printing flights from database")

    def update_reservation_price(self):
        """
               Updates the price of a reservation.

               Returns
               -------
               str
                   The result of the reservation price update operation.
               """
        try:
            self.print_reservations()
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct pin of reservation: ").strip()
                choosen_num = int(choosen_num)
                for reservation in self.reservation_dao.read():
                    if reservation[0] == choosen_num:
                        choice = reservation[0]

            new_price = int(input("Enter new price: "))
            if isinstance(new_price, int) and int(new_price) > 0:
                self.reservation_dao.update(choice, new_price)

        except Exception:
            self.print_message("Error with updating reservation")

    def delete_reservation(self):
        """
                Deletes a reservation.

                Returns
                -------
                str
                    The result of the reservation deletion operation.
                """
        try:
            self.print_reservations()
            choice = None
            while (choice == None):
                choosen_num = input("Enter correct pin of reservation: ").strip()
                choosen_num = int(choosen_num)
                for reservation in self.reservation_dao.read():
                    if reservation[0] == choosen_num:
                        choice = reservation[0]
                self.reservation_dao.delete(choice)
        except Exception:
            self.print_message("Error with deleting reservation")

    def reset_db(self):
        """
               Resets the database by dropping and recreating it.

               Returns
               -------
               None
               """
        self.database.drop_database()
        self.database.create_database()