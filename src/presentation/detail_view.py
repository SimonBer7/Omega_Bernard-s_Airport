import tkinter as tk
import tkinter.font as tkFont
"""
Class: Detail_view

This class represents the GUI window for displaying details of a reservation.

Methods:
- setup(self): Sets up the GUI elements and layout.
- close_win(self): Closes the current window.

Attributes:
- app: An instance of the main application.
- reservation: Details of the reservation.
"""
class Detail_view(tk.Toplevel):
    def __init__(self, master, app, reservation):
        super().__init__(master)
        self.app = app
        self.reservation = reservation
        self.setup()

    def setup(self):
        #setting title
        self.title("Bernard's Airport")
        #setting window size
        width=800
        height=700
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
        self.label_heading["text"] = "Reservation - "+str(self.reservation[0][0])
        self.label_heading.place(x=210, y=10, width=300, height=100)

        self.label_passenger=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_passenger["font"] = ft
        self.label_passenger["fg"] = "#333333"
        self.label_passenger["anchor"] = "center"
        self.label_passenger["text"] = "Passenger: "
        self.label_passenger.place(x=110, y=110, width=200, height=50)

        self.label_destination=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_destination["font"] = ft
        self.label_destination["fg"] = "#333333"
        self.label_destination["anchor"] = "center"
        self.label_destination["text"] = "Destination:"
        self.label_destination.place(x=110, y=170, width=200, height=50)

        self.label_city=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_city["font"] = ft
        self.label_city["fg"] = "#333333"
        self.label_city["anchor"] = "center"
        self.label_city["text"] = "City:"
        self.label_city.place(x=110, y=230, width=200, height=50)

        self.label_temperature=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_temperature["font"] = ft
        self.label_temperature["fg"] = "#333333"
        self.label_temperature["anchor"] = "center"
        self.label_temperature["text"] = "Average temperature:"
        self.label_temperature.place(x=110, y=290, width=200, height=50)

        self.label_plane=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_plane["font"] = ft
        self.label_plane["fg"] = "#333333"
        self.label_plane["anchor"] = "center"
        self.label_plane["text"] = "Plane:"
        self.label_plane.place(x=110, y=350, width=200, height=50)

        self.label_pilot=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_pilot["font"] = ft
        self.label_pilot["fg"] = "#333333"
        self.label_pilot["anchor"] = "center"
        self.label_pilot["text"] = "Pilot:"
        self.label_pilot.place(x=110, y=410, width=200, height=50)

        self.label_from=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_from["font"] = ft
        self.label_from["fg"] = "#333333"
        self.label_from["anchor"] = "center"
        self.label_from["text"] = "From:"
        self.label_from.place(x=110, y=470, width=100, height=50)

        self.label_to=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_to["font"] = ft
        self.label_to["fg"] = "#333333"
        self.label_to["anchor"] = "center"
        self.label_to["text"] = "To:"
        self.label_to.place(x=400, y=470, width=100, height=50)

        self.label_price=tk.Label(self, bg="lightblue")
        ft = tkFont.Font(family='Times',size=16)
        self.label_price["font"] = ft
        self.label_price["fg"] = "#333333"
        self.label_price["anchor"] = "center"
        self.label_price["text"] = "Price:"
        self.label_price.place(x=110, y=530, width=200, height=50)

        self.button_back=tk.Button(self)
        self.button_back["bg"] = "lightcoral"
        ft = tkFont.Font(family='Times',size=16)
        self.button_back["font"] = ft
        self.button_back["fg"] = "#000000"
        self.button_back["justify"] = "center"
        self.button_back["text"] = "Back"
        self.button_back.place(x=610, y=580, width=150, height=80)
        self.button_back["command"] = self.close_win

        def create_message(parent, text, x, y, width, height):
            message = tk.Message(parent, bg="lightblue", font=("Times", 16), fg="#333333", text=text,
                                 aspect=False, width=width)
            message.place(x=x, y=y, width=width, height=height)
            return message

        message_y_positions = [110, 170, 230, 290, 350, 410, 470, 470, 530]
        message_height = 50
        for i, data in enumerate(self.reservation[0][1:]):
            if i == 6:
                create_message(self, data, 180, message_y_positions[i], 200, message_height)
            elif i == 7:
                create_message(self, data, 480, message_y_positions[i], 200, message_height)
            elif i == 8:
                create_message(self, data, 0, 620, 400, message_height)
            elif i == 9:
                create_message(self, data, 280, message_y_positions[8], 200, message_height)
            else:
                create_message(self, data, 310, message_y_positions[i], 400, message_height)


    def close_win(self):
        self.destroy()
