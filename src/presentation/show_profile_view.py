import tkinter as tk
import tkinter.font as tkFont

"""
   Class representing the GUI window for displaying user profile information.

   Attributes:
       app: An instance of the main application.

   Methods:
       setup(self): Sets up the GUI elements and layout.
       move_back(self): Closes the current window.
   """

class Profile_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):
        # Setting title
        self.title("Bernard's Airport - Profile")
        # Setting window size
        width = 800
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.main_heading = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=38)
        self.main_heading["font"] = ft
        self.main_heading["fg"] = "#333333"
        self.main_heading["justify"] = "center"
        self.main_heading["text"] = "Profile"
        self.main_heading.place(x=0, y=40, width=800, height=50)

        self.back_button = tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=18)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=300, y=500, width=200, height=100)
        self.back_button["command"] = self.move_back

        self.label_name = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_name["font"] = ft
        self.label_name["fg"] = "#333333"
        self.label_name["justify"] = "left"
        self.label_name["text"] = "Name: "
        self.label_name.place(x=100, y=120, width=300, height=50)

        self.label_email = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "left"
        self.label_email["text"] = "Email: "
        self.label_email.place(x=100, y=200, width=300, height=50)

        self.label_phone = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_phone["font"] = ft
        self.label_phone["fg"] = "#333333"
        self.label_phone["justify"] = "left"
        self.label_phone["text"] = "Phone mnuber:"
        self.label_phone.place(x=100, y=280, width=300, height=50)

        self.label_pin = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=18)
        self.label_pin["font"] = ft
        self.label_pin["fg"] = "#333333"
        self.label_pin["justify"] = "left"
        self.label_pin["text"] = "PIN:"
        self.label_pin.place(x=100, y=360, width=300, height=50)

        message_data = [
            (self.master.app.logged_user.get_name(), 400, 120),
            (self.master.app.logged_user.get_email(), 400, 200),
            (self.master.app.logged_user.get_phone_num(), 400, 280),
            (self.master.app.logged_user.get_pin(), 400, 360)
        ]
        message_width = 300
        message_height = 50
        for text, x, y in message_data:
            message = tk.Message(self, bg="lightblue", font=("Times", 18), fg="#333333", justify="center",
                                 text=text, width=message_width)
            message.place(x=x, y=y, width=message_width, height=message_height)

    def move_back(self):
        self.destroy()


