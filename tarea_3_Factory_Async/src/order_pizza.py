from order_manager import Order_Manager
from pizza import Pizza


class Order_Pizza(Order_Manager):

    # Builder for Order Pizza class
    def __init__(self):
        super().__init__()

    # Creates a Pizza order
    def create_order(self, name, order_id):
        return Pizza(name, order_id)
