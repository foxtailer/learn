from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed(0)

for i in range(36):
    turtle.color(random.random(), random.random(), random.random())
    turtle.setheading(i * 10)
    turtle.circle(80)
screen = Screen()
screen.exitonclick()