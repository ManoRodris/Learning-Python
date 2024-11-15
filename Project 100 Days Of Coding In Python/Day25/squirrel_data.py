import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241115.csv")
grey_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_colors = {
    "Fur color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrel, cinnamon_squirrel, black_squirrel]
}

data = pandas.DataFrame(squirrel_colors)
data.to_csv("squirrel_colors.csv", index=False)
