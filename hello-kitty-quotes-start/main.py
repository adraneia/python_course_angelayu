from tkinter import *
import requests

def get_quote():
    response = requests.get("https://www.affirmations.dev/")
    response.raise_for_status()
    data = response.json()
    quote=data["affirmation"]
    canvas.itemconfig(quote_text, text = quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="photo2.PNG")
canvas.create_image(150, 200, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=255, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kitty_img = PhotoImage(file="hello-kitty.png")
kitty_button = Button(image=kitty_img, highlightthickness=0, command=get_quote)
kitty_button.grid(row=1, column=0)



window.mainloop()