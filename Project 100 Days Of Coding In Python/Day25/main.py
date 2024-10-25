# with open("weather_data.csv", "r") as data:
#     weather_data = data.readlines()
#     print(weather_data)

# import csv
#
# with open("weather_data.csv", "r") as data:
#     weather_data = csv.reader(data)
#     next(weather_data)
#     temperature = [int(data_file[1]) for data_file in weather_data]
#     print(temperature)

import pandas

weather_data = pandas.read_csv("weather_data.csv")
print(weather_data["temp"])