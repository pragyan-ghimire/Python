from tkinter import *
from tkinter import colorchooser # submodule

def click():
    global btn_color
    color= colorchooser.askcolor()
    # print(color)
    button.config(fg= color[1])

window = Tk()

window.geometry("420x420")

button = Button(text="click me", command=click)
button.pack()

window.mainloop()