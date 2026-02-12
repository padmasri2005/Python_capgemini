import logging

logging.basicConfig(
    filename = "Railway.log",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
class Ticket:
    base_fare = 100
    passDetail= []
    def __init__(self,name,phone_no,aadhaar):
        self.pname = name
        self.phone_no = phone_no
        self.aadhaar = aadhaar
        self.numTickets = 0
        

    def book_ticket(self,from_add,to_add,numTickets):
        if self.aadhaar in Ticket.passDetail:
            # print("You already booked Tickets")
            logging.warning("You already booked Tickets")
            return
        
        Ticket.passDetail.append(self.aadhaar)
        self.numTickets = numTickets
        logging.info("Tickets booked successfully")
        # print("Tickets booked successfully")

    def cancel_ticket(self):
        if self.aadhaar not in Ticket.passDetail:
            # print("No Tickets are booked on your name")
            logging.warning("No Tickets are booked on your name")
            return
        Ticket.passDetail.remove(self.aadhaar)
        # print("Tickets cancelled successfully")
        logging.info("Tickets cancelled successfully")

    def calculate_fare(self):
        if self.aadhaar not in Ticket.passDetail:
            # print("No Tickets booked yet..")
            logging.warning("No Tickets booked yet..")
            return
        amount = Ticket.base_fare * self.numTickets

        # print("Total Fare : ",amount)
        logging.info("Total Fare : %d ",amount)

    @classmethod
    def update_base_fare(cls,new_fare):
        cls.base_fare = new_fare
        # print("Base Fare : ",cls.base_fare)
        logging.info("Base Fare : %d",cls.base_fare)

p1 = Ticket("Srinitha",7418529630,789654123369)
p1.book_ticket("HYD","DELHI",4)
p1.calculate_fare()

p2 = Ticket("Rammu",1234569877,123654789012)
p2.book_ticket("BANG","GOA",10)
p2.cancel_ticket()
p1.update_base_fare(500)