from turtle import Turtle, Screen
import heroes
import villains
from random import randint

print(heroes.gen())
print(villains.gen())

tim = Turtle()
tim.shape("turtle")
tim.color("OliveDrab4")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

screen = Screen()
screen.colormode(255)

for sides in range(3, 11):
    angle = 360/sides
    tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    for _ in range(1, sides+1):
        tim.right(angle)
        tim.forward(100)
    
screen.exitonclick()