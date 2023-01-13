from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side, screen_size) -> None:
        super().__init__()
        self.side = side
        self.screen_soze = screen_size
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        if self.side == "l":
            self.goto(-(screen_size[1]/2-10), 0)
        elif self.side == "r":
            self.goto((screen_size[1]/2-10), 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.setx(new_y)

    def go_ddown(self):
        new_y = self.ycor() - 20
        self.setx(new_y)