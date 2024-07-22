from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side, fild) -> None:
        super().__init__()
        self.side = side
        self.fild = fild
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed(10)
        if self.side == "l":
            self.goto(-(fild[1]/2-20), 0)
        elif self.side == "r":
            self.goto((fild[1]/2-20), 0)

    def go_up(self):
        if self.ycor() > 250:
            pass
        else:
            new_y = self.ycor() + 25
            self.sety(new_y)

    def go_down(self):
        if self.ycor() < - 250:
            pass
        else:
            new_y = self.ycor() - 20
            self.sety(new_y)