import tkinter as tk
import tkinter.font as tkFont
"""
Class: Delete_account_view

This class represents the GUI window for deleting the user's account.

Methods:
- setup(self): Sets up the GUI elements and layout.
- delete_account(self): Deletes the user's account.
- move_back(self): Closes the current window.

Attributes:
- app: An instance of the main application.
"""
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
        self.configure(bg="lightblue")

        self.label_heading=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=23)
        self.label_heading["font"] = ft
        self.label_heading["fg"] = "#333333"
        self.label_heading["justify"] = "center"
        self.label_heading["text"] = "Delete Account"
        self.label_heading.place(x=0, y=0, width=500, height=100)

        self.label_text=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=18)
        self.label_text["font"] = ft
        self.label_text["fg"] = "#333333"
        self.label_text["justify"] = "center"
        self.label_text["text"] = "Are you sure you want to delete this account?"
        self.label_text.place(x=0, y=90, width=500, height=100)

        self.button_yes=tk.Button(self)
        self.button_yes["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times',size=10)
        self.button_yes["font"] = ft
        self.button_yes["fg"] = "#000000"
        self.button_yes["justify"] = "center"
        self.button_yes["text"] = "YES"
        self.button_yes.place(x=120, y=220, width=100, height=70)
        self.button_yes["command"] = self.delete_account

        self.button_no=tk.Button(self)
        self.button_no["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times',size=10)
        self.button_no["font"] = ft
        self.button_no["fg"] = "#000000"
        self.button_no["justify"] = "center"
        self.button_no["text"] = "NO"
        self.button_no.place(x=290, y=220, width=100, height=70)
        self.button_no["command"] = self.move_back

    def delete_account(self):
        if self.master.app.delete_account():
            self.destroy()
            self.app.destroy()
            self.master.deiconify()


    def move_back(self):
        self.destroy()
