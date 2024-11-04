import turtle
import pandas
from states import States
import keyboard
from score import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = States()
scoreboard = Scoreboard()

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#screen.exitonclick()

#state = States((100,100), "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name? ").title()
# print(answer_state)

data = pandas.read_csv("50_states.csv")
print(data["state"])
data_list = data["state"].to_list()

#FILTERING ROWS
# row_of_answer_state = data[data.state == answer_state]
# print(row_of_answer_state)
# print(data[data.state == answer_state].x)
# x_position = data[data.state == answer_state].x
# y_position = data[data.state == answer_state].y



game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name? ").title()
    print(answer_state)
    if answer_state in data_list:
        x_position = int(data[data.state == answer_state].x)
        y_position = int(data[data.state == answer_state].y)
        state.create_state((x_position, y_position), answer_state)
        print("slay")
        #getattr(student, "student_name")
        print(state.list_of_found_states)
        #print(dir(state.list_of_found_states))


        #game_is_on = str(screen.textinput(title="Guess the State", prompt="Do you want to guess again? (y / n)"))
        game_is_on = not keyboard.is_pressed('q')
    scoreboard.update_scoreboard(len(state.list_of_found_states))

turtle.mainloop()