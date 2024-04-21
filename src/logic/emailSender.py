"""
Class: EmailSender

This class is responsible for sending reservation confirmation emails to passengers.
It generates the email content based on reservation details and sends it using the SMTP protocol.

Attributes:
- subject (str): The subject of the email.
- body (str): The body content of the email.
- sender_email (str): The email address of the sender.
- sender_password (str): The password of the sender's email account.

Methods:
- set_values(self, data): Sets the values of the email attributes based on reservation data.
- send_reservation_email(self, user): Sends a reservation confirmation email to the specified user.
"""

import smtplib
from email.mime.text import MIMEText

class EmailSender:
    """
    Class responsible for sending reservation confirmation emails to passengers.
    """

    def __init__(self, data):
        """
        Initializes a new EmailSender object.

        Parameters:
        - data (list): Reservation data used to populate the email content.
        """
        self.subject = None
        self.body = None
        self.sender_email = None
        self.sender_password = None
        self.set_values(data)

    def set_values(self, data):
        """
        Sets the values of the email attributes based on reservation data.

        Parameters:
        - data (list): Reservation data used to populate the email content.
        """
        self.subject = "Bernard's Airport - Reservation " + str(data[0][0])
        self.sender_email = "bernardairport@gmail.com"
        self.sender_password = "knde fywr viky yrex"
        self.body = f"""Dear Passenger {data[0][1]},

We hope this message finds you well. Thank you for choosing Bernard's Airport for your travel needs.

Your reservation details are as follows:
- Reservation ID: {data[0][0]}
- Destination: {data[0][2]}
- City: {data[0][3]}
- Temperature: {data[0][4]}
- Plane: {data[0][5]}
- Pilot: {data[0][6]}
- Date of leaving: {data[0][7]}
- Date of arriving: {data[0][8]}
- Date of reservation: {data[0][9]}
- Price: {data[0][10]} KC

We are committed to providing you with a seamless and enjoyable airport experience. Our dedicated team is working hard to ensure that your journey with us is comfortable and stress-free.

If you have any specific requests or questions regarding your reservation, please feel free to reach out to our customer service team at bernardairport@gmail.com. We are here to assist you in any way we can.

Once again, thank you for choosing Bernard's Airport. We look forward to welcoming you at the airport and wish you a pleasant and safe journey.

Safe travels!

Sincerely,
Bernard's Airport
"""

    def send_reservation_email(self, user):
        """
        Sends a reservation confirmation email to the specified user.

        Parameters:
        - user (Passenger): The passenger object representing the recipient of the email.
        """
        msg = MIMEText(self.body)
        msg["Subject"] = self.subject
        msg["From"] = self.sender_email
        msg["To"] = user.email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, msg["To"], msg.as_string())
