from order_service import Order_Service
from order_burger import Order_Burger
from order_pizza import Order_Pizza
import random


class Main:

    if __name__ == "__main__":

        # Create order service with number of threads to use in first argument of
        # Order_Service
        service = Order_Service(2)

        # Factory for burgers
        burger_menu = ["Double with cheese", "Maple Bacon", "Chicken Crispy"]
        order_burger = Order_Burger()
        for i in range(2):
            order = order_burger.create_order(burger_menu[random.randrange(0, 3)], i)
            service.add_order(order)

        # Factory for pizzas
        pizza_menu = ["Pepperoni Pizza", "Triple Cheese", "Veggie Pizza"]
        order_pizza = Order_Pizza()
        for i in range(2):
            order = order_pizza.create_order(pizza_menu[random.randrange(0, 3)], i)
            service.add_order(order)

        # Process orders

        service.process_order()
