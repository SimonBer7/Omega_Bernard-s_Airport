import tkinter as tk
import tkinter.font as tkFont
from src.views.login_view import Login_view
from src.views.signup_view import Signup_view


class MainWindow(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setup()

    def setup(self):
        #setting title
        self.title("Bernard's Airport")
        #setting window size
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.main_title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=23)
        self.main_title["font"] = ft
        self.main_title["fg"] = "#333333"
        self.main_title["justify"] = "center"
        self.main_title["text"] = "Welcome in Bernard's Airport let's book some flights"
        self.main_title.place(x=40, y=100, width=700, height=50)

        self.login_button=tk.Button(self)
        self.login_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=23)
        self.login_button["font"] = ft
        self.login_button["fg"] = "#000000"
        self.login_button["justify"] = "center"
        self.login_button["text"] = "Log in"
        self.login_button.place(x=100, y=240, width=200, height=200)
        self.login_button["command"] = self.switch_to_login

        self.signup_button=tk.Button(self)
        self.signup_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=23)
        self.signup_button["font"] = ft
        self.signup_button["fg"] = "#000000"
        self.signup_button["justify"] = "center"
        self.signup_button["text"] = "Sign up"
        self.signup_button.place(x=500, y=240, width=200, height=200)
        self.signup_button["command"] = self.switch_to_signup

    def switch_to_login(self):
        self.withdraw()
        login_view = Login_view(self, self.app)
        login_view.deiconify()

    def switch_to_signup(self):
        self.withdraw()
        signup_view = Signup_view(self, self.app)
        signup_view.deiconify()




