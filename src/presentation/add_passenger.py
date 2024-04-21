import tkinter as tk
import tkinter.font as tkFont
from src.data.models.passenger import Passenger
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
"""
Class: Add_passenger_view

This class represents the GUI window for adding a new passenger.

Methods:
- setup(self): Sets up the GUI elements and layout.
- on_window_close(self): Handles the window close event.
- add_passenger(self): Handles the process of adding a new passenger.
- close(self): Closes the current window.

Attributes:
- app: An instance of the main application.
"""

class Add_passenger_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Passengers")
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
        self.create_heading["text"] = "Create new passenger"
        self.create_heading.place(x=270, y=0, width=300, height=100)

        self.label_email = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "left"
        self.label_email["text"] = "Email:"
        self.label_email.place(x=100, y=180, width=250, height=50)

        self.entry_email = tk.Entry(self)
        self.entry_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_email["font"] = ft
        self.entry_email["fg"] = "#333333"
        self.entry_email["justify"] = "center"
        self.entry_email["text"] = ""
        self.entry_email.place(x=400, y=170, width=300, height=50)

        self.label_password = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["justify"] = "left"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=100, y=370, width=250, height=50)

        self.entry_password = tk.Entry(self)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=400, y=370, width=300, height=50)

        self.create_button = tk.Button(self)
        self.create_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.create_button["font"] = ft
        self.create_button["fg"] = "#000000"
        self.create_button["justify"] = "center"
        self.create_button["text"] = "CREATE"
        self.create_button.place(x=280, y=510, width=200, height=80)
        self.create_button["command"] = self.add_passenger

        self.label_password_again = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_password_again["font"] = ft
        self.label_password_again["fg"] = "#333333"
        self.label_password_again["justify"] = "left"
        self.label_password_again["text"] = "Password again:"
        self.label_password_again.place(x=100, y=440, width=250, height=50)

        self.entry_password_again = tk.Entry(self)
        self.entry_password_again["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password_again["font"] = ft
        self.entry_password_again["fg"] = "#333333"
        self.entry_password_again["justify"] = "center"
        self.entry_password_again["text"] = ""
        self.entry_password_again.place(x=400, y=440, width=300, height=50)

        self.entry_phone = tk.Entry(self)
        self.entry_phone["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_phone["font"] = ft
        self.entry_phone["fg"] = "#333333"
        self.entry_phone["justify"] = "center"
        self.entry_phone["text"] = ""
        self.entry_phone.place(x=400, y=240, width=300, height=50)

        self.entry_name = tk.Entry(self)
        self.entry_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_name["font"] = ft
        self.entry_name["fg"] = "#333333"
        self.entry_name["justify"] = "center"
        self.entry_name["text"] = ""
        self.entry_name.place(x=400, y=100, width=300, height=50)

        self.label_name = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_name["font"] = ft
        self.label_name["fg"] = "#333333"
        self.label_name["justify"] = "left"
        self.label_name["text"] = "Name:"
        self.label_name.place(x=100, y=100, width=250, height=50)

        self.label_phone = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_phone["font"] = ft
        self.label_phone["fg"] = "#333333"
        self.label_phone["justify"] = "left"
        self.label_phone["text"] = "Phone number"
        self.label_phone.place(x=100, y=240, width=250, height=50)

        self.entry_pin = tk.Entry(self)
        self.entry_pin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_pin["font"] = ft
        self.entry_pin["fg"] = "#333333"
        self.entry_pin["justify"] = "center"
        self.entry_pin["text"] = ""
        self.entry_pin.place(x=400, y=300, width=300, height=50)

        self.label_pin = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_pin["font"] = ft
        self.label_pin["fg"] = "#333333"
        self.label_pin["justify"] = "left"
        self.label_pin["text"] = "PIN"
        self.label_pin.place(x=100, y=300, width=250, height=50)

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

    def add_passenger(self):
        passenger = Passenger(self.entry_name.get(), self.entry_email.get(), self.entry_password.get(), self.entry_phone.get(), self.entry_pin.get())
        if self.master.app.passenger_dao.insert(passenger):
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_pin.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_password_again.delete(0, tk.END)
            success = Success_view(self.master, self)
            success.deiconify()
            self.destroy()
        else:
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_pin.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_password_again.delete(0, tk.END)
            error = Error_view(self.master, self)
            error.deiconify()

    def close(self):
        self.destroy()

