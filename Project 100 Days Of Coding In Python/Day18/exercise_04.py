import turtle as t
import random as r

gabriel = t.Turtle()
t.colormode(255)
gabriel.color("blue")
gabriel.shape("turtle")
gabriel.pensize(10)
gabriel.speed(10)

def rgb_generator():
    return r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)

for _ in range(200):
    gabriel.pencolor(rgb_generator())
    x = r.randint(0, 3)
    match x:
        case 0:
            gabriel.seth(0)
        case 1:
            gabriel.seth(90)
        case 2:
            gabriel.seth(180)
        case 3:
            gabriel.seth(270)
    gabriel.forward(30)



screen = t.Screen()
screen.exitonclick()