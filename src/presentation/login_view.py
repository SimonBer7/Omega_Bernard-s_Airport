import tkinter as tk
import tkinter.font as tkFont
from src.presentation.user_main_view import User_main_view
from src.presentation.error_view import Error_view
from src.presentation.admin_view import Admin_view
"""
Class: Login_view

This class represents the GUI window for user login.

Attributes:
    app: An instance of the main application.

Methods:
    setup(self): Sets up the GUI elements and layout.
    on_window_close(self): Handles window close event.
    show_user_main_view(self): Switches to the user main view.
    show_admin_view(self): Switches to the admin view.
    login(self): Validates user login credentials.
    move_to_signup(self): Switches to the signup view.
"""
class Login_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):
        # Setting title
        self.title("Log In")
        # Setting window size
        width = 800
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.login_heading = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=46)
        self.login_heading["font"] = ft
        self.login_heading["fg"] = "#333333"
        self.login_heading["justify"] = "center"
        self.login_heading["text"] = "Log In"
        self.login_heading.place(x=250, y=30, width=250, height=100)

        self.email_label = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=23)
        self.email_label["font"] = ft
        self.email_label["fg"] = "#333333"
        self.email_label["justify"] = "center"
        self.email_label["text"] = "Email:"
        self.email_label.place(x=40, y=180, width=250, height=50)

        self.entry_email = tk.Entry(self)
        self.entry_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_email["font"] = ft
        self.entry_email["fg"] = "#333333"
        self.entry_email["justify"] = "center"
        self.entry_email["text"] = ""
        self.entry_email.place(x=360, y=180, width=300, height=50)

        self.password_label = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=23)
        self.password_label["font"] = ft
        self.password_label["fg"] = "#333333"
        self.password_label["justify"] = "center"
        self.password_label["text"] = "Password:"
        self.password_label.place(x=60, y=290, width=250, height=50)

        self.entry_password = tk.Entry(self)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=360, y=290, width=300, height=50)

        self.login_button = tk.Button(self)
        self.login_button["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times', size=18)
        self.login_button["font"] = ft
        self.login_button["fg"] = "#000000"
        self.login_button["justify"] = "center"
        self.login_button["text"] = "LOG IN"
        self.login_button.place(x=260, y=400, width=250, height=100)
        self.login_button["command"] = self.login

        self.text = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=13)
        self.text["font"] = ft
        self.text["fg"] = "#333333"
        self.text["justify"] = "center"
        self.text["text"] = "Don't have an account?"
        self.text.place(x=110, y=570, width=250, height=50)

        self.signup_button = tk.Button(self)
        self.signup_button["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times', size=10)
        self.signup_button["font"] = ft
        self.signup_button["fg"] = "#000000"
        self.signup_button["justify"] = "center"
        self.signup_button["text"] = "Sign up"
        self.signup_button.place(x=500, y=560, width=100, height=50)
        self.signup_button["command"] = self.move_to_signup

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def on_window_close(self):
        self.destroy()
        self.master.deiconify()

    def show_user_main_view(self):
        self.withdraw()
        user_amin_view = User_main_view(self.master, self)
        user_amin_view.mainloop()

    def show_admin_view(self):
        self.withdraw()
        admin_view = Admin_view(self.master, self)
        admin_view.mainloop()


    def login(self):
        if self.app.authorization(self.entry_email.get(), self.entry_password.get()):
            self.entry_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            if self.master.app.logged_user.get_pin() == "111111/1111":
                self.show_admin_view()
            else:
                self.show_user_main_view()
        else:
            self.entry_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            error = Error_view(self.master, self)
            error.deiconify()

    def move_to_signup(self):
        self.destroy()
        self.master.deiconify()
        self.master.switch_to_signup()

