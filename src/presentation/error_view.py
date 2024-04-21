import tkinter as tk
import tkinter.font as tkFont
"""
Class: Error_view

This class represents the GUI window for displaying error messages.

Methods:
- setup(self): Sets up the GUI elements and layout.

Attributes:
- app: An instance of the main application.
"""
class Error_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):
        #setting title
        self.title("Error")
        #setting window size
        width=300
        height=300
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="#c45843")

        self.text=tk.Label(self, bg="#c45843")
        ft = tkFont.Font(family='Times',size=48)
        self.text["font"] = ft
        self.text["fg"] = "#333333"
        self.text["justify"] = "center"
        self.text["text"] = "!!! Error !!!"
        self.text.place(x=0, y=0, width=300, height=300)

        # Bind the Escape key to close the window
        self.bind("<Escape>", lambda event: self.destroy())

        # Make the window modal
        self.grab_set()
