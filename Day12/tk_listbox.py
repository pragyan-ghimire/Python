from tkinter import *

foods = ["Pizza", "Burger", "Curd"]

def submit():
    # print(listbox.get(listbox.curselection()))
    
    # for multimode
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    
    for index in food:
        print(index)


def add():
    index = listbox.size()
    listbox.insert(index, entryBox.get())
    listbox.config(height= listbox.size())

def delete():
    # listbox.delete(listbox.curselection()) # for single mode

    # for multiple mode
    for index in reversed(listbox.curselection()): # if no reversed function is used, the index changes after first item is deleted
        listbox.delete(index)



    listbox.config(height= listbox.size())

window = Tk()

listbox = Listbox(window)

for index in range(len(foods)):
    listbox.insert(index+1, foods[index])

listbox.config(
    bg= "#f7ffde",
    font= ("Constantia", 24),
    width= 12,
    height= listbox.size(),
    selectmode= MULTIPLE, # allows for multiple selection
)
listbox.pack()

entryBox = Entry(window)
entryBox.pack()

add = Button(window, text="Add" ,command= add)
add.pack()

button = Button(window, text="Submit" ,command= submit)
button.pack()

delbutton = Button(window, text="Delete" ,command= delete)
delbutton.pack()
window.mainloop()