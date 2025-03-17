from turtle import Turtle, Screen
import random

game_on = False
colors =  ["red", "purple", "blue", "green", "yellow", "orange"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will wind the race? Enter a color: ")
turtles = []
x = -230
y = -100

for _ in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[_].color(colors[_])
    turtles[_].penup()
    turtles[_].goto(x, y)
    y += 40

if user_bet:
    game_on = True

while game_on:
    rnd_distance = random.randint(0, 10)
    rnd_turtle = random.randint(0, 5)
    turtles[rnd_turtle].forward(10)

    if turtles[rnd_turtle].xcor() == 250:
        print(f"The {turtles[rnd_turtle].color()[0]} turtle is the winner!")
        game_on = False
        if user_bet == turtles[rnd_turtle].color()[0]:
            print("You win!")
        else:
            print("You lose!")

screen.exitonclick()