import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
screen.screensize(725, 491)
image = "blank_states_img.gif"
states_csv = pd.read_csv('50_states.csv')

screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

check_state = answer_state in states_csv["state"].values

print(check_state)

screen.exitonclick()