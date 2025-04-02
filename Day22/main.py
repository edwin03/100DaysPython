from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

game_is_on = True

while game_is_on:
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")
    screen.update()  

screen.exitonclick()