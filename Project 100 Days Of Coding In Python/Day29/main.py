# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")

img = PhotoImage(file=r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Project 100 Days Of Coding In Python\Day29\logo.png")
canvas = Canvas(window, width=220, height=240, highlightthickness=0)
canvas.create_image(110, 120, image=img)
canvas.pack()

window.mainloop()