from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(
        initialdir= "D:\\Documents\\",
        defaultextension= ".txt",
        filetypes= [
            ("Text file",".txt"),
            ("Html", ".html"),
            ("all files", ".*")
        ]
    )
    # file_text = str(text.get("1.0", END))
    file_text = input("Enter some text: ")
    file.write(file_text)
    file.close()

window = Tk()


text = Text(window)
text.pack()

btn = Button(window, text="Save", command= saveFile)
btn.pack()


window.mainloop()