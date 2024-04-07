import tkinter as tk
import tkinter.font as tkFont


class Login:
    def __init__(self, app):
        self.app = app
        self.root = None
        self.setup()

    def setup(self):
        # Setting title
        self.root = tk.Tk()
        self.root.title("Log In")
        # Setting window size
        width = 800
        height = 700
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        login_heading = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=46)
        login_heading["font"] = ft
        login_heading["fg"] = "#333333"
        login_heading["justify"] = "center"
        login_heading["text"] = "Log In"
        login_heading.place(x=250, y=30, width=250, height=100)

        email_label = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=23)
        email_label["font"] = ft
        email_label["fg"] = "#333333"
        email_label["justify"] = "center"
        email_label["text"] = "Email:"
        email_label.place(x=70, y=180, width=250, height=50)

        self.entry_email = tk.Entry(self.root)
        self.entry_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.entry_email["font"] = ft
        self.entry_email["fg"] = "#333333"
        self.entry_email["justify"] = "center"
        self.entry_email["text"] = ""
        self.entry_email.place(x=360, y=180, width=250, height=50)

        password_label = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=23)
        password_label["font"] = ft
        password_label["fg"] = "#333333"
        password_label["justify"] = "center"
        password_label["text"] = "Password:"
        password_label.place(x=90, y=290, width=250, height=50)

        self.entry_password = tk.Entry(self.root)
        self.entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.entry_password["font"] = ft
        self.entry_password["fg"] = "#333333"
        self.entry_password["justify"] = "center"
        self.entry_password["text"] = ""
        self.entry_password.place(x=360, y=290, width=250, height=50)

        login_button = tk.Button(self.root)
        login_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=18)
        login_button["font"] = ft
        login_button["fg"] = "#000000"
        login_button["justify"] = "center"
        login_button["text"] = "LOG IN"
        login_button.place(x=260, y=400, width=250, height=100)
        login_button["command"] = self.login

        text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=13)
        text["font"] = ft
        text["fg"] = "#333333"
        text["justify"] = "center"
        text["text"] = "Don't have an account?"
        text.place(x=110, y=570, width=250, height=50)

        signup_button = tk.Button(self.root)
        signup_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        signup_button["font"] = ft
        signup_button["fg"] = "#000000"
        signup_button["justify"] = "center"
        signup_button["text"] = "Sign up"
        signup_button.place(x=500, y=560, width=100, height=50)
        signup_button["command"] = self.switch_to_signup
        self.root.mainloop()

    def login(self):
        self.app.authorization(self.entry_email, self.entry_password)

    def switch_to_signup(self):
        self.app.signup()


if __name__ == "__main__":
    app = Login(None)  # Pass None since the parent app reference is not needed in this case
