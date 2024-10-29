import pandas

weather_data = pandas.read_csv("weather_data.csv")
temp_list = weather_data["temp"].mean()
max_value = weather_data["temp"].max()
print(max_value)