import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move_forward, "Up")
screen.listen()

amount_of_cars = 0
car.create_cars()

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car.move_cars()
    amount_of_cars += 1

    if amount_of_cars == 6:
        car.create_cars()
        amount_of_cars = 0

    if player.ycor() > 280:
        player.goto_restart_position()
        score.increase_level()
        car.increase_speed()

    if car.detect_collision(player.pos()):
        game_is_on = False
        score.show_game_over()

screen.exitonclick()








