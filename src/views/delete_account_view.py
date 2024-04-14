import tkinter as tk
import tkinter.font as tkFont

class Delete_account_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()


    def setup(self):
        #setting title
        self.title("Bernard's Airport - Delete account")
        #setting window size
        width=500
        height=400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_732=tk.Label(self)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_732["font"] = ft
        GLabel_732["fg"] = "#333333"
        GLabel_732["justify"] = "center"
        GLabel_732["text"] = ""
        GLabel_732.place(x=0,y=20,width=800,height=100)

        GLabel_669=tk.Label(self)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_669["font"] = ft
        GLabel_669["fg"] = "#333333"
        GLabel_669["justify"] = "center"
        GLabel_669["text"] = "Delete Account"
        GLabel_669.place(x=0,y=0,width=500,height=100)

        GLabel_146=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_146["font"] = ft
        GLabel_146["fg"] = "#333333"
        GLabel_146["justify"] = "center"
        GLabel_146["text"] = "Are you sure you want to delete this account?"
        GLabel_146.place(x=0,y=90,width=500,height=100)

        GButton_790=tk.Button(self)
        GButton_790["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_790["font"] = ft
        GButton_790["fg"] = "#000000"
        GButton_790["justify"] = "center"
        GButton_790["text"] = "YES"
        GButton_790.place(x=120,y=220,width=100,height=70)
        GButton_790["command"] = self.GButton_790_command

        GButton_617=tk.Button(self)
        GButton_617["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_617["font"] = ft
        GButton_617["fg"] = "#000000"
        GButton_617["justify"] = "center"
        GButton_617["text"] = "NO"
        GButton_617.place(x=290,y=220,width=100,height=70)
        GButton_617["command"] = self.GButton_617_command

    def GButton_790_command(self):
        print("command")


    def GButton_617_command(self):
        print("command")

