from turtle import Turtle, Screen

colors =  ["red", "purple", "blue", "green", "yellow", "orange"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will wind the race? Enter a color: ")
print(user_bet)
turtles = []
x = -230
y = -100

for _ in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[_].color(colors[_])
    turtles[_].penup()
    turtles[_].goto(x, y)
    y += 40

screen.exitonclick()