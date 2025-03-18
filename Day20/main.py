from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

turtles = []
cords = [20, 0]

for _ in range(3):
    turtles.append(Turtle(shape="square"))
    turtles[_].color("white")
    cords[0] -= 20
    turtles[_].penup()
    turtles[_].goto(cords)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(turtles) - 1, 0, -1):
        turtles[seg_num].goto(turtles[seg_num-1].pos())
    turtles[0].forward(20)
    

screen.exitonclick()