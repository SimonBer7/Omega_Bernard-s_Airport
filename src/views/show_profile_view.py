import tkinter as tk
import tkinter.font as tkFont

class Profile_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):
        #setting title
        self.title("Bernard's Airport - Profile")
        #setting window size
        width=800
        height=700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.GLabel_732=tk.Label(self)
        ft = tkFont.Font(family='Times',size=38)
        self.GLabel_732["font"] = ft
        self.GLabel_732["fg"] = "#333333"
        self.GLabel_732["justify"] = "center"
        self.GLabel_732["text"] = "Profile"
        self.GLabel_732.place(x=0,y=40,width=800,height=50)

        self.GButton_209=tk.Button(self)
        self.GButton_209["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.GButton_209["font"] = ft
        self.GButton_209["fg"] = "#000000"
        self.GButton_209["justify"] = "center"
        self.GButton_209["text"] = "Back"
        self.GButton_209.place(x=300,y=570,width=200,height=100)
        self.GButton_209["command"] = self.GButton_209_command

        self.GLabel_557=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_557["font"] = ft
        self.GLabel_557["fg"] = "#333333"
        self.GLabel_557["justify"] = "left"
        self.GLabel_557["text"] = "Name: "
        self.GLabel_557.place(x=100,y=120,width=300,height=50)

        self.GMessage_597=tk.Message(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GMessage_597["font"] = ft
        self.GMessage_597["fg"] = "#333333"
        self.GMessage_597["justify"] = "center"
        self.GMessage_597["text"] = self.master.app.logged_user.get_name()
        self.GMessage_597.place(x=400,y=120,width=300,height=50)

        self.GLabel_935=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_935["font"] = ft
        self.GLabel_935["fg"] = "#333333"
        self.GLabel_935["justify"] = "left"
        self.GLabel_935["text"] = "Email: "
        self.GLabel_935.place(x=100,y=200,width=300,height=50)

        self.GMessage_713=tk.Message(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GMessage_713["font"] = ft
        self.GMessage_713["fg"] = "#333333"
        self.GMessage_713["justify"] = "center"
        self.GMessage_713["text"] = self.master.app.logged_user.get_email()
        self.GMessage_713.place(x=400,y=200,width=300,height=50)

        self.GLabel_142=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_142["font"] = ft
        self.GLabel_142["fg"] = "#333333"
        self.GLabel_142["justify"] = "left"
        self.GLabel_142["text"] = "Password: "
        self.GLabel_142.place(x=100,y=280,width=300,height=50)

        self.GMessage_571=tk.Message(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GMessage_571["font"] = ft
        self.GMessage_571["fg"] = "#333333"
        self.GMessage_571["justify"] = "center"
        self.GMessage_571["text"] = self.master.app.logged_user.get_password()
        self.GMessage_571.place(x=400,y=280,width=300,height=50)

        self.GLabel_723=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_723["font"] = ft
        self.GLabel_723["fg"] = "#333333"
        self.GLabel_723["justify"] = "left"
        self.GLabel_723["text"] = "Phone mnuber:"
        self.GLabel_723.place(x=100,y=360,width=300,height=50)

        self.GMessage_936=tk.Message(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GMessage_936["font"] = ft
        self.GMessage_936["fg"] = "#333333"
        self.GMessage_936["justify"] = "center"
        self.GMessage_936["text"] = self.master.app.logged_user.get_phone_num()
        self.GMessage_936.place(x=400,y=360,width=300,height=50)

        self.GLabel_49=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_49["font"] = ft
        self.GLabel_49["fg"] = "#333333"
        self.GLabel_49["justify"] = "left"
        self.GLabel_49["text"] = "PIN:"
        self.GLabel_49.place(x=100,y=440,width=300,height=50)

        self.GMessage_446=tk.Message(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GMessage_446["font"] = ft
        self.GMessage_446["fg"] = "#333333"
        self.GMessage_446["justify"] = "center"
        self.GMessage_446["text"] = self.master.app.logged_user.get_pin()
        self.GMessage_446.place(x=400,y=440,width=300,height=50)

    def GButton_209_command(self):
        print("command")


