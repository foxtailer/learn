from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(440, 0)