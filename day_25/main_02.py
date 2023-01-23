import pandas as pd

data = pd.read_csv(r"E:\git\learn\day_25\228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

squirrel_colors = ["Gray", "Black", "Cinnamon"]

sq_by_color = {}

for color in squirrel_colors:
    sq_by_color[color] = len(data[data["Primary Fur Color"] == color])

new_data = pd.DataFrame([sq_by_color])
print(new_data)