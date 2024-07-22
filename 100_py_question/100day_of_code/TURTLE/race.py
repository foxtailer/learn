from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(800, 400)

t_colors = ["red", "green", "blue", "yellow", "purple"]
turtles = []

while True:
    user_choise = screen.textinput(title="Raice Game", prompt="Make your choice, what color of winning turtle: \nred, green, blue, yellow, purple")
    if user_choise in t_colors:
        break
    
def spawn(t_list):
    field_width = screen.screensize()[1] - 50 * 2  # 50 is a border x 
    distance = field_width / len(t_list)
    pos_y = -(screen.screensize()[1] / 2) + 10  # 10 is border y
    pos_x = -(screen.screensize()[0] / 2) + 50
    for turtle in t_list:
        turtle.goto(pos_x, pos_y)  # 10 is border y
        turtle.showturtle()
        pos_y += distance

def race(t_list):
    winner = 0
    winner_color = ""
    while not winner:
        for turtle in t_list:
            if turtle.xcor() < screen.screensize()[0] - 50:
                turtle.forward(random.randint(1, 10))
            else:
                winner = 1
                winner_color = turtle.color()
                print(winner_color[0] == user_choise)


for i in range(len(t_colors)):
    turtle = Turtle(shape="turtle")
    turtle.hideturtle()
    turtle.penup()
    turtle.color(t_colors[i])
    turtles.append(turtle)

spawn(turtles)
race(turtles)

screen.exitonclick()