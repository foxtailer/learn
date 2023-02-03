import turtle
import random

screen = turtle.Screen()
screen.setup(400, 400)
tur = turtle.Turtle()
tur.shape("turtle")
tur.stamp()
tur.speed(10)

class Point:
    def __init__(self) -> None:
        self.x = random.randint(-200, 200)
        self.y = random.randint(-200, 200)

bag = []
for _ in range(1000):
    bag.append(Point())

for point in bag:
    match point:
        case point.x, point.y if abs(point.x) == abs(point.y):
            tur.penup()
            tur.color("red")
            tur.goto(point.x, point.y)
            tur.stamp()
        case _:
            tur.penup()
            tur.color("green")
            tur.goto(point.x, point.y)
            tur.stamp()
    

turtle.mainloop()