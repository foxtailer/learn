from turtle import Turtle, Screen
import random
import math

rotate = [90, 180, 0, 270]
rotate_2 = [0, 45, 90, 135, 180, 225, 270, 315, 360]


class Stroll:

    def __init__(self, angls, amount) -> None:
        self.angls = angls
        self.wolkers = []
        for i in range(amount):
            self.wolkers.append(Turtle())
        for wolker in self.wolkers:
            wolker.width(7)
            wolker.speed(0)

    def rand_color(self):
        return random.random(), random.random(), random.random()

    def wolk(self):
        while True:
            for wolker in self.wolkers:
                wolker.color(self.rand_color())
                wolker.setheading(random.choice(self.angls))
                if wolker.heading() == 45 or wolker.heading() == 135 or wolker.heading() == 225 or wolker.heading() == 315:
                    wolker.forward(math.sqrt(35**2 + 35**2))
                else:
                    wolker.forward(35)

stroll = Stroll(rotate_2, 10)
stroll.wolk()

screen = Screen()
screen.exitonclick()