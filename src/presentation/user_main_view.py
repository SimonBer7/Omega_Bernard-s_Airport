import tkinter as tk
import tkinter.font as tkFont
from src.presentation.show_profile_view import Profile_view
from src.presentation.change_email_view import Change_email_view
from src.presentation.delete_account_view import Delete_account_view
from src.presentation.booking_view import Booking_view
from src.presentation.my_flights_view import My_flights_view
from src.presentation.delete_flight_view import Delete_flights_view

"""
   Class representing the main user interface window.

   Methods:
       setup(self): Sets up the GUI elements and layout.
       show_profile(self): Opens the profile view.
       change_email(self): Opens the change email view.
       show_my_flights(self): Opens the view for displaying booked flights.
       book_flights_view(self): Opens the view for booking flights.
       delete_my_flights(self): Opens the view for deleting booked flights.
       delete_account(self): Opens the view for deleting the user account.
       logout(self): Logs out the user and closes the window.
   """
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

        bg_image = tk.PhotoImage(file="./data/img/bg.png")

        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        bg_label.image = bg_image


        self.welcome_heading=tk.Label(self, bg="white")
        ft = tkFont.Font(family='Times',size=38)
        self.welcome_heading["font"] = ft
        self.welcome_heading["fg"] = "#333333"
        self.welcome_heading["justify"] = "center"
        self.welcome_heading["text"] = "Welcome back "+self.master.app.logged_user.get_name()
        self.welcome_heading.place(x=0, y=30, width=800, height=100)

        self.show_profile_btn=tk.Button(self)
        self.show_profile_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.show_profile_btn["font"] = ft
        self.show_profile_btn["fg"] = "#000000"
        self.show_profile_btn["justify"] = "center"
        self.show_profile_btn["text"] = "Show profile"
        self.show_profile_btn.place(x=40, y=200, width=200, height=100)
        self.show_profile_btn["command"] = self.show_profile

        self.change_email_btn=tk.Button(self)
        self.change_email_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.change_email_btn["font"] = ft
        self.change_email_btn["fg"] = "#000000"
        self.change_email_btn["justify"] = "center"
        self.change_email_btn["text"] = "Change email"
        self.change_email_btn.place(x=300, y=200, width=200, height=100)
        self.change_email_btn["command"] = self.change_email

        self.show_my_flights_btn=tk.Button(self)
        self.show_my_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.show_my_flights_btn["font"] = ft
        self.show_my_flights_btn["fg"] = "#000000"
        self.show_my_flights_btn["justify"] = "center"
        self.show_my_flights_btn["text"] = "Show my flights"
        self.show_my_flights_btn.place(x=560, y=200, width=200, height=100)
        self.show_my_flights_btn["command"] = self.show_my_flights

        self.book_flights_btn=tk.Button(self)
        self.book_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.book_flights_btn["font"] = ft
        self.book_flights_btn["fg"] = "#000000"
        self.book_flights_btn["justify"] = "center"
        self.book_flights_btn["text"] = "Book flights"
        self.book_flights_btn.place(x=40, y=380, width=200, height=100)
        self.book_flights_btn["command"] = self.book_flights_view

        self.delete_flights_btn=tk.Button(self)
        self.delete_flights_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_flights_btn["font"] = ft
        self.delete_flights_btn["fg"] = "#000000"
        self.delete_flights_btn["justify"] = "center"
        self.delete_flights_btn["text"] = "Delete my flights"
        self.delete_flights_btn.place(x=300, y=380, width=200, height=100)
        self.delete_flights_btn["command"] = self.delete_my_flights

        self.delete_account_btn=tk.Button(self)
        self.delete_account_btn["bg"] = "lightskyblue"
        ft = tkFont.Font(family='Times',size=18)
        self.delete_account_btn["font"] = ft
        self.delete_account_btn["fg"] = "#000000"
        self.delete_account_btn["justify"] = "center"
        self.delete_account_btn["text"] = "Delete account"
        self.delete_account_btn.place(x=560, y=380, width=200, height=100)
        self.delete_account_btn["command"] = self.delete_account

        self.logout_button=tk.Button(self)
        self.logout_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times',size=18)
        self.logout_button["font"] = ft
        self.logout_button["fg"] = "#000000"
        self.logout_button["justify"] = "center"
        self.logout_button["text"] = "Log Out"
        self.logout_button.place(x=420, y=550, width=200, height=100)
        self.logout_button["command"] = self.logout

        self.protocol("WM_DELETE_WINDOW", self.logout)

    def show_profile(self):
        profile_view = Profile_view(self.master, self)
        profile_view.deiconify()

    def change_email(self):
        change_email_view = Change_email_view(self.master, self)
        change_email_view.deiconify()


    def show_my_flights(self):
        my_flights_view = My_flights_view(self.master, self)
        my_flights_view.deiconify()


    def book_flights_view(self):
        book_flights_view = Booking_view(self.master, self)
        book_flights_view.deiconify()


    def delete_my_flights(self):
        delete_flights_view = Delete_flights_view(self.master, self)
        delete_flights_view.deiconify()


    def delete_account(self):
        delete_account_view = Delete_account_view(self.master, self)
        delete_account_view.deiconify()


    def logout(self):
        self.destroy()
        self.app.on_window_close()

