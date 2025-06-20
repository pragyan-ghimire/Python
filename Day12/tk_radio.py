from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

# def display(index):
#     print(food[index])

def display():
    print(f"You ordered {food[x.get()]}")

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index],
        variable=x,  # groups radiobuttons together if they share same variable
        value=index,  # assigns diff val to each radiobtn
        # command= lambda idx=index: display(idx),
        command= display,
        # indicatoron= 0, # removes circle indicator (push button shown)
    )
    radiobutton.config(
        padx= 25,
        pady= 16, 
        font=("Impact", 24)
    )
    radiobutton.pack(anchor= 'w')

window.mainloop()
