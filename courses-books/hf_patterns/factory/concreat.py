from abstract import PizzaStore, Pizza, PizzaIngredientFactory

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
        elif pizza_type == '...':
            return CheasePizza(NYPizzaIngredientFactory())
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
        
############## Add ingredients facrory ############3#
''' We can get rid of regional types of piza
they prepare by the same methods but use diferent ingredients
'''

# Concrete ingredient classes (placeholders)
class ThinCrustDough(): pass
class MarinaraSauce(): pass
class ReggianoCheese(): pass
class Garlic(): pass
class Onion(): pass
class Mushroom(): pass
class RedPepper(): pass
class SlicedPepperoni(): pass
class FreshClams(): pass
# Chichago
class EggPlant(): pass
class BlackOlives(): pass
class FrozenClams(): pass
class ThickCrustDough(): pass
class PlumTomatoSauce(): pass
class MozzarellaCheese(): pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [EggPlant(), BlackOlives()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class CheasePizza():
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.name = "Chease pizza"
        self.dough = self.ingrediens_factory.create_dough()
        self.sauce = self.ingrediens_factory.create_sauce()
        self.toppings = [self.ingrediens_factory.create_cheese(),
                         self.ingrediens_factory.create_veggies()]