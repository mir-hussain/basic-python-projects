from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.bgcolor("#FFDDE1")
turtle.width(3)

turtle.fillcolor("#C4335C")
turtle.color("#C4335C")
turtle.begin_fill()
turtle.right(-45)
turtle.forward(141)
turtle.circle(70, 180)
turtle.right(90)
turtle.circle(70, 180)
turtle.forward(141)
turtle.end_fill()
turtle.right(45)
turtle.penup()
turtle.forward(90)
turtle.pendown()
turtle.left(90)
turtle.width(10)
turtle.circle(200)


screen.exitonclick()
