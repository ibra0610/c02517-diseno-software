from order import Order

class Pizza(Order):

    def __init__(self, name, order_id):
        super().__init__(name, order_id)

