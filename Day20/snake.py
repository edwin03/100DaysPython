from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            self.turtles.append(Turtle(shape="square"))
            self.turtles[_].color("white")
            self.turtles[_].penup()
            self.turtles[_].goto(STARTING_POSITIONS[_])

    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            self.turtles[seg_num].goto(self.turtles[seg_num-1].pos())
        self.turtles[0].forward(MOVE_DISTANCE)