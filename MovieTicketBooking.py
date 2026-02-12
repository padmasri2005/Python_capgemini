import logging

logging.basicConfig(
    filename="Movie.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MovieTicket:

    ticket_price = 200
    booked_users = []

    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no
        self.numSeats = 0


    def book_seat(self, movie_name, theatre, numSeats):

        if self.phone_no in MovieTicket.booked_users:
            logging.warning("User already booked tickets")
            return

        MovieTicket.booked_users.append(self.phone_no)
        self.numSeats = numSeats
        logging.info("Seats booked successfully for %s", movie_name)

    def cancel_booking(self):

        if self.phone_no not in MovieTicket.booked_users:
            logging.warning("No booking found for user")
            return

        MovieTicket.booked_users.remove(self.phone_no)
        logging.info("Booking cancelled successfully")

    def calculate_ticket_price(self):

        if self.phone_no not in MovieTicket.booked_users:
            logging.warning("No tickets booked yet")
            return

        amount = MovieTicket.ticket_price * self.numSeats
        logging.info("Total Ticket Price : %d", amount)


    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        logging.info("Ticket price updated to : %d", cls.ticket_price)


m1 = MovieTicket("Padma", 9876543210)
m1.book_seat("Kalki", "PVR", 3)
m1.calculate_ticket_price()

m2 = MovieTicket("Ravi", 9123456780)
m2.book_seat("Pushpa", "INOX", 2)
m2.cancel_booking()

m1.update_ticket_price(350)
m1.calculate_ticket_price()
