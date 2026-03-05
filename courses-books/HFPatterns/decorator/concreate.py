# classes should be open te extention and close to changes 

from abstract import Beverage, CondimentDecorator, Size


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89



class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        size = self.get_size()
        if size == Size.SMALL:
            return self.beverage.cost() + 0.10
        elif size == Size.MEDIUM:
            return self.beverage.cost() + 0.15
        elif size == Size.LARGE:
            return self.beverage.cost() + 0.20
        else:
            return self.beverage.cost()


class Chocolate(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + ", Chocolate"

    def cost(self):
        size = self.get_size()
        if size == Size.SMALL:
            return self.beverage.cost() + 0.10
        elif size == Size.MEDIUM:
            return self.beverage.cost() + 0.15
        elif size == Size.LARGE:
            return self.beverage.cost() + 0.20
        else:
            return self.beverage.cost()
