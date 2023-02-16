from tkinter import *


window = Tk()
window.title("First Window")
window.minsize(width=500, height=600)


my_label = Label(text="I am a label")
my_label.pack()


def change_label():
    new_text = use_input.get()
    my_label["text"] = new_text


button = Button(text="Click", command=change_label)
button.pack()

use_input = Entry()
use_input.pack()


window.mainloop()
