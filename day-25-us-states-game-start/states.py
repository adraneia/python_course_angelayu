from turtle import Turtle

class States(Turtle):

    def __init__(self):
        super().__init__()
        self.list_of_found_states = []
        self.hideturtle()


    def create_state(self, position, state_name):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.color("black")
        new_state.goto(position)
        new_state.write(state_name, font=('Arial', 12, 'normal'))
        #self.list_of_found_states.append(new_state)
        self.list_of_found_states.append(state_name)
