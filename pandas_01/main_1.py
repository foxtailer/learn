import pandas as pd

data = pd.read_csv(r"E:\_temp\25 Day 25 - Intermediate - Working with CSV Data and the Pandas Library\226 weather-data.csv")

data_dict = data.to_dict()
print(data_dict)

print(data.temp.max())

# Get data row

print(data[data.day == "Wednesday"])
print(data[data.temp > 15])
print(data[data.temp == data.temp.max()])

temp_F = []
for i in data.temp:
    temp_F.append(int(i) * 9/5 + 32)

data["temp_f"] = temp_F

print(data)

data.to_csv("new_csv.csv")