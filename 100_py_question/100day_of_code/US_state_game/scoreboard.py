from turtle import Turtle

class ScoreBoard(Turtle):
    _score = 0
    _miss = 0
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("black")
        self.write(f"Right: {self._score}/50              Miss: {self._miss}", False, align="center")

    def resume(self):
        self._score += 1
        self.clear()
        self.write(f"Right: {self._score}/50              Miss: {self._miss}", False, align="center")

    def miss(self):
        self._miss += 1
        self.clear()
        self.write(f"Right: {self._score}/50              Miss: {self._miss}", False, align="center")

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")

    def win(self):
        self.goto(0, 0)
        self.write("WIN!", False, align="center")
