import turtle
import random

colors = ["blue", "green", "yellow", "orange", "red", "purple"]
game_running = False
screen = turtle.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
if user_bet:
    game_running = True

all_turtles = []
y_position = -70
for x in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)
    y_position += 30

while game_running:
    for each_turtle in all_turtles:
        random_pace = random.randint(0, 10)
        each_turtle.forward(random_pace)
        if each_turtle.xcor() > 230:
            winner = each_turtle
            if winner.fillcolor() == user_bet:
                color_winner = winner.fillcolor()
                print(f"Congratulations! Your bet is right! The {color_winner} turtle win")
                game_running = False
            else:
                color_winner = winner.fillcolor()
                print(f"Sorry, your bet is wrong, the {color_winner} turtle win")
                game_running = False

screen.exitonclick()