from tkinter import *

def miles_to_km():
    m = float(entry.get())
    km = round(m * 1.609, 2)
    km = str(km)
    label_3.config(text=f"{km}")

# Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.insert(0, string="0")
entry.grid(column=1, row=0)

# Labels
label = Label(text="Miles")
label.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()