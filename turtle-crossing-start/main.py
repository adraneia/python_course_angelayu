import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
#car = CarManager()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down,"Down")
screen.onkey(turtle.up,"w")
screen.onkey(turtle.down,"s")

times_slept = 0
game_is_on = True
while game_is_on:
    times_slept += 1
    time.sleep(0.1)
    if times_slept % 6 == 0:
        car = CarManager()
        times_slept = 0
    if car.xcor() > -300:
        car.go_left()

    screen.update()


screen.exitonclick()