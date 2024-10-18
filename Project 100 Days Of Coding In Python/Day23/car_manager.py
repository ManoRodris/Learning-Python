from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.starting_move_distance = 5

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.seth(0)
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for each_car in self.all_cars:
            each_car.backward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT

    def detect_collision(self, turtle_pos):
        for each_car in self.all_cars:
            if each_car.distance(turtle_pos) <= 20:
                return True