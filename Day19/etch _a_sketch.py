from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter():
    tim.setheading(tim.heading() + 10)

def clockwise():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.penup()
    tim.clear()
    tim.setpos(0, 0)
    tim.pendown()

screen.listen()
# this is a higher order function since it takes a function as an input
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(counter, key="a")
screen.onkey(clockwise, key="d")
screen.onkey(clear, key="c")

screen.exitonclick()
