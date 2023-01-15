from turtle import Turtle, Screen
import random, time
from runer import Runer
from car import Car
from scorebord import ScoreBoard

SCREEN_X = 600
SCREEN_Y = 600
game_on = True
game_speed = 0.5

screen = Screen()
turtle = Runer()
scorebord = ScoreBoard((SCREEN_X, SCREEN_Y))

# Game screen settings
screen.tracer(0)
screen.setup(SCREEN_X, SCREEN_Y)
screen.title("Cross Game")
screen.listen()
screen.onkeypress(turtle.run, "Up")

cars = []
for _ in range(50):
    cars.append(Car(screen.screensize()))

# Turtle object settings
turtle.penup()
turtle.shape("turtle")
turtle.color("black")
turtle.setheading(90)
turtle.goto(0, -(SCREEN_Y/2-20))

def lvl_up():
    scorebord.resume()
    turtle.goto(0, -(SCREEN_Y/2-20))
    global game_speed
    game_speed *= 0.9


while game_on:
    time.sleep(game_speed)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -SCREEN_X/2:
            car.restart()

    if turtle.ycor() > SCREEN_Y / 2:
        lvl_up()


screen.exitonclick()
