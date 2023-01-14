from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scorebord()

    def update_scorebord(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("courier", 80, "normal"))
        self.goto(0, 210)
        self.write(":", False, "center", ("courier", 80, "normal"))