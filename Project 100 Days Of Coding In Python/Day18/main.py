from color_searcher import colors_list
import turtle as t
import random as r

# First: Make the turtle run through a line making 10 circles with different random colors
# Second: Make the turtle repeat that in a line above the past line
# Third: Make the program repeat that ten times

rodrigo = t.Turtle()
t.colormode(255)
rodrigo.speed("fastest")
rodrigo.penup()
rodrigo.hideturtle()

def go_to_next_line():
    rodrigo.setheading(90)
    rodrigo.forward(50)
    rodrigo.setheading(180)
    rodrigo.forward(500)
    rodrigo.setheading(0)

def draw_circles():
    random_color = r.choice(colors_list)
    rodrigo.dot(20, random_color)
    rodrigo.forward(50)

def start_in_footer():
    rodrigo.setheading(225)
    rodrigo.forward(350)
    rodrigo.setheading(0)

start_in_footer()
for _ in range(10):
    for _ in range(10):
        draw_circles()
    go_to_next_line()

screen = t.Screen()
screen.exitonclick()

