from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
      window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

# Configuring the window interface
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Configuring the title above the other elements
title_label = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=1)

# Configuring the tomato visualization in canva
tomato_img = PhotoImage(file=r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Project 100 Days Of Coding In Python\Day28\tomato.png")
canvas = Canvas(window, width=220, height=240, bg=YELLOW, highlightthickness=0)
canvas.create_image(110, 120, image=tomato_img)
timer_text = canvas.create_text(110, 140, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=2)

# Configuring the buttons
start_button = Button(text="Start", bg=YELLOW, fg=RED, command=start_timer)
start_button.grid(column=0, row=3)
print(start_button.configure().keys())

reset_button = Button(text="Reset", bg=YELLOW, fg=RED)
reset_button.grid(column=2, row=3)

# Configuring the amount of times the pomodoro app was played
checkmark_label = Label(text="✔", font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)

window.mainloop()