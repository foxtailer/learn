from turtle import Screen
from paddle import Paddle

SCREEN_W = 900
SCREEN_H = 600

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(SCREEN_W, SCREEN_H)

paddle_1 = Paddle('r',(SCREEN_H, SCREEN_W))
paddle_2 = Paddle('l',(SCREEN_H, SCREEN_W))

screen.listen()
screen.onkey(paddle_1.go_up, "Up")


screen.exitonclick()