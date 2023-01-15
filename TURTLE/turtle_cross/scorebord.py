from turtle import Turtle

class ScoreBoard(Turtle):
    _score = 0
    def __init__(self, fild) -> None:
        super().__init__()
        self.x_max = fild[0]/2
        self.x_min = -(fild[0]/2)
        self.y_max = fild[1]/2
        self.y_min = -(fild[1]/2)
        self.hideturtle()
        self.penup()
        self.goto(self.x_min +40, self.y_max-20)
        self.color("black")
        self.write("Score: 0", False, align="center")

    def resume(self):
        self._score += 1
        self.clear()
        self.write(f"Score: {self._score}", False, align="center")

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")
