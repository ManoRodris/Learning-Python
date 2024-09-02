import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("blue")

def go_forward():
    tim.forward(10)

def go_back():
    tim.backward(10)

def go_clockwise():
    tim.right(10)

def go_counterclockwise():
    tim.left(10)

def clear_canva():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = turtle.Screen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_back)
screen.onkey(key="d", fun=go_clockwise)
screen.onkey(key="a", fun=go_counterclockwise)
screen.onkey(key="c", fun=clear_canva)
screen.listen()
screen.exitonclick()
