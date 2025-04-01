from abstract import PizzaStore, Pizza

'''
# Simple factory just create new pizza objects
class SimplePizzaFactory:
    @classmethod
    def create_pizza(self, type):
        if type == 'cheese'
            pizza = CheesePizza()
        if type == 'pepperoni'
            pizza = PepperoniPizza()
        if type == 'clam'
            pizza = ClamPizza()
        return pizza
'''


# Concrete Product: NY Style Pizza
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")

class NYStylePepperoniPizza(Pizza):
    ...

class NYStyleClamPizza(Pizza):
    ...

# Concrete Product: Chicago Style Pizza
class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
    ...

class ChicagoStyleClamPizza(Pizza):
    ...

# Concrete Creator: NY Pizza Store
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        else:
            return None

# Concrete Creator: Chicago Pizza Store
class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        else:
            return None