from turtle import Turtle, Screen
import heroes, villains, random
from random import randint

print(heroes.gen())
print(villains.gen())

tim = Turtle()
tim.shape("turtle")
tim.color("OliveDrab4")
tim.pensize(1)
tim.speed("fastest")
loops = 72


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

# for sides in range(3, 11):
#     angle = 360/sides
#     tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     for _ in range(1, sides+1):
#         tim.right(angle)
#         tim.forward(100)

# # Random walk challange
# for _ in range(loops):
#     tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     tim.setheading(random.choice([0, 90, 180, 270]))
#     tim.fd(30)

# Spirograh challange
for _ in range(loops):
    tim.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    tim.setheading(tim.heading() + 5)
    tim.circle(100)
    
screen.exitonclick()