import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from src.presentation.success_view import Success_view
from src.presentation.error_view import Error_view
from src.logic.log_writter import Log_writter
"""
Class: Flight_view

This class represents the GUI window for displaying flight information.

Attributes:
    app: An instance of the main application.
    flights: A list of flights loaded from the main application.
    log_writer: An instance of the Log_writter class for logging.

Methods:
    setup(self): Sets up the GUI elements and layout.
    delete_flight(self): Deletes the selected flight from the list of flights.
    move_back(self): Destroys the current window and moves back to the previous window.
"""
class Flight_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.flights = self.master.app.load_flights()
        self.log_writter = Log_writter()
        self.setup()

    def setup(self):
        # setting title
        self.title("Bernard's Airport - Flights")
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
        self.label_heading["text"] = "Flights"
        self.label_heading.place(x=600, y=40, width=300, height=100)

        self.flight_frame = ttk.Frame(self)
        self.flight_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.flight_tree = ttk.Treeview(self.flight_frame, columns=("Country", "Plane", "Pilot", "Date leaving", "Date arriving", "Price"))
        self.flight_tree.heading("#0", text="Fly number")
        self.flight_tree.heading("Country", text="Country")
        self.flight_tree.heading("Plane", text="Plane")
        self.flight_tree.heading("Pilot", text="Pilot")
        self.flight_tree.heading("Date leaving", text="Date leaving")
        self.flight_tree.heading("Date arriving", text="Date leaving")
        self.flight_tree.heading("Price", text="Price")

        for flight in self.flights:
            self.flight_tree.insert("", "end", text=flight[0],
                                    values=(flight[1], flight[2], flight[3], flight[4], flight[5] ,flight[6]))

        self.flight_tree.pack(expand=True, fill=tk.BOTH)

        self.delete_button = tk.Button(self)
        self.delete_button["bg"] = "tomato"
        ft = tkFont.Font(family='Times', size=18)
        self.delete_button["font"] = ft
        self.delete_button["fg"] = "#000000"
        self.delete_button["justify"] = "center"
        self.delete_button["text"] = "Delete"
        self.delete_button.place(x=650, y=490, width=200, height=80)
        self.delete_button["command"] = self.delete_flight

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
            values = self.flight_tree.item(selected_items)['text']
            if values:
                if self.master.app.flight_dao.delete(values):
                    self.destroy()
                    succes = Success_view(self.master, self)
                    succes.deiconify()
                else:
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                self.log_writter.write_to_log("Error with deleting plane")
                error = Error_view(self.master, self)
                error.deiconify()
        elif len(selected_items) > 1:
            self.log_writter.write_to_log("Only one plane should be selected")
            error = Error_view(self.master, self)
            error.deiconify()
        else:
            self.log_writter.write_to_log("No plane selected")
            error = Error_view(self.master, self)
            error.deiconify()

    def move_back(self):
        self.destroy()
