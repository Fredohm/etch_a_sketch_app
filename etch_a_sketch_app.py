from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed("fastest")
turtle.shape("turtle")
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_counter_clockwise():
    turtle.left(10)


def turn_clockwise():
    turtle.right(10)


def clear_drawing():
    turtle.reset()


def pen_up():
    turtle.penup()


def pen_down():
    turtle.pendown()


screen.listen()
screen.onkeypress(move_forwards, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(turn_counter_clockwise, "Left")
screen.onkeypress(turn_clockwise, "Right")
screen.onkeypress(clear_drawing, "space")
screen.onkey(pen_up, "a")
screen.onkey(pen_down, "z")

screen.exitonclick()
