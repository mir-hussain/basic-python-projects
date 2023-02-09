import turtle
from turtle import Turtle, Screen
from random import randint

pen = Turtle()
screen = Screen()

turtle.colormode(255)

pen.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return r, g, b


print(random_color())


for number in range(1, 73):
    pen.color(random_color())
    pen.circle(200)
    pen.home()
    pen.right(number * 5)

for number in range(1, 73):
    pen.color(random_color())
    pen.circle(100)
    pen.home()
    pen.right(number * 5)

screen.exitonclick()
