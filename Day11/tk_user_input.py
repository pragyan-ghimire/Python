# entry widget = textbox that accepts a sigle line of user input

from tkinter import *


def submit():
    username = entry.get()
    print(username)
def delete():
    entry.delete(0, END) # deletes the line of text
def backspace():
    entry.delete(len(entry.get())-1, END) # deletes last character 

window = Tk()



window.geometry("420x420")
 
entry = Entry()
entry.config(font=("Ink Free", 16),bg="#000000", fg= "#ffffff")
# entry.insert(0, "Something") # default text
# entry.config(state= DISABLED) # can be active or disabled
entry.config(width= 10) # display 10 char at max
# entry.config(show= "*") # hides character with show character
entry.pack()

submit = Button(window, text= "Submit", command= submit)
# submit.pack(side = RIGHT)
submit.pack()
delete = Button(window, text= "delete", command= delete)
delete.pack()
backspace = Button(window, text= "backspace", command= backspace)
backspace.pack()

window.mainloop()