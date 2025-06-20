from tkinter import *

def submit():
    print(text.get("1.0", END))

window = Tk()

text = Text(
    window, 
    background= "#ff6600",
    font= ("Ink Free", 24),
    height= 8,
    width= 20,
    padx= 20,
    pady= 20
    )
text.pack()

button = Button(window, text= "submit", command= submit)
button.pack()



window.mainloop()