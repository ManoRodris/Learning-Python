import turtle as t
import random

tony = t.Turtle()
tony.shape("turtle")
tony.color("red")
tony.pencolor("blue")
t.colormode(255)
tony.pensize(10)

for num_sides in range(3, 11):
    angle = 360/num_sides
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tony.pencolor(rgb)
    for y in range(num_sides):
        tony.right(angle)
        tony.forward(100)


screen = t.Screen()
screen.exitonclick()
