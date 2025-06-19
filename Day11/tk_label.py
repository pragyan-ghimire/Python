from tkinter import *

# label = widget that can holds text and/or an image within a window

window = Tk()
window.geometry("420x420")

photo = PhotoImage(file="../Photos/1.png")

label = Label(
    master=window,
    text="Hello world",
    font=("Arial", 40, "bold"),
    fg="green",
    bg="black",
    bd= 10,
    relief= SUNKEN,
    padx= 16,
    pady= 16,
    image= photo,
    compound= "bottom" # show image relative to text
)
label.pack()  # shows horizontal middle
# label.place(x= 0, y= 0) # shows horizontal middle

window.mainloop()
