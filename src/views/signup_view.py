import tkinter as tk
import tkinter.font as tkFont
from src.data.models.passenger import Passenger

class Signup_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()


    def setup(self):
        #setting title
        self.title("Sign up")
        #setting window size
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.signup_heading = tk.Label(self)
        ft = tkFont.Font(family='Times', size=46)
        self.signup_heading["font"] = ft
        self.signup_heading["fg"] = "#333333"
        self.signup_heading["justify"] = "center"
        self.signup_heading["text"] = "Sign Up"
        self.signup_heading.place(x=270, y=0, width=250, height=100)

        self.label_email = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "left"
        self.label_email["text"] = "Email:"
        self.label_email.place(x=150, y=180, width=250, height=50)

        self.entry_email = tk.Entry(self)
        self.entry_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_email["font"] = ft
        self.entry_email["fg"] = "#333333"
        self.entry_email["justify"] = "center"
        self.entry_email["text"] = ""
        self.entry_email.place(x=400, y=170, width=250, height=50)

        self.label_password = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["justify"] = "left"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=150, y=370, width=250, height=50)

        self.entry_password = tk.Entry(self)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=400, y=370, width=250, height=50)

        self.signup_button = tk.Button(self)
        self.signup_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        self.signup_button["font"] = ft
        self.signup_button["fg"] = "#000000"
        self.signup_button["justify"] = "center"
        self.signup_button["text"] = "SIGN UP"
        self.signup_button.place(x=280, y=510, width=200, height=80)
        self.signup_button["command"] = self.signup

        self.text = tk.Label(self)
        ft = tkFont.Font(family='Times', size=13)
        self.text["font"] = ft
        self.text["fg"] = "#333333"
        self.text["justify"] = "center"
        self.text["text"] = "Already have an account?"
        self.text.place(x=130, y=610, width=250, height=50)

        self.login_button = tk.Button(self)
        self.login_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.login_button["font"] = ft
        self.login_button["fg"] = "#000000"
        self.login_button["justify"] = "center"
        self.login_button["text"] = "Log In"
        self.login_button.place(x=500, y=610, width=100, height=50)
        self.login_button["command"] = self.move_to_login

        self.label_password_again = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_password_again["font"] = ft
        self.label_password_again["fg"] = "#333333"
        self.label_password_again["justify"] = "left"
        self.label_password_again["text"] = "Password again:"
        self.label_password_again.place(x=150, y=440, width=250, height=50)

        self.entry_password_again = tk.Entry(self)
        self.entry_password_again["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password_again["font"] = ft
        self.entry_password_again["fg"] = "#333333"
        self.entry_password_again["justify"] = "center"
        self.entry_password_again["text"] = ""
        self.entry_password_again.place(x=400, y=440, width=250, height=50)

        self.entry_phone = tk.Entry(self)
        self.entry_phone["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_phone["font"] = ft
        self.entry_phone["fg"] = "#333333"
        self.entry_phone["justify"] = "center"
        self.entry_phone["text"] = ""
        self.entry_phone.place(x=400, y=240, width=250, height=50)

        self.entry_name = tk.Entry(self)
        self.entry_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_name["font"] = ft
        self.entry_name["fg"] = "#333333"
        self.entry_name["justify"] = "center"
        self.entry_name["text"] = ""
        self.entry_name.place(x=400, y=100, width=250, height=50)

        self.label_name = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_name["font"] = ft
        self.label_name["fg"] = "#333333"
        self.label_name["justify"] = "left"
        self.label_name["text"] = "Name:"
        self.label_name.place(x=150, y=100, width=250, height=50)

        self.label_phone = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_phone["font"] = ft
        self.label_phone["fg"] = "#333333"
        self.label_phone["justify"] = "left"
        self.label_phone["text"] = "Phone number"
        self.label_phone.place(x=150, y=240, width=250, height=50)

        self.entry_pin = tk.Entry(self)
        self.entry_pin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_pin["font"] = ft
        self.entry_pin["fg"] = "#333333"
        self.entry_pin["justify"] = "center"
        self.entry_pin["text"] = ""
        self.entry_pin.place(x=400, y=300, width=250, height=50)

        self.label_pin = tk.Label(self)
        ft = tkFont.Font(family='Times', size=18)
        self.label_pin["font"] = ft
        self.label_pin["fg"] = "#333333"
        self.label_pin["justify"] = "left"
        self.label_pin["text"] = "PIN"
        self.label_pin.place(x=150, y=300, width=250, height=50)

        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def on_window_close(self):
        self.destroy()
        self.master.deiconify()

    def signup(self):
        passenger = Passenger(self.entry_name.get(), self.entry_email.get(), self.entry_password.get(), self.entry_phone.get(), self.entry_pin.get())
        if self.app.passenger_dao.insert(passenger):
            self.move_to_login()
        else:
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_pin.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.entry_password_again.delete(0, tk.END)
            self.title("Sign Up - Error, try again")



    def move_to_login(self):
        self.destroy()
        self.master.deiconify()
        self.master.switch_to_login()


