import os
import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# Defining a fix way inside the project for the accounts informations
file_root = os.path.join(os.path.dirname(__file__), "data", "accounts.txt")
os.makedirs(os.path.dirname(file_root), exist_ok=True)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if (not password_text or not password_text.strip()) or (not email_text or not email_text.strip()) or (not website_text or not website_text.strip()):
        messagebox.showerror(title="E-mail or password invalid", message="Please don't leave any fields empty!")
    else:
        its_ok = messagebox.askokcancel(title=website_text, message=f"Are you sure these informations are right? \n E-mail: {email_text} \n Password: {password_text}")
        if its_ok:
            with open(file_root, "a", encoding="utf-8") as f:
                f.write(f"{website_text} | {email_text} | {password_text} \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Instance of the main window

window = Tk()
# window.geometry("240x240")
window.config(padx=50, pady=50)
window.title("Password Manager")

# Configuring the picture
img = PhotoImage(file=r"C:\Users\Rodrigo\Documents\Projects\Learning-Python\Project 100 Days Of Coding In Python\Day29\logo.png")
# img = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Configuring the labels and entries

website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(window, width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(window, width=50)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(window, width=30)
password_entry.grid(column=1, row=3, padx=(0,5))

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, padx=(0,5))

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()