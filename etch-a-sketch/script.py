from turtle import Turtle, Screen


pen = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    pen.forward(20)


def turn_right():
    pen.right(20)


def turn_left():
    pen.left(20)


def backward():
    pen.backward(20)


def clear():
    pen.penup()
    pen.clear()
    pen.home()
    pen.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=backward)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
