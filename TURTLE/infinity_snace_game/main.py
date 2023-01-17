from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_speed = 0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    if snake.body[0].distance(food.pos()) < 15:
        food.refresh()
        scoreboard.resume()
        snake.extend()
    
    if snake.body[0].xcor() < - 290 or snake.body[0].xcor() > 290 or snake.body[0].ycor() > 290 or snake.body[0].ycor() < -290:
        scoreboard.compare()
        snake.reset()
        snake.create_snake()
        

    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            scoreboard.compare()
            snake.reset()
            snake.create_snake()
            


screen.exitonclick()