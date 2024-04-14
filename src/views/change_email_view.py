import tkinter as tk
import tkinter.font as tkFont


class Change_email_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Change email")
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
        self.GLabel_732["text"] = "Change your email"
        self.GLabel_732.place(x=0,y=20,width=800,height=100)

        self.GButton_209=tk.Button(self)
        self.GButton_209["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.GButton_209["font"] = ft
        self.GButton_209["fg"] = "#000000"
        self.GButton_209["justify"] = "center"
        self.GButton_209["text"] = "Back"
        self.GButton_209.place(x=570,y=590,width=200,height=80)
        self.GButton_209["command"] = self.move_back

        self.GLabel_935=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_935["font"] = ft
        self.GLabel_935["fg"] = "#333333"
        self.GLabel_935["justify"] = "left"
        self.GLabel_935["text"] = "Current email: "
        self.GLabel_935.place(x=60,y=150,width=300,height=50)

        self.GLineEdit_479 = tk.Entry(self)
        self.GLineEdit_479["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.GLineEdit_479["font"] = ft
        self.GLineEdit_479["fg"] = "#333333"
        self.GLineEdit_479["justify"] = "center"
        self.GLineEdit_479["text"] = ""
        self.GLineEdit_479.place(x=400, y=150, width=300, height=50)

        self.GLabel_723=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_723["font"] = ft
        self.GLabel_723["fg"] = "#333333"
        self.GLabel_723["justify"] = "left"
        self.GLabel_723["text"] = "New email:"
        self.GLabel_723.place(x=60,y=250,width=300,height=50)

        self.GLineEdit_597 = tk.Entry(self)
        self.GLineEdit_597["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.GLineEdit_597["font"] = ft
        self.GLineEdit_597["fg"] = "#333333"
        self.GLineEdit_597["justify"] = "center"
        self.GLineEdit_597["text"] = ""
        self.GLineEdit_597.place(x=400, y=250, width=300, height=50)

        self.GLabel_49=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_49["font"] = ft
        self.GLabel_49["fg"] = "#333333"
        self.GLabel_49["justify"] = "left"
        self.GLabel_49["text"] = "Password:"
        self.GLabel_49.place(x=60,y=350,width=300,height=50)

        self.GLineEdit_584 = tk.Entry(self)
        self.GLineEdit_584["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=18)
        self.GLineEdit_584["font"] = ft
        self.GLineEdit_584["fg"] = "#333333"
        self.GLineEdit_584["justify"] = "center"
        self.GLineEdit_584["text"] = ""
        self.GLineEdit_584.place(x=400, y=350, width=300, height=50)

        self.GButton_170=tk.Button(self)
        self.GButton_170["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        self.GButton_170["font"] = ft
        self.GButton_170["fg"] = "#000000"
        self.GButton_170["justify"] = "center"
        self.GButton_170["text"] = "UPDATE"
        self.GButton_170.place(x=300,y=450,width=200,height=100)
        self.GButton_170["command"] = self.GButton_170_command

    def move_back(self):
        self.destroy()


    def GButton_170_command(self):
        print("command")

