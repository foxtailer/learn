from turtle import Turtle, Screen

turtle = Turtle()

def dash_line(lenght, dot_amount):
    for _ in range(dot_amount):
        turtle.forward(lenght)
        turtle.penup()
        turtle.forward(lenght)
        turtle.pendown()

dash_line(10, 10)
screen = Screen()
screen.exitonclick()