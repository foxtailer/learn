from abc import ABC, abstractmethod

# Abstract class for beverages
class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


# Abstract class for condiment decorators
class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass
