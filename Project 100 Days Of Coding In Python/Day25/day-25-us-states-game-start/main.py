import turtle
import pandas as pd

def write_state(correct_state_info):
    x_cord = correct_state_info[1]
    y_cord = correct_state_info[2]
    write_state = turtle.Turtle()
    write_state.penup()
    write_state.ht()
    write_state.goto(x_cord, y_cord)
    write_state.write(f"{correct_state_info[0]}", align="center", font=("Arial", 8, "normal"))

screen = turtle.Screen()
screen.title("US States Game")
screen.screensize(725, 491)
screen.setup(725, 491)
image = "blank_states_img.gif"
states_csv = pd.read_csv('50_states.csv')
all_states = states_csv["state"].values
correct_state_count = 0
correct_state_names = []

screen.addshape(image)
turtle.shape(image)

while correct_state_count < 50:
    answer_state = screen.textinput(title=f"{correct_state_count}/50 States Correct",
                                    prompt="What's another state's name?").title()
    check_state = answer_state in all_states

    if answer_state == "Exit":
        states_to_learn = [each_state for each_state in all_states if each_state not in correct_state_names]
        print(states_to_learn)
        break

    if check_state:
        state_row = states_csv[states_csv["state"] == answer_state]
        correct_state_info = state_row.values[0]
        write_state(correct_state_info)
        correct_state_count += 1
        correct_state_names.append(answer_state)
