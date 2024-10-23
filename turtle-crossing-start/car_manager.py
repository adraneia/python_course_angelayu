from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random.randint(0, 5)])
        self.penup()
        self.goto(280,random.randint(-250, 250))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed("slowest")
        # self.go_left()


    def go_left(self):
        new_x = self.xcor() - 1
        self.goto(new_x, self.ycor())


