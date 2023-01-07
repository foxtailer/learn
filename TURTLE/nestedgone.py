from turtle import Turtle, Screen
import random
turtle = Turtle()
colors = ["deep sky blue","spring green","pale green","salmon","medium purple"]

def nestedgone(lenght, amount):
    sides = 3
    for i in range(amount):
        turtle.color(random.choice(colors))
        for i in range(sides):
            turtle.forward(lenght)
            turtle.right(360/sides)
        sides += 1


nestedgone(100, 10)
screen = Screen()
screen.exitonclick()