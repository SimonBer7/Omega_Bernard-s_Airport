import tkinter as tk
import tkinter.font as tkFont

class Signup:
    def __init__(self, app):
        self.root = None
        self.app = app
        self.setup()


    def setup(self):
        self.root = tk.Tk()
        #setting title
        self.root.title("Sign up")
        #setting window size
        width=800
        height=700
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_809=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_809["font"] = ft
        GLabel_809["fg"] = "#333333"
        GLabel_809["justify"] = "center"
        GLabel_809["text"] = "Sign up"
        GLabel_809.place(x=250,y=30,width=250,height=100)

        GLineEdit_338=tk.Entry(self.root)
        GLineEdit_338["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_338["font"] = ft
        GLineEdit_338["fg"] = "#333333"
        GLineEdit_338["justify"] = "center"
        GLineEdit_338["text"] = "Enter your email"
        GLineEdit_338.place(x=330,y=250,width=250,height=50)

        GLabel_256=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "center"
        GLabel_256["text"] = "Email:"
        GLabel_256.place(x=110,y=250,width=150,height=50)

        GLabel_366=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_366["font"] = ft
        GLabel_366["fg"] = "#333333"
        GLabel_366["justify"] = "center"
        GLabel_366["text"] = "Password:"
        GLabel_366.place(x=130,y=350,width=150,height=50)

        GLineEdit_203=tk.Entry(self.root)
        GLineEdit_203["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_203["font"] = ft
        GLineEdit_203["fg"] = "#333333"
        GLineEdit_203["justify"] = "center"
        GLineEdit_203["text"] = "Enter your password"
        GLineEdit_203.place(x=330,y=350,width=250,height=50)

        GButton_519=tk.Button(self.root)
        GButton_519["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "SIGN UP"
        GButton_519.place(x=250,y=460,width=250,height=50)
        GButton_519["command"] = self.GButton_519_command

        GLabel_590=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_590["font"] = ft
        GLabel_590["fg"] = "#333333"
        GLabel_590["justify"] = "center"
        GLabel_590["text"] = "Already have an account?"
        GLabel_590.place(x=140,y=600,width=300,height=50)

        GButton_132=tk.Button(self.root)
        GButton_132["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "Log in"
        GButton_132.place(x=400,y=610,width=100,height=30)
        GButton_132["command"] = self.switch_to_login

        GLabel_235=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_235["font"] = ft
        GLabel_235["fg"] = "#333333"
        GLabel_235["justify"] = "center"
        GLabel_235["text"] = "Name:"
        GLabel_235.place(x=110,y=160,width=150,height=50)

        GLineEdit_714=tk.Entry(self.root)
        GLineEdit_714["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_714["font"] = ft
        GLineEdit_714["fg"] = "#333333"
        GLineEdit_714["justify"] = "center"
        GLineEdit_714["text"] = "Enter your name"
        GLineEdit_714.place(x=330,y=160,width=250,height=50)
        self.root.mainloop()

    def switch_to_login(self):
        self.app.login()

    def GButton_519_command(self):
        print("command")

