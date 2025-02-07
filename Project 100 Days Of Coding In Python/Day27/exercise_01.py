import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    global clicks
    clicks +=1
    my_label.config(text=f"You clicked {clicks} times")

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

clicks = 0
button = tkinter.Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="Second button")
button_2.grid(column=2, row=0)

window.mainloop()