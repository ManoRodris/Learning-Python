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

amount_of_cars = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    amount_of_cars += 1
    car.move_cars()

    if amount_of_cars == 6:
        car = CarManager()
        amount_of_cars = 0

    screen.onkey(player.move_forward, "Up")
    screen.listen()

screen.exitonclick()








