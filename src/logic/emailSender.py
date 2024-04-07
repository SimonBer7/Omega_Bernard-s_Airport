class EmailSender:
    """
    The EmailSender class represents an object responsible for sending reservation confirmation emails to passengers.

    ...

    Attributes
    ----------
    subject : str
        The subject of the email.
    body : str
        The body of the email.
    sender_email : str
        The email address from which the email is sent.
    sender_password : str
        The password associated with the sender's email address.

    Methods
    -------
    set_values(reservation, flight)
        Sets the values for the email subject, body, sender email, and sender password based on reservation and flight details.
    send_reservation_email(user)
        Sends a reservation confirmation email to the provided user.

    """

    def __init__(self, reservation, flight):
        """
        Initializes a new EmailSender object with initial attributes set to None.

        Parameters
        ----------
        reservation : Reservation
            The Reservation object for which the email is being sent.
        flight : Flight
            The Flight object associated with the reservation.
        """
        self.subject = None
        self.body = None
        self.sender_email = None
        self.sender_password = None
        self.set_values(reservation, flight)

    def set_values(self, reservation, flight):
        """
        Sets the values for the email subject, body, sender email, and sender password based on reservation and flight details.

        Parameters
        ----------
        reservation : Reservation
            The Reservation object for which the email is being sent.
        flight : Flight
            The Flight object associated with the reservation.
        """
        self.subject = "Bernard's Airport - Reservation " + str(reservation.pin)
        self.sender_email = "airportbernard@gmail.com"
        self.sender_password = "wyzm hzct ador fcps"
        self.body = f"""Dear Passenger,

We hope this message finds you well. Thank you for choosing Bernard's Airport for your travel needs.

Your reservation details are as follows:
- Reservation ID: {reservation.pin}
- Date of leaving: {flight.date_leaving}
- Date of arriving: {flight.date_arriving}
- Date of reservation: {reservation.date}
- Price: {reservation.price} KC

We are committed to providing you with a seamless and enjoyable airport experience. Our dedicated team is working hard to ensure that your journey with us is comfortable and stress-free.

If you have any specific requests or questions regarding your reservation, please feel free to reach out to our customer service team at airportbernard@gmail.com. We are here to assist you in any way we can.

Once again, thank you for choosing Bernard's Airport. We look forward to welcoming you on airport and wish you a pleasant and safe journey.

Safe travels!

Sincerely,
Bernard's Airport
"""

    def send_reservation_email(self, user):
        """
        Sends a reservation confirmation email to the provided user.

        Parameters
        ----------
        user : Passenger
            The Passenger object representing the user to whom the email will be sent.
        """
        msg = MIMEText(self.body)
        msg["Subject"] = self.subject
        msg["From"] = self.sender_email
        msg["To"] = user.email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, msg["To"], msg.as_string())
