from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_coordinated = self.xcor() + self.x_move
        y_coordinated = self.ycor() + self.y_move
        self.goto(x_coordinated, y_coordinated)

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_off_paddle()

