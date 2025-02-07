from tkinter import *

# Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=300)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0, padx=5, pady=(15, 0))

# Labels
label = Label(text="Miles")
label.grid(column=2, row=0, pady=(15, 0))

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

window.mainloop()