import pandas as pd

colors = {}
data = pd.read_csv(r"C:\Users\User\Desktop\glovo\git\learn\pandas_01\228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
colors["Gray"] = len(data[data["Primary Fur Color"] == "Gray"])
colors["Cinnamon"] = len(data[data["Primary Fur Color"] == "Cinnamon"])
colors["Black"] = len(data[data["Primary Fur Color"] == "Black"])

pd_colors = pd.DataFrame(colors, index=3)
print(pd_colors)