import threading
import queue
from order import Order


class Cook(threading.Thread):

    # Builder for cook class
    # daemon = True kills threads when the main program finishes
    def __init__(self, name, order_queue, lock):
        super().__init__()
        self.name = name
        self.order_queue = order_queue
        self.lock = lock
        self.daemon = True

    def run(self):
        while True:
            try:
                # Get an order from the queue
                order = self.order_queue.get(timeout=1)

                # Process food order
                with self.lock:
                    print(
                        f"[{self.name}] Preparing order {order.order_id} ({order.get_type()})"
                    )

                # Prepare the order
                result = order.cook()

                # Print confirmation order prepared
                with self.lock:
                    print(f"[{self.name}] Order {order.order_id} prepared: {result}")

                # Mark order as completed
                self.order_queue.task_done()

            # In case there are no more orders in queue
            except queue.Empty:
                break
