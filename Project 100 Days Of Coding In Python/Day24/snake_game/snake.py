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

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def create_each_part(self, position):
        part_of_snake = Turtle(shape="square")
        part_of_snake.color("yellow")
        part_of_snake.penup()
        part_of_snake.goto(position)
        self.snake.append(part_of_snake)

    def create_snake(self):
        for x in range(3):
            position = (self.x_positions, 0)
            self.create_each_part(position)
            self.x_positions -= 20

    def increase_snake(self):
        position = self.snake[-1].pos()
        self.create_each_part(position)

    def collision(self):
        for part in self.snake[1:]:
            if self.head.distance(part) < 15:
                return True
        return False

    def reset(self):
        for each_part in self.snake:
            each_part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

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


