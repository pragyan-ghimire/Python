from tkinter import *
from tkinter import messagebox

# there are many variety of message box

def click():
    # messagebox.showinfo(title= "Notification", message= "This is a show info message box.")
    # messagebox.showwarning(title= "Notification", message= "This is a show warning message box.")
    # messagebox.showerror(title= "Notification", message= "This is a show error message box.")
    # ok = messagebox.askokcancel(title= "Notification", message= "This is a ask ok cancel message box.")
    # if ok:
    #     print("Do the task")
    # else:
    #     print("Cancel the task")
    retry = messagebox.askretrycancel(title= "Notification", message= "This is a ask retry cancel message box.")
    if retry:
        print("Retry the task")
    else:
        print("Cancel the task")


window = Tk()

button = Button(window, command= click, text= "click me")
button.pack()

window.mainloop()