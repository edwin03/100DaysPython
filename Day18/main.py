# import colorgram

# colors = colorgram.extract('image.jpg', 35)
# pallet = []

# for _ in range(35):
#     pallet.append((colors[_].rgb.r, colors[_].rgb.b, colors[_].rgb.b))

# print(pallet)

from turtle import Turtle, Screen
import random

color_list = [(253, 247, 247), (253, 252, 252), (235, 243, 243), (198, 32, 32), (248, 25, 25), (40, 188, 188), (244, 253, 253), (39, 69, 69), (238, 5, 5), (227, 49, 49), (29, 154, 154), (212, 15, 15), (17, 17, 17), (241, 161, 161), (195, 12, 12), (223, 120, 120), (68, 31, 31), (61, 8, 8), (223, 206, 206), (11, 62, 62), (219, 11, 11), (54, 229, 229), (19, 49, 49), (238, 216, 216), (79, 212, 212), (10, 238, 238), (73, 168, 168), (93, 198, 198), (65, 239, 239), (217, 51, 51), (6, 42, 42), (176, 233, 233), (239, 161, 161), (249, 48, 48), (5, 222, 222)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()
x = -250
y = -275

for _ in range(10):
    y += 50 
    tim.setpos(x, y)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        # tim.fillcolor(random.choice(color_list))
        # tim.begin_fill()
        # tim.circle(20)
        # tim.end_fill()
        tim.forward(50)

screen.exitonclick()