from concreat import *


# Client Code (Test)
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"\nEthan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"\nJoel ordered a {pizza.get_name()}\n")

'''
The Factory Method pattern defines an interface for creating an object 
but allows subclasses to choose the class of the created instance. Thus, 
the Factory Method delegates the instantiation operation to subclasses.
'''