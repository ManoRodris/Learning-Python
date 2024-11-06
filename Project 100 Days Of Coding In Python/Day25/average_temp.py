import pandas

weather_data = pandas.read_csv("weather_data.csv")
temp_list = weather_data["temp"].mean()
max_value = weather_data["temp"].max()
#print(max_value)
#print(weather_data[weather_data.temp == max_value])

monday = weather_data[weather_data.day == "Monday"]
#fahrenheit_monday = monday.temp -
print(type(monday.temp))