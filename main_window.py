import tkinter as tk
import tkinter.font as tkFont

class MainWindow:
    def __init__(self, app):
        self.app = app
        self.setup()

    def setup(self):
        #setting title
        self.app.root.title("Bernard's Airport")
        #setting window size
        width=800
        height=700
        screenwidth = self.app.root.winfo_screenwidth()
        screenheight = self.app.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.app.root.geometry(alignstr)
        self.app.root.resizable(width=False, height=False)

        GLabel_4=tk.Label(self.app.root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#333333"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "Welcome in Bernard's Airport let's book some flights"
        GLabel_4.place(x=40,y=100,width=700,height=50)

        GButton_130=tk.Button(self.app.root)
        GButton_130["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=23)
        GButton_130["font"] = ft
        GButton_130["fg"] = "#000000"
        GButton_130["justify"] = "center"
        GButton_130["text"] = "Log in"
        GButton_130.place(x=100,y=240,width=200,height=200)
        GButton_130["command"] = self.app.login

        GButton_778=tk.Button(self.app.root)
        GButton_778["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=23)
        GButton_778["font"] = ft
        GButton_778["fg"] = "#000000"
        GButton_778["justify"] = "center"
        GButton_778["text"] = "Sign up"
        GButton_778.place(x=500,y=240,width=200,height=200)
        GButton_778["command"] = self.app.signup
    def GButton_130_command(self):
        print("command")


    def GButton_778_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
