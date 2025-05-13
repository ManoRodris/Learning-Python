# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# Instance of the main window

window = Tk()
# window.geometry("240x240")
window.config(padx=50, pady=50)
window.title("Password Manager")

# Configuring the picture
img = PhotoImage(file=r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Project 100 Days Of Coding In Python\Day29\logo.png")
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Configuring the labels and entries

website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(window, width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(window, width=50)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(window, width=30)
password_entry.grid(column=1, row=3, padx=(0,5))

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3, padx=(0,5))

add_button = Button(text="Add", width=42)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()