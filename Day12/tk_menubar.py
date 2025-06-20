from tkinter import *

def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved")



window = Tk()

menubar = Menu(window)
window.config(menu= menubar)

fileMenu = Menu(
    menubar, 
    tearoff= 0, # get rid of dotted line
    ) 
menubar.add_cascade(label= "File", menu= fileMenu) # dropdown sort of effect
fileMenu.add_command(label= "Open", command= openFile) # we can also add image using image arg 
fileMenu.add_command(label= "Save", command= saveFile)
fileMenu.add_separator()
fileMenu.add_command(label= "Exit", command=quit)


editMenu = Menu(
    menubar, 
    tearoff= 0, # get rid of dotted line
    ) 
menubar.add_cascade(label= "Edit", menu= editMenu) # dropdown sort of effect
editMenu.add_command(label= "Copy")
editMenu.add_command(label= "Cut")
editMenu.add_command(label= "Paste")

window.mainloop()
