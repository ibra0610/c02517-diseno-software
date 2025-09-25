class Order:

    # Builder for Order class
    def __init__(self, name, order_id):
        self.name = name
        self.order_id = order_id

    # Prepare ordered food
    def cook(self):
        pass

    # Get the type of order
    def get_type(self):
        pass
