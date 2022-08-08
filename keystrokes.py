from turtle import *

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clock_wise():
    tim.right(10)


def clear():
    tim.clear()
    tim.setheading(0)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
