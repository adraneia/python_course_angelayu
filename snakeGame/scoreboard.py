from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        #self.create_scoreboard()
        self.score = 0
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 34, "normal"))

    def update_scoreboard(self):
        self.score +=1
        print(self.score)
        self.clear()
        self.write_scoreboard()

