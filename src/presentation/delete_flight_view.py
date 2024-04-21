import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
from src.data.dao.reservationDao import ReservationDao
"""
Class: Delete_flights_view

This class represents the GUI window for deleting flights.

Methods:
- setup(self): Sets up the GUI elements and layout.
- delete_flight(self): Deletes the selected flight.
- move_back(self): Closes the current window.

Attributes:
- app: An instance of the main application.
- flights: List of flights belonging to the user.
- reservation_dao: An instance of ReservationDao.
"""
class Delete_flights_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.flights = self.master.app.users_reservation
        self.reservation_dao = ReservationDao(self.master.app.database)
        self.setup()

    def setup(self):
        # setting title
        self.title("Bernard's Airport - My flights")
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
        self.label_heading["text"] = "My flights"
        self.label_heading.place(x=600, y=40, width=300, height=100)

        self.flight_frame = ttk.Frame(self)
        self.flight_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.flight_tree = ttk.Treeview(self.flight_frame, columns=("Destination", "Plane", "Pilot", "Date leaving", "Date arriving", "Price"))
        self.flight_tree.heading("#0", text="Reservation PIN")
        self.flight_tree.heading("Destination", text="Destination")
        self.flight_tree.heading("Plane", text="Plane")
        self.flight_tree.heading("Pilot", text="Pilot")
        self.flight_tree.heading("Date leaving", text="Date leaving")
        self.flight_tree.heading("Date arriving", text="Date arriving")
        self.flight_tree.heading("Price", text="Price")

        for flight in self.flights:
            self.flight_tree.insert("", "end", text=flight[0],
                                    values=(flight[2], flight[5], flight[6], flight[7], flight[8], flight[10]))

        self.flight_tree.pack(expand=True, fill=tk.BOTH)

        self.book_button = tk.Button(self)
        self.book_button["bg"] = "tomato"
        ft = tkFont.Font(family='Times', size=18)
        self.book_button["font"] = ft
        self.book_button["fg"] = "#000000"
        self.book_button["justify"] = "center"
        self.book_button["text"] = "DELETE"
        self.book_button.place(x=650, y=490, width=200, height=80)
        self.book_button["command"] = self.delete_flight

        self.back_button = tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=13)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=1300, y=570, width=100, height=70)
        self.back_button["command"] = self.move_back

    def delete_flight(self):
        selected_items = self.flight_tree.selection()
        if len(selected_items) == 1:
            selected_item = selected_items[0]
            pin = self.flight_tree.item(selected_item)['text']
            if self.reservation_dao.delete(pin):
                success = Success_view(self.master, self)
                success.deiconify()
                self.destroy()
                self.master.app.users_reservation = self.master.app.passenger_dao.read_reservations(self.master.app.passenger_dao.read_id(self.master.app.logged_user.get_pin()))
            else:
                error = Error_view(self.master, self)
                error.deiconify()
        elif len(selected_items) > 1:
            error = Error_view(self.master, self)
            error.deiconify()
        else:
            error = Error_view(self.master, self)
            error.deiconify()

    def move_back(self):
        self.destroy()
