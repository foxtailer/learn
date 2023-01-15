from turtle import Turtle

class Runer(Turtle):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        self.forward(10)