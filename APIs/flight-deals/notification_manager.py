import smtplib
import os

MY_EMAIL = os.environ.get("PERSONAL_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")

class NotificationManager():
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self, price, source, from_airport, destination, to_airport):
        self.price = price
        self.source = source
        self.destination = destination
        self.from_airport = from_airport
        self.to_airport = to_airport

    def send_email(self):
        """
        This method sends an email with notifications on latest flightdeal
        """
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, EMAIL_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= RECIPIENT,
                msg=f"Subject: Low Price Alert!\n\nOnly {self.price} to fly from {self.source}-{self.from_airport} to {self.destination}-{self.to_airport}"
            )
