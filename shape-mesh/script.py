from turtle import Turtle, Screen
from random import choice

turtle = Turtle()
screen = Screen()

turtle.penup()
turtle.setx(-100)
turtle.sety(250)
turtle.pendown()

color_list = ["red", "green", "orange", "blue", "black", "purple", "gray"]

for side in range(4, 11):
    turtle.color(choice(color_list))
    for line in range(side):
        turtle.forward(200)
        turtle.right(360 / side)

screen.exitonclick()
