import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from src.presentation.add_passenger import Add_passenger_view
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
from src.logic.log_writter import Log_writter
"""
    Class representing the GUI window for managing passengers.

    Attributes:
        app: An instance of the main application.
        passengers: List of passengers.
        log_writer: Instance of Log_writer for logging.

    Methods:
        setup(self): Sets up the GUI elements and layout.
        open_add_passenger(self): Opens the window to add a new passenger.
        delete_passenger(self): Deletes the selected passenger.
        move_back(self): Closes the current window and moves back to the previous window.
    """
class Passenger_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.passengers = self.master.app.load_passengers()
        self.log_writter = Log_writter()
        self.setup()

    def setup(self):
        # setting title
        self.title("Bernard's Airport - Passengers")
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
        self.label_heading["text"] = "Passengers"
        self.label_heading.place(x=600, y=40, width=300, height=100)

        self.flight_frame = ttk.Frame(self)
        self.flight_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.flight_tree = ttk.Treeview(self.flight_frame, columns=("Email", "Phone number", "PIN"))
        self.flight_tree.heading("#0", text="Name")
        self.flight_tree.heading("Email", text="Email")
        self.flight_tree.heading("Phone number", text="Phone number")
        self.flight_tree.heading("PIN", text="PIN")

        for passenger in self.passengers:
            self.flight_tree.insert("", "end", text=passenger[0],
                                    values=(passenger[1], passenger[2], passenger[3]))

        self.flight_tree.pack(expand=True, fill=tk.BOTH)

        self.delete_button = tk.Button(self)
        self.delete_button["bg"] = "tomato"
        ft = tkFont.Font(family='Times', size=18)
        self.delete_button["font"] = ft
        self.delete_button["fg"] = "#000000"
        self.delete_button["justify"] = "center"
        self.delete_button["text"] = "Delete"
        self.delete_button.place(x=800, y=490, width=200, height=80)
        self.delete_button["command"] = self.delete_passenger

        self.create_button = tk.Button(self)
        self.create_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.create_button["font"] = ft
        self.create_button["fg"] = "#000000"
        self.create_button["justify"] = "center"
        self.create_button["text"] = "Create"
        self.create_button.place(x=500, y=490, width=200, height=80)
        self.create_button["command"] = self.open_add_passenger

        self.back_button = tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=13)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=1300, y=570, width=100, height=70)
        self.back_button["command"] = self.move_back

    def open_add_passenger(self):
        create_passenger = Add_passenger_view(self.master, self)
        create_passenger.deiconify()
        self.destroy()

    def delete_passenger(self):
        selected_items = self.flight_tree.selection()
        if len(selected_items) == 1:
            values = self.flight_tree.item(selected_items[0])["values"]
            if values and values[2] != "111111/1111":
                if self.master.app.reservation_dao.delete_by_pas_id(self.master.app.passenger_dao.read_id(values[2])) and self.master.app.passenger_dao.admin_delete_by_pin(values[2]):
                    self.destroy()
                    succes = Success_view(self.master, self)
                    succes.deiconify()
                else:
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                self.log_writter.write_to_log("Error with the selected passenger")
                error = Error_view(self.master, self)
                error.deiconify()
        elif len(selected_items) > 1:
            self.log_writter.write_to_log("Only one passenger should be selected")
            error = Error_view(self.master, self)
            error.deiconify()
        else:
            self.log_writter.write_to_log("No passengers selected")
            error = Error_view(self.master, self)
            error.deiconify()


    def move_back(self):
        self.destroy()
