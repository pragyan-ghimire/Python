from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(
        initialdir="D:\\Documents\\",
        title= "Open File",
        filetypes= (
            ("text files","*.txt"),
            ("all files", "*.*")
        )
    )
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

btn = Button(window, text="Open", command= openFile)
btn.pack()

window.mainloop()