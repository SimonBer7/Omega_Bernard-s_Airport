import tkinter as tk
import tkinter.font as tkFont
from src.data.models.destination import Destination
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
from src.logic.log_writter import Log_writter
"""
Class: Add_Destination_view

This class represents the GUI window for adding a new destination.

Methods:
- setup(self): Sets up the GUI elements and layout.
- on_window_close(self): Handles the window close event.
- add_destination(self): Handles the process of adding a new destination.
- close(self): Closes the current window.

Attributes:
- app: An instance of the main application.
- log_writer: An instance of the Log_writter class for logging.
"""

class Add_Destination_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.log_writter = Log_writter()
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Destinations")
        #setting window size
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.create_heading = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=25)
        self.create_heading["font"] = ft
        self.create_heading["fg"] = "#333333"
        self.create_heading["justify"] = "center"
        self.create_heading["text"] = "Create new Destination"
        self.create_heading.place(x=270, y=0, width=300, height=100)

        self.label_capital = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_capital["font"] = ft
        self.label_capital["fg"] = "#333333"
        self.label_capital["justify"] = "left"
        self.label_capital["text"] = "Capital city:"
        self.label_capital.place(x=100, y=180, width=250, height=50)

        self.entry_capital = tk.Entry(self)
        self.entry_capital["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_capital["font"] = ft
        self.entry_capital["fg"] = "#333333"
        self.entry_capital["justify"] = "center"
        self.entry_capital["text"] = ""
        self.entry_capital.place(x=400, y=180, width=300, height=50)


        self.create_button = tk.Button(self)
        self.create_button["bg"] = "lighgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.create_button["font"] = ft
        self.create_button["fg"] = "#000000"
        self.create_button["justify"] = "center"
        self.create_button["text"] = "CREATE"
        self.create_button.place(x=280, y=510, width=200, height=80)
        self.create_button["command"] = self.add_destination


        self.entry_temerature = tk.Entry(self)
        self.entry_temerature["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_temerature["font"] = ft
        self.entry_temerature["fg"] = "#333333"
        self.entry_temerature["justify"] = "center"
        self.entry_temerature["text"] = ""
        self.entry_temerature.place(x=400, y=260, width=300, height=50)

        self.entry_country = tk.Entry(self)
        self.entry_country["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_country["font"] = ft
        self.entry_country["fg"] = "#333333"
        self.entry_country["justify"] = "center"
        self.entry_country["text"] = ""
        self.entry_country.place(x=400, y=100, width=300, height=50)

        self.label_country = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_country["font"] = ft
        self.label_country["fg"] = "#333333"
        self.label_country["justify"] = "left"
        self.label_country["text"] = "Country:"
        self.label_country.place(x=100, y=100, width=250, height=50)

        self.label_temperature = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_temperature["font"] = ft
        self.label_temperature["fg"] = "#333333"
        self.label_temperature["justify"] = "left"
        self.label_temperature["text"] = "Average temperature"
        self.label_temperature.place(x=100, y=260, width=250, height=50)

        self.close_button = tk.Button(self)
        self.close_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=18)
        self.close_button["font"] = ft
        self.close_button["fg"] = "#000000"
        self.close_button["justify"] = "center"
        self.close_button["text"] = "Back"
        self.close_button.place(x=580, y=600, width=200, height=80)
        self.close_button["command"] = self.close

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def on_window_close(self):
        self.destroy()

    def add_destination(self):
        try:
            temperature = float(self.entry_temerature.get())
            if float(temperature) or temperature == 0:
                destination = Destination(self.entry_country.get(), self.entry_capital.get(), temperature)
                if self.master.app.destination_dao.insert(destination):
                    self.entry_country.delete(0, tk.END)
                    self.entry_capital.delete(0, tk.END)
                    self.entry_temerature.delete(0, tk.END)
                    success = Success_view(self.master, self)
                    success.deiconify()
                    self.destroy()
                else:
                    self.entry_country.delete(0, tk.END)
                    self.entry_capital.delete(0, tk.END)
                    self.entry_temerature.delete(0, tk.END)
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                raise ValueError
        except ValueError:
            self.entry_country.delete(0, tk.END)
            self.entry_capital.delete(0, tk.END)
            self.entry_temerature.delete(0, tk.END)
            error = Error_view(self.master, self)
            error.deiconify()
            self.log_writter.write_to_log("Age must be an integer.")

    def close(self):
        self.destroy()

