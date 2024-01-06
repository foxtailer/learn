from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def say_something(self):
        raise NotImplemented

class Cat(Animal):
    def say_something(self):
        print("Mrrr")

c = Cat()