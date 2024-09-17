import turtle
from paddle import Paddle

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong game")

screen.tracer(0)

player_one = Paddle()
player_one.goto(350, 0)

player_two = Paddle()
player_two.goto(-350, 0)

game_on = True

while game_on:
    screen.listen()

    screen.onkey(player_one.up, "Up")
    screen.onkey(player_one.down, "Down")

    screen.onkey(player_two.up, "w")
    screen.onkey(player_two.down, "s")

    screen.update()

screen.exitonclick()
