from turtle import Turtle

class Snake:
    _tern = ""
    def __init__(self) -> None:
        self.bones = 3
        self.body = []
        self.create_snake()
    
    def create_snake(self):
        _x = 0, 0
        for _ in range(self.bones):
            self.add_segment(_x)
            #_x[0] += 20
    
    def extend(self):
        self.add_segment(self.body[-1].pos())

    def add_segment(self, position):
        bone = Turtle(shape="square")
        bone.penup()
        bone.color("white")
        bone.goto(position)
        self.body.append(bone)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].goto(self.body[index - 1].pos())
        self.body[0].forward(20)
        #self.body[0].left(90)

