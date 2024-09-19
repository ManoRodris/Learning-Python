from turtle import Turtle

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_coordinated = self.xcor() + self.x_move
        y_coordinated = self.ycor() + self.y_move
        self.goto(x_coordinated, y_coordinated)

    def bounce(self):
        self.y_move *= -1

    def change_direction(self):
        if self.heading() == NORTH:
            self.seth(SOUTH)
        elif self.heading() == SOUTH:
            self.seth(NORTH)
        elif self.heading() == EAST:
            self.seth(WEST)
        elif self.heading() == WEST:
            self.seth(EAST)