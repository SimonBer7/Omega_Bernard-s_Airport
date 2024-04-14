import tkinter as tk
import tkinter.font as tkFont
from src.views.show_profile_view import Profile_view
from src.views.change_email_view import Change_email_view
from src.views.delete_account_view import Delete_account_view

class User_main_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):

        self.title("Bernard's Airport")
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.welcome_heading=tk.Label(self)
        ft = tkFont.Font(family='Times',size=38)
        self.welcome_heading["font"] = ft
        self.welcome_heading["fg"] = "#333333"
        self.welcome_heading["justify"] = "center"
        self.welcome_heading["text"] = "Welcome back "+self.master.app.logged_user.get_name()
        self.welcome_heading.place(x=0, y=40, width=800, height=50)

        self.show_profile_btn=tk.Button(self)
        self.show_profile_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.show_profile_btn["font"] = ft
        self.show_profile_btn["fg"] = "#000000"
        self.show_profile_btn["justify"] = "center"
        self.show_profile_btn["text"] = "Show profile"
        self.show_profile_btn.place(x=40, y=160, width=200, height=100)
        self.show_profile_btn["command"] = self.show_profile

        self.change_email_btn=tk.Button(self)
        self.change_email_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.change_email_btn["font"] = ft
        self.change_email_btn["fg"] = "#000000"
        self.change_email_btn["justify"] = "center"
        self.change_email_btn["text"] = "Change email"
        self.change_email_btn.place(x=300, y=160, width=200, height=100)
        self.change_email_btn["command"] = self.change_email

        self.show_my_flights_btn=tk.Button(self)
        self.show_my_flights_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.show_my_flights_btn["font"] = ft
        self.show_my_flights_btn["fg"] = "#000000"
        self.show_my_flights_btn["justify"] = "center"
        self.show_my_flights_btn["text"] = "Show my flights"
        self.show_my_flights_btn.place(x=560, y=160, width=200, height=100)
        self.show_my_flights_btn["command"] = self.GButton_99_command

        self.book_flights_btn=tk.Button(self)
        self.book_flights_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.book_flights_btn["font"] = ft
        self.book_flights_btn["fg"] = "#000000"
        self.book_flights_btn["justify"] = "center"
        self.book_flights_btn["text"] = "Book flights"
        self.book_flights_btn.place(x=40, y=340, width=200, height=100)
        self.book_flights_btn["command"] = self.GButton_75_command

        self.delete_flights_btn=tk.Button(self)
        self.delete_flights_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_flights_btn["font"] = ft
        self.delete_flights_btn["fg"] = "#000000"
        self.delete_flights_btn["justify"] = "center"
        self.delete_flights_btn["text"] = "Delete my flights"
        self.delete_flights_btn.place(x=300, y=340, width=200, height=100)
        self.delete_flights_btn["command"] = self.GButton_367_command

        self.delete_account_btn=tk.Button(self)
        self.delete_account_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_account_btn["font"] = ft
        self.delete_account_btn["fg"] = "#000000"
        self.delete_account_btn["justify"] = "center"
        self.delete_account_btn["text"] = "Delete account"
        self.delete_account_btn.place(x=560, y=340, width=200, height=100)
        self.delete_account_btn["command"] = self.delete_account

        self.logout_button=tk.Button(self)
        self.logout_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.logout_button["font"] = ft
        self.logout_button["fg"] = "#000000"
        self.logout_button["justify"] = "center"
        self.logout_button["text"] = "Log Out"
        self.logout_button.place(x=420, y=520, width=200, height=100)
        self.logout_button["command"] = self.logout

        self.protocol("WM_DELETE_WINDOW", self.logout)

    def show_profile(self):
        profile_view = Profile_view(self.master, self)
        profile_view.deiconify()

    def change_email(self):
        change_email_view = Change_email_view(self.master, self)
        change_email_view.deiconify()


    def GButton_99_command(self):
        print("command")


    def GButton_75_command(self):
        print("command")


    def GButton_367_command(self):
        print("command")


    def delete_account(self):
        delete_account_view = Delete_account_view(self.master, self)
        delete_account_view.deiconify()


    def logout(self):
        self.destroy()
        self.app.on_window_close()


