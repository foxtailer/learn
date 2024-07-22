from turtle import Screen
from paddle import Paddle
from boll import Boll
import time
from scorebord import Scorebord

SCREEN_W = 900
SCREEN_H = 600
is_on = True

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(SCREEN_W, SCREEN_H)
screen.tracer(0)

paddle_1 = Paddle('r',(SCREEN_H, SCREEN_W))
paddle_2 = Paddle('l',(SCREEN_H, SCREEN_W))
boll = Boll((SCREEN_H, SCREEN_W))
scorebord = Scorebord()

while is_on:
    time.sleep(boll.move_spead)
    screen.update()
    screen.listen()
    screen.onkeypress(paddle_1.go_up, "Up")
    screen.onkeypress(paddle_1.go_down, "Down")
    screen.onkeypress(paddle_2.go_up, "w")
    screen.onkeypress(paddle_2.go_down, "s")
    boll.move()

    # Detect colision whith puddle
    if boll.distance(paddle_1) < 50 and boll.xcor() > 400 or boll.distance(paddle_2) < 50 and boll.xcor() < -400:
        boll.bounce("x")

    # Detect gol
    if boll.xcor() > 460:
        scorebord.l_score += 1
        scorebord.update_scorebord()
        boll.restart()
        screen.update()
        time.sleep(1)
    if boll.xcor() < -460:
        scorebord.r_score += 1
        scorebord.update_scorebord()
        boll.restart()
        screen.update()
        time.sleep(1)
        
        


screen.exitonclick()