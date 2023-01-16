import turtle
import random

rgb_colors = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90)]
turtle.colormode(255)


class Car(turtle.Turtle):
    def __init__(self, fild) -> None:
        super().__init__()
        self.x_max = fild[0]/2
        self.x_min = -(fild[0]/2)
        self.y_max = fild[1]/2
        self.y_min = -(fild[1]/2)
        self.penup()
        #self.color(rgb_colors[random.randint(0, len(rgb_colors)-1)])
        self.color(random.choice(rgb_colors))
        self.shapesize(1,2)
        self.shape("square")
        self.setheading(180)
        self.goto(random.randint(self.x_max + 20, self.x_max + 700), random.randint(self.y_min-100, self.y_max+100))  # 40 it's a "save gone" at start and end runer position

    def move(self):
        self.forward(10)

    def restart(self):
        self.goto(random.randint(self.x_max + 20, self.x_max + 700), random.randint(self.y_min-100, self.y_max+100))  # 40 it's a "save gone" at start and end runer position

