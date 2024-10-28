from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.hideturtle()


    def create_car(self):

        new_car = Turtle("square")
        new_car.color(COLORS[random.randint(0, 5)])
        new_car.penup()
        new_car.goto(280,random.randint(-250, 250))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.speed("fast")
        self.list_of_cars.append(new_car)

    def move_increment(self):
         self.move_distance += MOVE_INCREMENT

    def go_left(self):
        for car in self.list_of_cars:
            car.backward(self.move_distance)
