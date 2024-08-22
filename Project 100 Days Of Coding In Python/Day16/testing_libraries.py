#Testing some libraries

# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("cyan2")
# timmy.left(120)
# timmy.forward(100)
#
# screen = Screen()
# screen.exitonclick()

import prettytable

pokemon_table = prettytable.PrettyTable()

pokemon_table.add_column("Pokemon", ["Charmander", "Bublasaur", "Squirtle"])
pokemon_table.add_column("Type", ["Fire", "Grass", "Water"])
pokemon_table.align = "l"
print(pokemon_table)