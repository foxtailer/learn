from turtle import Turtle, Screen
import random
import math

rotate = [90, 180, 0, 270]
rotate_2 = [0, 45, 90, 135, 180, 225, 270, 315, 360]
_colors = ["deep sky blue","spring green","pale green","salmon","medium purple", "saddle brown", "dark green", "red"]

def rand_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

class Stroll:
    def __init__(self, angls, colors, amount) -> None:
        self.angls = angls
        self.colors = colors
        self.wolkers = []
        for i in range(amount):
            self.wolkers.append(Turtle())
        for wolker in self.wolkers:
            wolker.width(7)
            wolker.speed(0)

    def wolk(self):
        while True:
            for wolker in self.wolkers:
                wolker.color(random.choice(self.colors))
                wolker.setheading(random.choice(self.angls))
                if wolker.heading() == 45 or wolker.heading() == 135 or wolker.heading() == 225 or wolker.heading() == 315:
                    wolker.forward(math.sqrt(35**2 + 35**2))
                else:
                    wolker.forward(35)

stroll = Stroll(rotate_2, _colors, 10)
stroll.wolk()

screen = Screen()
screen.exitonclick()