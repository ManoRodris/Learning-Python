from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,3)
        self.penup()
        self.seth(0)
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-270, 270))

    def move_cars(self):
        self.forward(STARTING_MOVE_DISTANCE)

