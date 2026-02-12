import logging

logging.basicConfig(
    filename="Order.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

class Order:
    tax_percentage = 5    
    def __init__(self,name,phone_no,address):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.items = {}
    def place_order(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name][0]+=quantity
            return

        self.items[item_name] = [quantity, price]

        # print("Order Placed Successfully")
        logging.info("Dear %s ,Order placed Successfully",self.name)

    def cancel_order(self,item_name):
        if item_name not in self.items:
            logging.warning("No Order is placed related to %s", item_name)
            return

        # if self.items[item_name][0] == 0:
        del self.items[item_name]
           
        # print("Order cancelled successfully")
        logging.info("Dear %s ,Order cancelled Successfully",self.name)

    def total_price(self):
        amount = 0
        for item in self.items.values():
            sub = item[0] * item[1]
            amount += sub

        # print("Total Amount :",amount)
        logging.info("Total Amount : %d",amount)

    @classmethod
    def update_tax_percentage(cls,new_tax_perc):
        cls.tax_percentage = new_tax_perc
        logging.info("Tax Percentage is updated to : %d",cls.tax_percentage)

o1 = Order("Padma Sri",7396428888,"Miyapur,Hyderabad")
o2 = Order("Rajani",7410258963,"Rama Murthy Nagar,Banglore")
o3 = Order("Nagamani",8105907223,"Sanagareddy,Delhi")

o1.place_order("FaceWash",1,500)
o2.place_order("Watter Bottle",3,900)
o2.place_order("Bag",1,15000)

o2.total_price()

o2.cancel_order("Ring")
o2.cancel_order("Bag")
o2.total_price()

o3.update_tax_percentage(7)
        