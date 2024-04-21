import tkinter as tk
import tkinter.font as tkFont
from src.presentation.passenger_view import Passenger_view
from src.presentation.pilot_view import Pilot_view
from src.presentation.plane_view import Plane_view
from src.presentation.destination_view import Destination_view
from src.presentation.flight_view import Flight_view
from src.presentation.reservation_view import Reservation_view
from src.presentation.reset_database_view import Reset_database_view

"""
Class: Admin_view

This class represents the GUI window for the admin panel.

Methods:
- setup(self): Sets up the GUI elements and layout.
- manage_passengers(self): Opens the window for managing passengers.
- manage_pilots(self): Opens the window for managing pilots.
- manage_planes(self): Opens the window for managing planes.
- manage_destinations(self): Opens the window for managing destinations.
- manage_flights(self): Opens the window for managing flights.
- manage_reservations(self): Opens the window for managing reservations.
- reset_database(self): Opens the window for resetting the database.
- logout(self): Logs out the admin user.

Attributes:
- app: An instance of the main application.
"""

class Admin_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):

        self.title("Bernard's Airport")
        width=1000
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.welcome_heading=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=38)
        self.welcome_heading["font"] = ft
        self.welcome_heading["fg"] = "#333333"
        self.welcome_heading["justify"] = "center"
        self.welcome_heading["text"] = "Hello "+self.master.app.logged_user.get_name()
        self.welcome_heading.place(x=100, y=40, width=800, height=50)

        self.show_profile_btn=tk.Button(self)
        self.show_profile_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.show_profile_btn["font"] = ft
        self.show_profile_btn["fg"] = "#000000"
        self.show_profile_btn["justify"] = "center"
        self.show_profile_btn["text"] = "Manage Passengers"
        self.show_profile_btn.place(x=80, y=160, width=250, height=100)
        self.show_profile_btn["command"] = self.manage_passengers

        self.change_email_btn=tk.Button(self)
        self.change_email_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.change_email_btn["font"] = ft
        self.change_email_btn["fg"] = "#000000"
        self.change_email_btn["justify"] = "center"
        self.change_email_btn["text"] = "Manage Pilots"
        self.change_email_btn.place(x=370, y=160, width=250, height=100)
        self.change_email_btn["command"] = self.manage_pilots

        self.show_my_flights_btn=tk.Button(self)
        self.show_my_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.show_my_flights_btn["font"] = ft
        self.show_my_flights_btn["fg"] = "#000000"
        self.show_my_flights_btn["justify"] = "center"
        self.show_my_flights_btn["text"] = "Manage Planes"
        self.show_my_flights_btn.place(x=660, y=160, width=250, height=100)
        self.show_my_flights_btn["command"] = self.manage_planes

        self.book_flights_btn=tk.Button(self)
        self.book_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.book_flights_btn["font"] = ft
        self.book_flights_btn["fg"] = "#000000"
        self.book_flights_btn["justify"] = "center"
        self.book_flights_btn["text"] = "Manage Destinations"
        self.book_flights_btn.place(x=80, y=340, width=250, height=100)
        self.book_flights_btn["command"] = self.manage_destinations

        self.delete_flights_btn=tk.Button(self)
        self.delete_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_flights_btn["font"] = ft
        self.delete_flights_btn["fg"] = "#000000"
        self.delete_flights_btn["justify"] = "center"
        self.delete_flights_btn["text"] = "Manage Flights"
        self.delete_flights_btn.place(x=370, y=340, width=250, height=100)
        self.delete_flights_btn["command"] = self.manage_flights

        self.delete_account_btn=tk.Button(self)
        self.delete_account_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_account_btn["font"] = ft
        self.delete_account_btn["fg"] = "#000000"
        self.delete_account_btn["justify"] = "center"
        self.delete_account_btn["text"] = "Manage Reservations"
        self.delete_account_btn.place(x=660, y=340, width=250, height=100)
        self.delete_account_btn["command"] = self.manage_reservations

        self.reset_button = tk.Button(self)
        self.reset_button["bg"] = "tomato"
        ft = tkFont.Font(family='Times', size=18)
        self.reset_button["font"] = ft
        self.reset_button["fg"] = "#000000"
        self.reset_button["justify"] = "center"
        self.reset_button["text"] = "Reset database"
        self.reset_button.place(x=200, y=520, width=200, height=100)
        self.reset_button["command"] = self.reset_database

        self.logout_button=tk.Button(self)
        self.logout_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times',size=18)
        self.logout_button["font"] = ft
        self.logout_button["fg"] = "#000000"
        self.logout_button["justify"] = "center"
        self.logout_button["text"] = "Log Out"
        self.logout_button.place(x=520, y=520, width=200, height=100)
        self.logout_button["command"] = self.logout

        self.protocol("WM_DELETE_WINDOW", self.logout)

    def manage_passengers(self):
        passenger_view = Passenger_view(self.master, self)
        passenger_view.deiconify()

    def manage_pilots(self):
        pilot_view = Pilot_view(self.master, self)
        pilot_view.deiconify()

    def manage_planes(self):
        plane_view = Plane_view(self.master, self)
        plane_view.deiconify()

    def manage_destinations(self):
        destination_view = Destination_view(self.master, self)
        destination_view.deiconify()

    def manage_flights(self):
        flight_view = Flight_view(self.master, self)
        flight_view.deiconify()

    def manage_reservations(self):
        reservation_view = Reservation_view(self.master, self)
        reservation_view.deiconify()

    def reset_database(self):
        reset_db_view = Reset_database_view(self.master, self)
        reset_db_view.deiconify()

    def logout(self):
        self.destroy()
        self.app.on_window_close()

