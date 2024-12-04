from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn= {}
#Create a dictionary in this format: [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}..
try:
    french_data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = french_data_df.to_dict(orient="records")


# french_data_df = pandas.read_csv("data/french_words.csv")
# print(french_data_df)
#
# #to_learn = french_data_df.to_dict()
# to_learn = french_data_df.to_dict(orient="records")
# print(to_learn)
#
# # french_dict = {row.French: row.English for (index, row) in french_data_df.iterrows()}
# # print(french_dict)

#---------------------NEXT CARD--------------------
def next_card():
    print("next_card")
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text = "French", fill="black")
    canvas.itemconfig(word_text, text =current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)
    # print(current_card)
    # print(current_card["French"])
    # print(current_card["English"])

#---------------------FLIP CARD--------------------
def flip_card():
    print("flip_card")
    canvas.itemconfig(canvas_image, image=card_back_png)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text =current_card["English"], fill="white")
#---------------------SAVE PROGRESS--------------------
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg = BACKGROUND_COLOR)

card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400,263, image = card_front_png)
title_text = canvas.create_text(400,150,text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263,text="", fill="black", font=("Ariel", 60, "italic"))
canvas.grid(column=0, row =0, columnspan=2)

wrong_png = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_png,highlightthickness=0,command=next_card)
wrong_button.grid(column=0 , row = 1)

right_png = PhotoImage(file="images/right.png")
right_button = Button(image=right_png,highlightthickness=0,command=is_known)
right_button.grid(column=1 , row = 1)

next_card()

window.mainloop()