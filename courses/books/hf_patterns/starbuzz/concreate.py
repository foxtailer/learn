from abstract import Beverage, CondimentDecorator


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
        return self.beverage.cost() + 0.20


class Chocolate(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + ", Chocolate"

    def cost(self):
        return self.beverage.cost() + 0.1
