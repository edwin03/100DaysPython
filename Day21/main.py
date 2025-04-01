from turtle import Turtle, Screen

def up():
        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

def down():
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)


screen.listen()

game_is_on = True

while game_is_on:
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.update()  


screen.exitonclick()