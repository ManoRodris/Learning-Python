import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong game")

screen.tracer(0)

player_one = Paddle((350, 0))
player_two = Paddle((-350, 0))

game_on = True

decrease_speed = 0.01

ball = Ball()
scoreboard = Scoreboard()

while game_on:
    time.sleep(ball.move_speed)
    screen.listen()

    screen.onkey(player_one.up, "Up")
    screen.onkey(player_one.down, "Down")

    screen.onkey(player_two.up, "w")
    screen.onkey(player_two.down, "s")

    screen.update()

    ball.move()

    if player_one.distance(ball) < 50 and ball.xcor() > 320:
        ball.bounce_off_paddle()

    if player_two.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_off_wall()

    if ball.xcor() > 390:
        scoreboard.increase_score(False)
        ball.refresh()

    if ball.xcor() < -390:
        scoreboard.increase_score(True)
        ball.refresh()

screen.exitonclick()
