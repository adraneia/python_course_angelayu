from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # password_letters = [new_item for item in list]
    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oooops", message=f"Make sure you havent left any fields empty !!!")
    else:
        # is_ok = messagebox.askokcancel(title=website_input.get(), message = f"These are the details entered: "
        #                                                                     f"\nEmail: {username_input.get()} "
        #                                                                     f"\nPassword: {password_input.get()} "
        #                                                                     f"\nIs it ok to save?")
        # if is_ok:
        #with open("password_manager.txt", mode="a") as file:
        # with open("password_manager_data.json", mode="w") as file:
        #     file.write(f"{website_input.get()}  |  {username_input.get()}  | {password_input.get()}\n")
        #     json.dump(new_data, file, indent=4)
        try:
            with open("password_manager_data.json", mode="r") as file:
                #reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager_data.json", "w") as file:
                json.dump(new_data, file, indent = 4)
        else:
            #updating old data with new data
            data.update(new_data)
            #print(type(data))
            with open("password_manager_data.json", "w") as file:
                #saving updated data
                json.dump(data,file,indent =4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = my_pass_png)
canvas.grid(column=1, row =0)

website_label = Label(text="Website:")
website_label.grid(column=0, row =1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row =2)

password_label = Label(text="Password:")
password_label.grid(column=0, row =3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.focus()
username_input.insert(0, "dummemail@gmail.com")


password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="generate password",highlightthickness=0,command=generate_password)
generate_password_button.grid(column=2 , row = 3)

add_button = Button(text="Add",highlightthickness=0,command=add,width=36 )
add_button.grid(column=1 , row = 4, columnspan=2)


window.mainloop()