import random
from turtle import Screen, Turtle
from colors import colors


def turtle_info():
    turtle_.shape("turtle")
    turtle_.pen(pendown=False, speed=10)
    turtle_.setx(-370)
    turtle_.sety(-300)


def first():
    for times in range(0, 20):
        turtle_.forward(35)
        turtle_.dot(30, str(colors[random.randint(0, 460)]))


def second():
    turtle_.left(90)
    turtle_.forward(35)
    turtle_.dot(30, str(colors[random.randint(0, 460)]))
    turtle_.left(90)
    for times in range(0, 19):
        turtle_.forward(35)
        turtle_.dot(30, str(colors[random.randint(0, 460)]))
    turtle_.right(90)
    turtle_.forward(35)
    turtle_.dot(30, str(colors[random.randint(0, 460)]))
    turtle_.right(90)
    for times in range(0, 19):
        turtle_.forward(35)
        turtle_.dot(30, str(colors[random.randint(0, 460)]))


turtle_ = Turtle()
turtle_info()
first()
second()
for i in range(0, 8):
    second()
screen = Screen()
screen.exitonclick()
