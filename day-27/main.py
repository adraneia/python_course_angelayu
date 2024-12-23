#import tkinter
from tkinter import *

#window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#add padding
window.config(padx=100, pady=200)
#Label

#my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="Final Text")
#my_label.pack()
#my_label.pack(side="left")
#-------------------pack place or grid to be shown, we cant mix up grid and pack
#my_label.place(x=100, y=0)
my_label.grid(column=0, row =0)
my_label.config(padx=50, pady=50)

#button
def button_clicked():
    print("i got clicked!")
    my_label.config(text="button clicked")
    my_label.config(text=input.get())
#button = tkinter.Button()
button = Button(text="click me!", command=button_clicked)
#button.pack(side="left")
button.grid(column=1 , row = 1)


#new button
new_button = Button(text="new_button click me!", command=button_clicked)
#button.pack(side="left")
new_button.grid(column=2 , row = 0)

#entry
input = Entry(width=10)
#input.pack(side="left")
input.grid(column=3, row=2)
print(input.get())

window.mainloop()