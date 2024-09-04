from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x_position = 0

snake = []

for x in range(3):
    part_of_snake = Turtle(shape="square")
    part_of_snake.color("yellow")
    part_of_snake.penup()
    part_of_snake.goto(x=x_position, y=0)
    snake.append(part_of_snake)
    x_position += 20

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for index in range(len(snake) - 1, 0, -1):
        new_x = snake[index - 1].xcor()
        new_y = snake[index - 1].ycor()
        snake[index].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()