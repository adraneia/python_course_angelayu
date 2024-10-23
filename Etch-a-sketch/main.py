from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(25)

def move_clockwise():
    tim.right(25)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = move_counter_clockwise)
screen.onkey(key = "d", fun = move_clockwise)
screen.onkey(key = "c", fun = clear)

screen.exitonclick()