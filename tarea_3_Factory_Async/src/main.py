from order_service import Order_Service
from order_burger import Order_Burger
from order_pizza import Order_Pizza

class Main:

    if __name__ == "__main__":

        # Create order service with number of threads to use in first argument of
        # Order_Service
        service = Order_Service(2)

        # Factory for burgers
        order_burger = Order_Burger()
        for i in range(3):
            order = order_burger.create_order("Triple with cheese", i)
            service.add_order(order)

        # Factory for pizzas
        order_pizza = Order_Pizza()
        for i in range(3):
            order = order_pizza.create_order("Pepperoni Pizza", i)
            service.add_order(order)

        # Process orders
        
        service.process_order()
