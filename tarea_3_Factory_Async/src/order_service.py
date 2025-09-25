import queue
import threading
from order import Order
from cook import Cook


class Order_Service:

    # Builder for Order Service class
    def __init__(self, number_of_cooks):
        self.order_queue = queue.Queue()  # Queue for threads
        self.orders = []
        self.number_of_cooks = number_of_cooks
        self.lock = threading.Lock()  # To make sure results are printed in order
        self.cooks_list = []

    # Adds order to the queue
    def add_order(self, order):
        self.orders.append(order)
        self.order_queue.put(order)

    # Process orders using threads
    def process_order(self):
        # If there are no items in the orders queue
        if not self.orders:
            print("[SYSTEM] No orders to process")
            return

        # Create cook threads
        for i in range(self.number_of_cooks):
            cook = Cook(f"COOK {i + 1}", self.order_queue, self.lock)
            self.cooks_list.append(cook)
            cook.start()

        # Wait for orders to be processed
        self.order_queue.join()

        # Wait for threads to finish
        for cook in self.cooks_list:
            cook.join(timeout=0.1)

        # Confirms all orders have been processed
        print("[SYSTEM] All orders have been processed")
