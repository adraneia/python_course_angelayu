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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f"Score : {self.score}, High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 34, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



