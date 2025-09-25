from order import Order

class Burger(Order):

    # Builder for Burger, from Order parent
    def __init__(self, name, order_id):
        super().__init__(name, order_id)

    # Prepare Burger
    def cook(self):
        return f"Preparing order {self.order_id} (Burger)" 
    
