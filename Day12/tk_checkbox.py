from tkinter import *


def display():
    if x.get() == 1:
        print("Python")
    if y.get() == 1:
        print("Java")


window = Tk()
x = IntVar()
checkbox = Checkbutton(
    window,
    text="Python",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
)
checkbox.config(
    font=("Arial", 20),
    fg="#0000ff",
    bg="#000000",
    activebackground="#000000",
    activeforeground="#0000ff",
)
# checkbox.config()
checkbox.pack(anchor= 'w')


y = IntVar()
checkbox2 = Checkbutton(
    window,
    text="Java",
    variable=y,
    onvalue=1,
    offvalue=0,
    command=display,
)
checkbox2.config(
    font=("Arial", 20),
    fg="#0000ff",
    bg="#000000",
    activebackground="#000000",
    activeforeground="#0000ff",
)
# checkbox2.config(anchor= 'w')
checkbox2.pack(anchor= 'w')
window.mainloop()
