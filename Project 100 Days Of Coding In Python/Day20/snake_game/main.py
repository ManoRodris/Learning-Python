from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_position = 0

for x in range(0, 3):
    part_of_snake = Turtle(shape="square")
    part_of_snake.color("yellow")
    part_of_snake.penup()
    part_of_snake.goto(x=x_position, y=0)
    x_position += 20

screen.exitonclick()