from turtle import Turtle, Screen
from random import randint, choice


pen = Turtle()
screen = Screen()

pen.shape("circle")
pen.width(10)
pen.speed(100)
color_list = ["red", "green", "orange", "blue", "black", "purple", "gray"]


for number in range(500):
    pen.color(choice(color_list))
    pen.right(45 * randint(0, 10))
    pen.forward(30)

screen.exitonclick()
