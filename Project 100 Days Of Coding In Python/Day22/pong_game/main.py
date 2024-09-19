import turtle
import time
from paddle import Paddle
from ball import Ball

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong game")

screen.tracer(0)

player_one = Paddle((350, 0))
player_two = Paddle((-350, 0))

game_on = True

ball = Ball()

while game_on:
    time.sleep(0.1)
    screen.listen()

    screen.onkey(player_one.up, "Up")
    screen.onkey(player_one.down, "Down")

    screen.onkey(player_two.up, "w")
    screen.onkey(player_two.down, "s")

    screen.update()

    ball.move()

    if player_one.distance(ball) <= 15 or player_two.distance(ball) <= 15:
        ball.bounce()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

screen.exitonclick()
