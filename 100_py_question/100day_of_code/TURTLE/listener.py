from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_bakward():
    turtle.backward(10)

def t_left():
    turtle.left(5)

def t_right():
    turtle.right(5)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_bakward, "s")
screen.onkey(t_left, "a")
screen.onkey(t_right, "d")
screen.onkey(turtle.clear, "c")
screen.exitonclick()