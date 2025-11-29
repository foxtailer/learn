from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")
screen.title("Fractal")
screen.setup(600, 600)

turtle = Turtle()
turtle.color("white")
turtle.shape("turtle")
turtle.speed(0)
turtle.hideturtle()

alpha = 0.05

def fractal_rectangle(A, B, C, D, deep=100):
    if deep < 1:
        return
    turtle.penup()
    turtle.setpos(D)
    turtle.pendown()
    for a, b in A, B, C, D:
        turtle.setpos(a, b)
    A1 = (A[0]*(1-alpha)+B[0]*alpha, A[1]*(1-alpha)+B[1]*alpha)
    B1 = (B[0]*(1-alpha)+C[0]*alpha, B[1]*(1-alpha)+C[1]*alpha)
    C1 = (C[0]*(1-alpha)+D[0]*alpha, C[1]*(1-alpha)+D[1]*alpha)
    D1 = (D[0]*(1-alpha)+A[0]*alpha, D[1]*(1-alpha)+A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1) 
    
fractal_rectangle((-200, 200), (200, 200), (200, -200), (-200, -200))

screen = Screen()
screen.exitonclick()
