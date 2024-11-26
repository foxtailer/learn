from duck import Duck
from behavior import *


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I’m a Mallard Duck")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())

    def display(self):
        print("I’m a model duck")


def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()

    print("\n")

    model = ModelDuck()
    model.display()
    model.perform_fly()
    
    # Меняем поведение модели на реактивное
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    mini_duck_simulator()
