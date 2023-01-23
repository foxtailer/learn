import turtle, pandas
from scoreboard import ScoreBoard

data = pandas.read_csv(r"learn\US_state_game\50_states.csv")
image = r"learn\US_state_game\blank_states_img.gif"
screen = turtle.Screen()
screen.title("US quize")
screen.addshape(image)
scorebord = ScoreBoard()

tur = turtle.Turtle()
tur.shape(image)

# Way to get coordinates
# def click_coord(x, y):
#     print(x, y)
# screen.onclick(click_coord)
score = 0
while True:
    user_choise = screen.textinput(title=f"US states quize({score}/50)", prompt="What state ou now?").title()
    if user_choise in data.state.to_list():
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        #tur.goto(data[data["state"] == user_choise].x.to_list()[0], data[data["state"] == user_choise].y.to_list()[0])
        tur.goto(int(data[data["state"] == user_choise].x), int(data[data["state"] == user_choise].y))
        tur.write(user_choise, False, align="center")
        score += 1
        scorebord.resume()
    else:
        scorebord.miss()
    if score == 50:
        print("You are great!")
        break

#turtle.mainloop()
screen.exitonclick()