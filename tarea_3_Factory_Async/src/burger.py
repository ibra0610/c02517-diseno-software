from order import Order

class Burger(Order):

    def __init__(self, name, order_id):
        super().__init__(name, order_id)


    def cook(self):
        return f"Preparing order {self.order_id} (Burger)" 
    
