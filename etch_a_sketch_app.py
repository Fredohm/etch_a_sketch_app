from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed("fastest")
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def counter_clockwise():
    turtle.left(1)


def clockwise():
    turtle.right(1)


def clear_drawing():
    turtle.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear_drawing)

screen.exitonclick()
