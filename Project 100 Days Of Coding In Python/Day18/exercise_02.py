import turtle as t

the_turtle = t.Turtle()
the_turtle.shape("turtle")

for x in range(10):
    the_turtle.pencolor("blue")
    the_turtle.forward(10)
    the_turtle.pencolor("white")
    the_turtle.forward(10)

screen = t.Screen()
screen.exitonclick()

