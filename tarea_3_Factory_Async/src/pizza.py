from order import Order

class Pizza(Order):

    # Builder for Pizza, from Order parent
    def __init__(self, name, order_id):
        super().__init__(name, order_id)

    # Prepare Pizza
    def cook(self):
        return f"Preparing order {self.order_id} (Pizza)"
    
    # Get the type of order
    def get_type(self):
        return "Pizza"
