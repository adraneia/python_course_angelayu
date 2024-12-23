from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#miles entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#miles label
miles = Label(text="miles")
miles.grid(column=2, row =0)

#is equal to
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row =1)

#result kilometers
kilometers_of_miles = Label(text="0")
kilometers_of_miles.grid(column=1, row =1)

#kilometers label
kilometers = Label(text="Km")
kilometers.grid(column=2, row =1)

#button
def button_clicked():
    kms = round(float(miles_input.get())*1.609,2)
    kilometers_of_miles.config(text=kms)

button = Button(text="calculate", command=button_clicked)
button.grid(column=1 , row = 2)

window.mainloop()