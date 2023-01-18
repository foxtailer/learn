# with open(r"E:\git\learn\day_25\weather-data.csv") as data:
#     print(data.readlines())

import csv

temperature = []

with open(r"E:\git\learn\day_25\weather-data.csv") as data_file:
    data = csv.reader(data_file)

    for line in data:
        temperature.append(line[1])

print(temperature[1:])