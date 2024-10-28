import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

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
        times_slept = 0
        screen.update()
        car_manager.create_car()
    car_manager.go_left()

    for car in car_manager.list_of_cars:
        # DETECT collision with car
        if car.distance(turtle) < 20:
            game_is_on = False
            print("loser")
            scoreboard.game_over()

    # DETECT collision with top edge of the screen
    if turtle.ycor() > 280:
        turtle.refresh()
        car_manager.move_increment()
        print("yippee")
        scoreboard.increase_level()

    screen.update()

screen.exitonclick()