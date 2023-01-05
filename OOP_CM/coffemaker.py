class CoffeMaker():
    def __init__(self) -> None:
        self.ingredients = {"water" : 2000,
                            "coffe" : 500,
                            "milk" : 1000
        }
    
    def report(self):
        print(f"Water: {self.ingredients['water']}")        
        print(f"Coffe: {self.ingredients['coffe']}")
        print(f"Milk: {self.ingredients['milk']}")

    def is_resource_sufficient(self, drink):
        result = True
        for ingredient in self.ingredients:
            if self.ingredients[ingredient] < drink.ingredients[ingredient]:
                result = False
                print(f"Not enouf {ingredient.capitalize()}")
        return result
        

    def make_coffee(self, order):
        for ingredient in order.ingredients:
            self.ingredients[ingredient] -= order.ingredients[ingredient]
