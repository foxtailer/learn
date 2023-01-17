from turtle import Turtle

class ScoreBoard(Turtle):
    _score = 0
    with open(r"E:\git\learn\TURTLE\infinity_snace_game\data.txt") as data:
        _max_score = int(data.read())
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self._score} Max score: {self._max_score}", False, align="center")

    def resume(self):
        self._score += 1
        self.clear()
        self.write(f"Score: {self._score} Max score: {self._max_score}", False, align="center")

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")

    def compare(self):
        if self._score > self._max_score:
            self._max_score = self._score
            with open(r"E:\git\learn\TURTLE\infinity_snace_game\data.txt", "w") as data:
                data.write(str(self._max_score))
        self._score = 0
        self.clear()
        self.write(f"Score: {self._score} Max score: {self._max_score}", False, align="center")
