from abc import ABC, abstractmethod

# PizzaStore(abstract) - Factory(Creator)
# NYPizzaStore/ChicagoPizzaStore - Concrete Factory(Creator)
# Pizza(abstract) - Product
# NYStyleCheesePizza/ChicagoStyleCheesePizza - Concreate Product
# create_pizza() - Factory method


class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass
    
    # Change to abstract when adding ingredients factory
    # def prepare(self):
    #     print(f"Preparing {self.name}")
    #     print("Tossing dough...")
    #     print("Adding sauce...")
    #     print("Adding toppings:")
    #     for topping in self.toppings:
    #         print(f"  {topping}")

    def bake(self):
        print("Bake for 25 minutes at 350°F")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Placing pizza in official PizzaStore box")

    def get_name(self):
        return self.name


# Abstract Creator
class PizzaStore(ABC):
    # order_pizza dont know with what object it works
    # concreate produt creates in subclasses
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type) 
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    # factory method, decide which pizza to create
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass  # This will be implemented by subclasses


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass
