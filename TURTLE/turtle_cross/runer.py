from turtle import Turtle

class Runer(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(0, -280)
        self.showturtle()

    def run(self):
        self.forward(10)