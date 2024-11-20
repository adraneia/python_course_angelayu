import turtle
import pandas
from states import States
from score import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = States()
scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
print(data["state"])
data_list = data["state"].to_list()

#FILTERING ROWS
# row_of_answer_state = data[data.state == answer_state]
# print(row_of_answer_state)
# print(data[data.state == answer_state].x)
# x_position = data[data.state == answer_state].x
# y_position = data[data.state == answer_state].y

while len(state.list_of_found_states) < 50:
    answer_state = screen.textinput(title=f"{len(state.list_of_found_states)} / 50 States Correct", prompt="Whats another state's name? ").title()
    print(answer_state)
    if answer_state == "Exit":

        break
    if answer_state in data_list:
        x_position = int(data[data.state == answer_state].x)
        y_position = int(data[data.state == answer_state].y)
        state.create_state((x_position, y_position), answer_state)
        print("slay")
        print(state.list_of_found_states)
        scoreboard.update_scoreboard(len(state.list_of_found_states))
turtle.mainloop()

#states to learn.csv
#states to learn.csv
print(state.list_of_found_states)
print(data_list)

states_to_learn = [item for item in state.list_of_found_states if item not in state.list_of_found_states]
#states_to_learn = []
# for element in data_list:
#     if element not in state.list_of_found_states:
#         states_to_learn.append(element)

states_to_learn_dict = {
     "states to learn" : states_to_learn
 }
states_to_learn_df = pandas.DataFrame(states_to_learn_dict)
states_to_learn_df.to_csv("states_to_learn.csv")




