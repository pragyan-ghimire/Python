from tkinter import *
from PIL import ImageTk, Image


def submit():
    print(f"The tempature is {scale.get()} degree C")


window = Tk()

img1 = Image.open(fp="../Photos/fire.png")
img2 = Image.open(fp="../Photos/ice.png")

fire_resized = img1.resize((80, 80) )
ice_resized = img2.resize((80, 80))
fire = ImageTk.PhotoImage(fire_resized)
ice = ImageTk.PhotoImage(ice_resized)

hotLabel = Label(window, image=fire, height=100, width=100)
hotLabel.pack()
scale = Scale(
    window,
    from_=100,
    to=0,
)
scale.config(
    length=600,
    orient=VERTICAL,  # orientation of scale,
    font=("Consolas", 16),
    tickinterval=10,
    # showvalue=0,  # hide the value
    resolution=5,  # increment of slider,
    troughcolor="#ff6600",
    fg="#FF1C00",
    bg="#69eaff",
    activebackground="#69eaff",
)
scale.set((scale["from"] - scale["to"]) / 2 + scale["to"])
scale.pack()


coldLabel = Label(window, image=ice)
coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
