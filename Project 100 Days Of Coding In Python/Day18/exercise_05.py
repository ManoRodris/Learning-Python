import turtle as t
import random

rodrigo = t.Turtle()
rodrigo.shape("turtle")
rodrigo.color("blue")
rodrigo.speed("fastest")
t.colormode(255)

def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

for x in range(0, 360, 5):
    rodrigo.seth(x)
    rodrigo.pencolor(random_rgb())
    rodrigo.circle(100)

screen = t.Screen()
screen.exitonclick()