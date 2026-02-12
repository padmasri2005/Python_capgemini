import logging

logging.basicConfig(
    filename="Hotel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HotelRoom:

    room_rent_per_day = 2500
    active_customers = []

    def __init__(self, customer_name, phone_no):
        self.customer_name = customer_name
        self.phone_no = phone_no
        self.days = 0

    def allocate_room(self, room_no, days):
        if self.phone_no in HotelRoom.active_customers:
            logging.warning("Customer already checked in")
            return

        HotelRoom.active_customers.append(self.phone_no)
        self.days = days
        logging.info("Room %d allocated to %s", room_no, self.customer_name)

    def vacate_room(self):
        if self.phone_no not in HotelRoom.active_customers:
            logging.warning("Customer has no active booking")
            return

        HotelRoom.active_customers.remove(self.phone_no)
        logging.info("Room vacated by %s", self.customer_name)

    def calculate_bill(self):
        if self.phone_no not in HotelRoom.active_customers:
            logging.warning("No active stay found")
            return

        total = HotelRoom.room_rent_per_day * self.days
        logging.info("Total bill for %s : %d", self.customer_name, total)

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent_per_day = new_rent
        logging.info("Room rent updated to : %d", cls.room_rent_per_day)


c1 = HotelRoom("Padmasri", 9876543210)
c1.allocate_room(101, 3)
c1.calculate_bill()

c2 = HotelRoom("Ravi", 9123456780)
c2.allocate_room(202, 2)
c2.vacate_room()

c1.update_room_rent(3000)
c1.calculate_bill()
