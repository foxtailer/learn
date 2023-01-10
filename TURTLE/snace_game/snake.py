from turtle import Turtle

class Snake:
    def __init__(self) -> None:
        self.bones = 3
        self.body = []
        self._x = 0
        for _ in range(self.bones):
            bone = Turtle(shape="square")
            bone.penup()
            bone.color("white")
            bone.setx(self._x)
            self.body.append(bone)
            self._x += 20
            #bone.shapesize(stretch_len = 20, stretch_wid = 20)
    
    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].goto(self.body[index - 1].pos())
        self.body[0].forward(20)
        self.body[0].left(90)

