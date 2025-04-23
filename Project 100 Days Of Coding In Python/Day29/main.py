# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
# window.geometry("240x240")
window.config(padx=20, pady=20)
window.title("Password Manager")

img = PhotoImage(file=r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Project 100 Days Of Coding In Python\Day29\logo.png")
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.pack()

window.mainloop()