from tkinter import *

count = 0
def click():
    global count
    count += 1
    # print(count)
    label.config(text= count)


window = Tk()
window.geometry("420x420")
button = Button(window, text="Click me")
# image = PhotoImage(file="../Photos/2.png")
button.config(command=click)
button.config(
    font=("Ink Free", 20, "bold"),
    bg="#ff6200",
    fg="#fffb1f",
    activebackground="#ff0000",
    activeforeground="#fffb1f",
    # image= image,
    compound= "left"
)
# button.config(state= DISABLED) # disabled button
button.pack()

label = Label(window, text= count)
label.config(font=('Helvetica', 12, 'bold'))
label.pack()

window.mainloop()
