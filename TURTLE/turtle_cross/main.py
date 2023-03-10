from turtle import Turtle, Screen
import random, time
from runer import Runer
from car import Car
from scorebord import ScoreBoard

SCREEN_X = 600
SCREEN_Y = 600
game_on = True
game_speed = 0.5
cars_amount = 10

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
def cars_init():
    for _ in range(cars_amount):
        cars.append(Car(screen.screensize()))

def lvl_up():
    scorebord.resume()
    turtle.goto(0, -(SCREEN_Y/2-20))
    global game_speed, cars_amount
    game_speed *= 0.9
    cars_amount += 5
    cars_init()

cars_init()

while game_on:
    time.sleep(game_speed)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -SCREEN_X/2:
            car.restart()
        if car.distance(turtle) < 20:
            scorebord.gameover()
            game_on = False

    if turtle.ycor() > SCREEN_Y / 2:
        lvl_up()


screen.exitonclick()
