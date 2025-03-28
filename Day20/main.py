from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
food.refresh()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

points = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # Detect collision with food. turtles[0] is the head.
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    # Detects collision with wall
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.turtles[1:0]:
        if snake.turtles[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # If head collides with any segment in the tail:
        # Trigger game_over



screen.exitonclick()