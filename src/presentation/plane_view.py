import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from src.presentation.add_plane import Add_plane_view
from src.presentation.error_view import Error_view
from src.presentation.success_view import Success_view
from src.logic.log_writter import Log_writter
"""
    Class representing the GUI window for managing planes.

    Attributes:
        app: An instance of the main application.
        planes: List of planes.
        log_writter: Instance of Log_writer for logging.

    Methods:
        setup(self): Sets up the GUI elements and layout.
        create_plane(self): Opens the window to add a new plane.
        delete_plane(self): Deletes the selected plane.
        move_back(self): Closes the current window and moves back to the previous window.
    """
class Plane_view(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.planes = self.master.app.load_planes()
        self.log_writter = Log_writter()
        self.setup()

    def setup(self):
        # setting title
        self.title("Bernard's Airport - Planes")
        # setting window size
        width = 1500
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.configure(bg="lightblue")

        self.label_heading = tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times', size=28)
        self.label_heading["font"] = ft
        self.label_heading["fg"] = "#333333"
        self.label_heading["justify"] = "center"
        self.label_heading["text"] = "Planes"
        self.label_heading.place(x=600, y=40, width=300, height=100)

        self.flight_frame = ttk.Frame(self)
        self.flight_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.flight_tree = ttk.Treeview(self.flight_frame, columns=("Type", "Capacity", "Active"))
        self.flight_tree.heading("#0", text="Name")
        self.flight_tree.heading("Type", text="Type")
        self.flight_tree.heading("Capacity", text="Capacity")
        self.flight_tree.heading("Active", text="Active")

        for plane in self.planes:
            self.flight_tree.insert("", "end", text=plane[0],
                                    values=(plane[1], plane[2], plane[3]))

        self.flight_tree.pack(expand=True, fill=tk.BOTH)

        self.delete_button = tk.Button(self)
        self.delete_button["bg"] = "tomato"
        ft = tkFont.Font(family='Times', size=18)
        self.delete_button["font"] = ft
        self.delete_button["fg"] = "#000000"
        self.delete_button["justify"] = "center"
        self.delete_button["text"] = "Delete"
        self.delete_button.place(x=800, y=490, width=200, height=80)
        self.delete_button["command"] = self.delete_plane

        self.create_button = tk.Button(self)
        self.create_button["bg"] = "lightgreen"
        ft = tkFont.Font(family='Times', size=18)
        self.create_button["font"] = ft
        self.create_button["fg"] = "#000000"
        self.create_button["justify"] = "center"
        self.create_button["text"] = "Create"
        self.create_button.place(x=500, y=490, width=200, height=80)
        self.create_button["command"] = self.create_plane

        self.back_button = tk.Button(self)
        self.back_button["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times', size=13)
        self.back_button["font"] = ft
        self.back_button["fg"] = "#000000"
        self.back_button["justify"] = "center"
        self.back_button["text"] = "Back"
        self.back_button.place(x=1300, y=570, width=100, height=70)
        self.back_button["command"] = self.move_back

    def create_plane(self):
        add_plane = Add_plane_view(self.master, self)
        add_plane.deiconify()
        self.destroy()

    def delete_plane(self):
        selected_items = self.flight_tree.selection()
        if len(selected_items) == 1:
            values = self.flight_tree.item(selected_items)['text']
            if values:
                if self.master.app.plane_dao.delete(values):
                    self.destroy()
                    succes = Success_view(self.master, self)
                    succes.deiconify()
                else:
                    error = Error_view(self.master, self)
                    error.deiconify()
            else:
                self.log_writter.write_to_log("Error with deleting plane")
                error = Error_view(self.master, self)
                error.deiconify()
        elif len(selected_items) > 1:
            self.log_writter.write_to_log("Only one plane should be selected")
            error = Error_view(self.master, self)
            error.deiconify()
        else:
            self.log_writter.write_to_log("No plane selected")
            error = Error_view(self.master, self)
            error.deiconify()

    def move_back(self):
        self.destroy()
