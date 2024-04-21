import tkinter as tk
import tkinter.font as tkFont
from src.presentation.success_view import Success_view
from src.presentation.error_view import Error_view
"""
Class: Change_email_view

This class represents the GUI window for changing the user's email.

Methods:
- setup(self): Sets up the GUI elements and layout.
- move_back(self): Closes the current window.
- update_email(self): Updates the user's email.

Attributes:
- app: An instance of the main application.
"""

class Change_email_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Change email")
        #setting window size
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.main_heading=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=38)
        self.main_heading["font"] = ft
        self.main_heading["fg"] = "#333333"
        self.main_heading["justify"] = "center"
        self.main_heading["text"] = "Change your email"
        self.main_heading.place(x=0, y=20, width=800, height=100)

        self.back_button=tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times',size=18)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=570, y=590, width=200, height=80)
        self.back_button["command"] = self.move_back

        self.label_current_email=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=18)
        self.label_current_email["font"] = ft
        self.label_current_email["fg"] = "#333333"
        self.label_current_email["justify"] = "left"
        self.label_current_email["text"] = "Current email: "
        self.label_current_email.place(x=60, y=150, width=300, height=50)

        self.entry_current_email = tk.Entry(self)
        self.entry_current_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_current_email["font"] = ft
        self.entry_current_email["fg"] = "#333333"
        self.entry_current_email["justify"] = "center"
        self.entry_current_email["text"] = ""
        self.entry_current_email.place(x=400, y=150, width=300, height=50)

        self.label_new_email=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=18)
        self.label_new_email["font"] = ft
        self.label_new_email["fg"] = "#333333"
        self.label_new_email["justify"] = "left"
        self.label_new_email["text"] = "New email:"
        self.label_new_email.place(x=60, y=250, width=300, height=50)

        self.entry_new_email = tk.Entry(self)
        self.entry_new_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_new_email["font"] = ft
        self.entry_new_email["fg"] = "#333333"
        self.entry_new_email["justify"] = "center"
        self.entry_new_email["text"] = ""
        self.entry_new_email.place(x=400, y=250, width=300, height=50)

        self.label_password=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=18)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["justify"] = "left"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=60, y=350, width=300, height=50)

        self.entry_password = tk.Entry(self)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=400, y=350, width=300, height=50)

        self.update_button=tk.Button(self)
        self.update_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times',size=18)
        self.update_button["font"] = ft
        self.update_button["fg"] = "#000000"
        self.update_button["justify"] = "center"
        self.update_button["text"] = "UPDATE"
        self.update_button.place(x=300, y=450, width=200, height=100)
        self.update_button["command"] = self.update_email

    def move_back(self):
        self.destroy()

    def update_email(self):
        if self.master.app.change_email(self.entry_new_email.get(), self.entry_current_email.get(), self.entry_password.get()):
            self.entry_new_email.delete(0, tk.END)
            self.entry_current_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            success = Success_view(self.master, self)
            success.deiconify()
        else:
            self.entry_new_email.delete(0, tk.END)
            self.entry_current_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            error = Error_view(self.master, self)
            error.deiconify()