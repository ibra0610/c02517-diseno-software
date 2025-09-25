from order import Order
import time


class Pizza(Order):

    # Builder for Pizza, from Order parent
    def __init__(self, name, order_id):
        super().__init__(name, order_id)

    # Prepare Pizza
    def cook(self):
        time.sleep(0.1)
        return f"Pizza {self.order_id} prepared ({self.name})"

    # Get the type of order
    def get_type(self):
        return f"Pizza: {self.name}"
