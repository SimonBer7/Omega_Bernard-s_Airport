import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from src.data.models.plane import Plane
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
from src.logic.log_writter import Log_writter
"""
Class: Add_plane_view

This class represents the GUI window for adding a new plane.

Methods:
- setup(self): Sets up the GUI elements and layout.
- on_window_close(self): Handles the window close event.
- add_plane(self): Handles the process of adding a new plane.
- close(self): Closes the current window.

Attributes:
- app: An instance of the main application.
- log_writer: An instance of the Log_writter class for logging.
"""
class Add_plane_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.log_writter = Log_writter()
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Planes")
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
        self.create_heading["text"] = "Create new plane"
        self.create_heading.place(x=270, y=0, width=300, height=100)

        self.label_email = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "left"
        self.label_email["text"] = "Type:"
        self.label_email.place(x=100, y=180, width=250, height=50)

        options = ["Public", "Private"]
        self.dropdown = ttk.Combobox(self, values=options, state="readonly", font=(14))
        self.dropdown.pack(pady=5)
        self.dropdown.place(x=400, y=180, width=300, height=50)

        self.label_active = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_active["font"] = ft
        self.label_active["fg"] = "#333333"
        self.label_active["justify"] = "left"
        self.label_active["text"] = "Active:"
        self.label_active.place(x=100, y=340, width=250, height=50)

        options_for_active = ["1", "0"]
        self.dropdown_active = ttk.Combobox(self, values=options_for_active, state="readonly", font=(14))
        self.dropdown_active.pack(pady=5)
        self.dropdown_active.place(x=400, y=340, width=300, height=50)

        self.create_button = tk.Button(self)
        self.create_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.create_button["font"] = ft
        self.create_button["fg"] = "#000000"
        self.create_button["justify"] = "center"
        self.create_button["text"] = "CREATE"
        self.create_button.place(x=280, y=510, width=200, height=80)
        self.create_button["command"] = self.add_passenger

        self.entry_capacity = tk.Entry(self)
        self.entry_capacity["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_capacity["font"] = ft
        self.entry_capacity["fg"] = "#333333"
        self.entry_capacity["justify"] = "center"
        self.entry_capacity["text"] = ""
        self.entry_capacity.place(x=400, y=260, width=300, height=50)

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

        self.label_capacity = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_capacity["font"] = ft
        self.label_capacity["fg"] = "#333333"
        self.label_capacity["justify"] = "left"
        self.label_capacity["text"] = "Capacity"
        self.label_capacity.place(x=100, y=260, width=250, height=50)

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
        try:
            capacity = int(self.entry_capacity.get())
            if capacity >= 0:
                plane = Plane(self.entry_name.get(), self.dropdown.get(), capacity, self.dropdown_active.get())
                if self.master.app.plane_dao.insert(plane):
                    self.entry_name.delete(0, tk.END)
                    self.dropdown.delete(0, tk.END)
                    self.entry_capacity.delete(0, tk.END)
                    self.dropdown_active.delete(0, tk.END)
                    success = Success_view(self.master, self)
                    success.deiconify()
                    self.destroy()
                else:
                    self.entry_name.delete(0, tk.END)
                    self.dropdown.delete(0, tk.END)
                    self.entry_capacity.delete(0, tk.END)
                    self.dropdown_active.delete(0, tk.END)
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                self.entry_name.delete(0, tk.END)
                self.dropdown.delete(0, tk.END)
                self.entry_capacity.delete(0, tk.END)
                self.dropdown_active.delete(0, tk.END)
                raise ValueError
        except ValueError:
            error = Error_view(self.master, self)
            error.deiconify()
            self.log_writter.write_to_log("Age must be an integer.")

    def close(self):
        self.destroy()
