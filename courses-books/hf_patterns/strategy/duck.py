# Separate all that can changes(behavior, fiatures) from duck
# and create interfase to update what stay saim
# - Incapsulate changes
# - composition better then ierarhy
# - program on interfase not on realization

'''
Мы знаем, что fly() и quack() — части класса Duck,
изменяющиеся в зависимости от субкласса.
Чтобы отделить эти аспекты поведения от класса Duck, мы
выносим оба метода за пределы класса Duck и создаем новый
набор классов для представления каждого аспекта.
'''

from behavior import *


class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def display(self):
        pass
    
    '''
    изменять поведение во время выполнения — при
    условии, что объект, подключенный посредством компо-
    зиции, реализует правильный интерфейс.
    '''
    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior
