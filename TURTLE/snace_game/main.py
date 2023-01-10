from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

x = Snake()
while True:
    x.move()
    screen.update()
    time.sleep(0.2)



screen.exitonclick()