# Tarea 3 | Javier Cruz - C02517

## [Repository link](https://github.com/ibra0610/c02517-diseno-software/tree/main/tarea_3_Factory_Async)

This project implements a concurrent food ordering system that uses the Factory Method Pattern to create different types of food orders.

## Factory Pattern
(From: [Refactoring Guru - Factory Method](https://refactoring.guru/design-patterns/factory-method))

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass. 
The Factory Method pattern suggests that you replace direct object construction calls with calls to a special *factory* method. Objects returned by a factory method are often referred to as *products*.

## Project Design

#### Creation of *Order* class

```python
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
```
This class defines the structure for food orders (parent, food inherits from this class).

#### Creation of Products (Food)

```python
class Burger(Order):

    # Builder for Burger, from Order parent
    def __init__(self, name, order_id):
        super().__init__(name, order_id)

    # Prepare Burger
    def cook(self):
        time.sleep(0.1)
        return f"Burger {self.order_id} prepared ({self.name})" 
    
    # Get the type of order
    def get_type(self):
        return f"Burger: {self.name}"
```

This is an example of food (order), new food items follow the same structure, inheriting from the Order class. 
These are the __*products*__ that __*factory*__ creates, as reviewed in the design pattern. 

#### Creation of Order_Manager (Abstract Creator)

```python
class Order_Manager:

    # Builder for Order Manager
    def __init__(self):
        pass
    
    # Creates order to cook, returns an order using it's ID
    def create_order(self, name, order_id) -> Order:
        pass
```

This class defines the factory method that subclasses implement. It returns the abstract __*product*__, not the specific variation. 

#### Creation of Order Product (Product creators)

```python
class Order_Burger(Order_Manager):

    # Builder for Order Burger class
    def __init__(self):
        super().__init__()

    # Creates a Burger order
    def create_order(self, name, order_id):
        return Burger(name, order_id)
``` 

This is an example of a product creator, the type of product may vary. Each __*factory*__ creates one type of __*product*__.

#### Project concurrency

- __*Factories*__ create orders that are added to a thread-safe queue.
- *Cook* threads can process orders without specifying their type.
