from abc import ABC, abstractmethod

# Enum for sizes
class Size:
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

# Abstract base class for beverages
class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"
        self.size = Size.SMALL  # Default size is Small

    def get_description(self):
        return self.description

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    @abstractmethod
    def cost(self):
        pass


# Abstract base class for condiment decorators
class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_size(self):
        return self.beverage.get_size()

    @abstractmethod
    def get_description(self):
        pass
