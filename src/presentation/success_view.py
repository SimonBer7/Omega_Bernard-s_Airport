import tkinter as tk
import tkinter.font as tkFont

"""
   Class representing the GUI window for displaying success messages.

   Methods:
       setup(self): Sets up the GUI elements and layout.
   """
class Success_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.setup()

    def setup(self):
        #setting title
        self.title("Success")
        #setting window size
        width=300
        height=300
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightgreen")

        self.text=tk.Label(self, bg="lightgreen")
        ft = tkFont.Font(family='Times',size=48)
        self.text["font"] = ft
        self.text["fg"] = "#333333"
        self.text["justify"] = "center"
        self.text["text"] = "Success"
        self.text.place(x=0, y=0, width=300, height=300)

        # Bind the Escape key to close the window
        self.bind("<Escape>", lambda event: self.destroy())

        # Make the window modal
        self.grab_set()
