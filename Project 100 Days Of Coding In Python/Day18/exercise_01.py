import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
tim.pencolor("blue")

for x in range(4):
    tim.forward(100)
    tim.left(90)



# forward(100)
# left(120)
# forward(100)

screen = turtle.Screen()
screen.exitonclick()