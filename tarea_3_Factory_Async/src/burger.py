from order import Order
import time

class Burger(Order):

    # Builder for Burger, from Order parent
    def __init__(self, name, order_id):
        super().__init__(name, order_id)

    # Prepare Burger
    def cook(self):
        time.sleep(0.1)
        return f"Burger {self.order_id} prepared ({self.name})" 
    
    # Get the type of order
    def get_type(self):
        return f"Burger: {self.name}"
    
