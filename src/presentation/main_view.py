import tkinter as tk
from src.presentation.login_view import Login_view
from src.presentation.signup_view import Signup_view

"""
   Class representing the main application window.

   Attributes:
       app: An instance of the main application.

   Methods:
       setup(self): Sets up the GUI elements and layout.
       switch_to_login(self): Switches to the login view.
       switch_to_signup(self): Switches to the signup view.
   """
class MainWindow(tk.Tk):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setup()

    def setup(self):
        # Setting title
        self.title("Bernard's Airport")
        # Setting window size
        width = 800
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        # Load background image
        bg_image = tk.PhotoImage(file="./data/img/bg.png")

        # Create a label for the background image
        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Ensure the image is not garbage-collected
        bg_label.image = bg_image

        # Main title label
        self.main_title = tk.Label(self, text="Welcome to Bernard's Airport, let's book some flights",
                                   font=("Times", 23), bg="lightskyblue", fg="#333333")
        self.main_title.place(x=40, y=50, width=700, height=50)

        # Login button
        self.login_button = tk.Button(self, text="Log in", font=("Times", 23), bg="lightskyblue", fg="#000000",
                                       command=self.switch_to_login)
        self.login_button.place(x=100, y=240, width=200, height=200)

        # Signup button
        self.signup_button = tk.Button(self, text="Sign up", font=("Times", 23), bg="lightskyblue", fg="#000000",
                                        command=self.switch_to_signup)
        self.signup_button.place(x=500, y=240, width=200, height=200)

    def switch_to_login(self):
        self.withdraw()
        login_view = Login_view(self, self.app)
        login_view.deiconify()

    def switch_to_signup(self):
        self.withdraw()
        signup_view = Signup_view(self, self.app)
        signup_view.deiconify()
