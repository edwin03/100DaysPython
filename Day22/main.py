from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball((0, 0))
sb = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.move_speed)

    # detect top and bottom hits
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect r_paddle misses
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        sb.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        sb.r_point()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    screen.update()  

screen.exitonclick()