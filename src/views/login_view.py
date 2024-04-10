import tkinter as tk
import tkinter.font as tkFont
from src.views.user_main_view import User_main_view

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

        self.login_heading = tk.Label(self)
        ft = tkFont.Font(family='Times', size=46)
        self.login_heading["font"] = ft
        self.login_heading["fg"] = "#333333"
        self.login_heading["justify"] = "center"
        self.login_heading["text"] = "Log In"
        self.login_heading.place(x=250, y=30, width=250, height=100)

        self.email_label = tk.Label(self)
        ft = tkFont.Font(family='Times', size=23)
        self.email_label["font"] = ft
        self.email_label["fg"] = "#333333"
        self.email_label["justify"] = "center"
        self.email_label["text"] = "Email:"
        self.email_label.place(x=70, y=180, width=250, height=50)

        self.entry_email = tk.Entry(self)
        self.entry_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_email["font"] = ft
        self.entry_email["fg"] = "#333333"
        self.entry_email["justify"] = "center"
        self.entry_email["text"] = ""
        self.entry_email.place(x=360, y=180, width=250, height=50)

        self.password_label = tk.Label(self)
        ft = tkFont.Font(family='Times', size=23)
        self.password_label["font"] = ft
        self.password_label["fg"] = "#333333"
        self.password_label["justify"] = "center"
        self.password_label["text"] = "Password:"
        self.password_label.place(x=90, y=290, width=250, height=50)

        self.entry_password = tk.Entry(self)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=360, y=290, width=250, height=50)

        self.login_button = tk.Button(self)
        self.login_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        self.login_button["font"] = ft
        self.login_button["fg"] = "#000000"
        self.login_button["justify"] = "center"
        self.login_button["text"] = "LOG IN"
        self.login_button.place(x=260, y=400, width=250, height=100)
        self.login_button["command"] = self.login

        self.text = tk.Label(self)
        ft = tkFont.Font(family='Times', size=13)
        self.text["font"] = ft
        self.text["fg"] = "#333333"
        self.text["justify"] = "center"
        self.text["text"] = "Don't have an account?"
        self.text.place(x=110, y=570, width=250, height=50)

        self.signup_button = tk.Button(self)
        self.signup_button["bg"] = "#f0f0f0"
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

    def login(self):
        if self.app.authorization(self.entry_email.get(), self.entry_password.get()):
            self.entry_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.show_user_main_view()
        else:
            self.entry_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.title("Log In - Error, try again")

    def move_to_signup(self):
        self.destroy()
        self.master.deiconify()
        self.master.switch_to_signup()


