from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.x_positions = 0
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in range(3):
            part_of_snake = Turtle(shape="square")
            part_of_snake.color("yellow")
            part_of_snake.penup()
            part_of_snake.goto(x=self.x_positions, y=0)
            self.x_positions += 20
            self.snake.append(part_of_snake)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def increase_snake(self):
        part_of_snake = Turtle(shape="square")
        part_of_snake.color("yellow")
        part_of_snake.penup()
        last_part = len(self.snake) - 1
        x_position = self.snake[last_part].xcor() + 20
        y_position = self.snake[last_part].ycor() + 20
        part_of_snake.goto(x=x_position, y=y_position)
        self.snake.append(part_of_snake)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


