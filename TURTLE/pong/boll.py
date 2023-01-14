from turtle import Turtle
import random
import time

class Boll(Turtle):
    def __init__(self, fild):
        super().__init__()
        self.fild = fild
        self.penup()
        self.shape("circle")
        #self.setheading(0)
        self.color("white")
        self.move_spead = 0.05
        self.x_move = 10
        self.y_move = 10
        self.move()
          
    def move(self):
        # wall bounce
        if self.ycor() > self.fild[0]/2 - 10 or self.ycor() < -(self.fild[0]/2 - 10):
            self.bounce("y")
        # move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, coord):
        if coord == "y":
            self.y_move *= -1
        elif coord == "x":
            self.x_move *= -1
            self.move_spead *= 0.9

    def restart(self):
        self.home()
        self.move_spead = 0.05
        self.x_move *= -1
        self.y_move *= -1
