import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import random
import datetime
from src.presentation.success_view import Success_view
from src.presentation.error_view import Error_view
from src.data.models.reservation import Reservation
from src.logic.emailSender import EmailSender
from src.logic.log_writter import Log_writter
"""
Class: Booking_view

This class represents the GUI window for booking flights.

Methods:
- setup(self): Sets up the GUI elements and layout.
- book_flight(self): Books the selected flight.
- move_back(self): Closes the current window.

Attributes:
- app: An instance of the main application.
- flights: A list of available flights.
- email_sender: An instance of the EmailSender class.
- log_writer: An instance of the Log_writer class.
"""
class Booking_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.flights = self.master.app.database_checker.show_flights()
        self.email_sender = None
        self.log_writter = Log_writter()
        self.setup()

    def setup(self):
        # setting title
        self.title("Bernard's Airport - Book flights")
        # setting window size
        width = 1500
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.label_heading = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=28)
        self.label_heading["font"] = ft
        self.label_heading["fg"] = "#333333"
        self.label_heading["justify"] = "center"
        self.label_heading["text"] = "Booking flights"
        self.label_heading.place(x=600, y=40, width=300, height=100)

        self.flight_frame = ttk.Frame(self)
        self.flight_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.flight_tree = ttk.Treeview(self.flight_frame, columns=("Destination", "Plane", "Pilot", "Date leaving", "Date arriving", "Price"))
        self.flight_tree.heading("#0", text="Flight Number")
        self.flight_tree.heading("Destination", text="Destination")
        self.flight_tree.heading("Plane", text="Plane")
        self.flight_tree.heading("Pilot", text="Pilot")
        self.flight_tree.heading("Date leaving", text="Date leaving")
        self.flight_tree.heading("Date arriving", text="Date arriving")
        self.flight_tree.heading("Price", text="Price")

        for flight in self.flights:
            self.flight_tree.insert("", "end", text=flight[0],
                                    values=(flight[1], flight[2], flight[3], flight[4], flight[5], flight[6]))

        self.flight_tree.pack(expand=True, fill=tk.BOTH)

        self.book_button = tk.Button(self)
        self.book_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.book_button["font"] = ft
        self.book_button["fg"] = "#000000"
        self.book_button["justify"] = "center"
        self.book_button["text"] = "BOOK"
        self.book_button.place(x=650, y=490, width=200, height=80)
        self.book_button["command"] = self.book_flight

        self.back_button = tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=13)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=1300, y=570, width=100, height=70)
        self.back_button["command"] = self.move_back

    def book_flight(self):
        selected_items = self.flight_tree.selection()
        if len(selected_items) == 1:
            flight_number = self.flight_tree.item(selected_items[0])["text"]
            values = self.flight_tree.item(selected_items[0])["values"]
            if values:
                price = values[-1]
                flight_id = self.master.app.flight_dao.read_flight_id(flight_number)
                passenger_id = self.master.app.passenger_dao.read_id(self.master.app.logged_user.get_pin())
                reservation = Reservation(random.randint(1, 1000), passenger_id, flight_id, datetime.datetime.now(),
                                          price)
                if self.master.app.reservation_dao.insert(reservation):
                    self.master.app.users_reservation = self.master.app.passenger_dao.read_reservations(self.master.app.passenger_dao.read_id(self.master.app.logged_user.get_pin()))
                    data_to_email = self.master.app.reservation_dao.read_reservations(passenger_id, reservation.get_pin())
                    self.email_sender = EmailSender(data_to_email)
                    self.email_sender.send_reservation_email(self.master.app.logged_user)
                    success = Success_view(self.master, self)
                    success.deiconify()
                else:
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                self.log_writter.write_to_log("Price information not found for the selected flight")
                error = Error_view(self.master, self)
                error.deiconify()
        elif len(selected_items) > 1:
            self.log_writter.write_to_log("Only one flight should be selected")
            error = Error_view(self.master, self)
            error.deiconify()
        else:
            self.log_writter.write_to_log("No flight selected")
            error = Error_view(self.master, self)
            error.deiconify()

    def move_back(self):
        self.destroy()
