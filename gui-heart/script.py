from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.bgcolor("#FFDDE1")
turtle.width(3)

# for _ in range(10):
#     turtle.circle(_ * 10)
# for _ in range(100):
#     turtle.right(-90 - _)
#     turtle.forward(200 - _)

turtle.fillcolor("#C4335C")
turtle.color("#C4335C")
turtle.begin_fill()
turtle.right(-45)
turtle.forward(141)
turtle.circle(70, 180)
turtle.right(90)
turtle.circle(70, 180)
turtle.forward(141)
turtle.right(45)
turtle.forward(140)
turtle.end_fill()

screen.exitonclick()
