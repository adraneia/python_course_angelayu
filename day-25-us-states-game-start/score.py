from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, score):
        self.clear()
        self.goto(-100, 200)
        self.write(score, align="center", font=("Courier", 80, "normal"))