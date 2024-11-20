# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#         #print(temperatures)
#         #print(row)
#     temperatures = temperatures[1:]
#     for temp in range(len(temperatures)):  # Converts each element to an integer
#         temperatures[temp] = int(temperatures[temp])
#     print(temperatures)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

#data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday.temp[0] * 9/5 + 32
# print(monday_temp_F)
#

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# print(data)


#gray cinamon black


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color_list = squirrel_data["Primary Fur Color"].to_list()
gray = primary_fur_color_list.count("Gray")
red = primary_fur_color_list.count("Cinnamon")
black = primary_fur_color_list.count("Black")

squirrel_count_dict = {
     "Fur" : ["Gray", "Red", "Black"],
     "scores": [gray, red, black]
}

squirrel_count_data = pandas.DataFrame(squirrel_count_dict)
squirrel_count_data.to_csv("new_squirrel_count.csv")
print(squirrel_count_data)

