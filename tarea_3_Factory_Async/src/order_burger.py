from order_manager import Order_Manager
from burger import Burger

class Order_Burger(Order_Manager):

    # Builder for Order Burger class
    def __init__(self):
        super().__init__()

    # Creates a Burger order
    def create_order(self, name, order_id):
        return Burger(name, order_id)