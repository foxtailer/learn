from turtle import Turtle

class ScoreBoard(Turtle):
    _score = 0
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write("Score: 0", False, align="center")

    def resume(self):
        self._score += 1
        self.clear()
        self.write(f"Score: {self._score}", False, align="center")

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")
