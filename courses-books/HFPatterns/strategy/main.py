'''
Паттерн Стратегия определяет семейство ал-
горитмов, инкапсулирует каждый из них и обе-
спечивает их взаимозаменяемость. Он позво-
ляет модифицировать алгоритмы независимо
от их использования на стороне клиента.


Единственная константа в программировании - ИЗМЕНЕНИЯ!

Выделите аспекты приложения, которые
могут изменяться, и отделите их от тех,
которые всегда остаются постоянными.
'''

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
