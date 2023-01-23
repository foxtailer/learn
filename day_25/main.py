# with open(r"E:\git\learn\day_25\weather-data.csv") as data:
#     print(data.readlines())
#____________________________________
# import csv

# temperature = []

# with open(r"E:\git\learn\day_25\weather-data.csv") as data_file:
#     data = csv.reader(data_file)

#     for line in data:
#         temperature.append(line[1])

# print(temperature[1:])
#_________________________________
import pandas
data = pandas.read_csv(r"E:\git\learn\day_25\weather-data.csv")
temp_list = data["temp"].to_list()
print("average", sum(temp_list)/len(temp_list))

# get colun from data
print(data["temp"])
print(data.temp)

#get data from row
#print(data[data.temp != 14])
print(type(data[data.temp == 24].day))
print(data[data.temp == 24].day.to_list()[0])
