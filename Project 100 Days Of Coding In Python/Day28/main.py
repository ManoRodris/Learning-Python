from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 1
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   global REPS

   work_time = WORK_MIN * 60
   short_break_time = SHORT_BREAK_MIN * 60
   long_break_time = LONG_BREAK_MIN * 60

   if REPS in (0, 2, 4, 6):
      count_down(work_time)
      REPS += 1
   elif REPS in (1, 3, 5):
      count_down(short_break_time)
      REPS += 1
   elif REPS == 7:
      count_down(long_break_time)
      REPS == 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
   count_min = math.floor(count / 60)
   count_sec = round(count % 60)

   if count_sec < 10:
      canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
   else:
      canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

   if count > 0:
      window.after(1000, count_down, count - 1)
   else:
      start_timer()
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

reset_button = Button(text="Reset", bg=YELLOW, fg=RED)
reset_button.grid(column=2, row=3)

# Configuring the amount of times the pomodoro app was played
checkmark_label = Label(text="✔", font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)

window.mainloop()