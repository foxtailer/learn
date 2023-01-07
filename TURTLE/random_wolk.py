from turtle import Turtle, Screen
import random
turtle = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle.pensize(7)
turtle2.pensize(7)
turtle3.pensize(7)
turtle.speed(0)
turtle2.speed(0)
turtle3.speed(0)
rotate = [90, 180, 0, 270]
colors = ["deep sky blue","spring green","pale green","salmon","medium purple", "saddle brown", "dark green", "red"]

while True:
    turtle.color(random.choice(colors))
    turtle.forward(35)
    #turtle.left(random.choice(rotate))
    turtle.setheading(random.choice(rotate))

    turtle2.color(random.choice(colors))
    turtle2.forward(35)
    #turtle.left(random.choice(rotate))
    turtle2.setheading(random.choice(rotate))

    turtle3.color(random.choice(colors))
    turtle3.forward(35)
    #turtle.left(random.choice(rotate))
    turtle3.setheading(random.choice(rotate))

screen = Screen()
screen.exitonclick()