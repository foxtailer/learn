import sys
import random


folder = '/home/zoy/vscode/learn/courses/Python Tutorial'
if folder not in sys.path:
    sys.path.append(folder)

from decorators_pycon import trace


GREETINGS = ['Heisann', 'Hi there', 'Ni!']


@trace
def greet(name, greeting='Hello'):
    return f'{greeting} {name}'


@trace
def random_greet(name='Emely'):
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)


@trace
def greet_many(number):
    return [random_greet() for _ in range(number)]


print(greet('Fedor', greeting='Aloha!'))
print('\n\n')
print(greet_many(4))
