import turtle as tl
import random
#import colorgram

#colors = colorgram.extract(r'C:\Users\User\Desktop\git\learn\TURTLE\hirst_painting\hirst.jpg', 20)
# for color in colors:   
#     rgb_colors.append(tuple(color.rgb))

rgb_colors = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90)]
tl.colormode(255)
turtle = tl.Turtle()
turtle.penup()
turtle.right(135)
turtle.forward(400)
turtle.right(225)
turtle.speed(0)

for _ in range(10):
    for _ in range(10):
        turtle.forward(50)
        turtle.dot(20, random.choice(rgb_colors))
    
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(180)

turtle.hideturtle()


screen = tl.Screen()
screen.exitonclick()