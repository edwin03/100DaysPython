from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.add_segment(_)

    
    def add_segment(self, position):
            self.turtles.append(Turtle(shape="square"))
            self.turtles[-1].color("white")
            self.turtles[-1].penup()
            self.turtles[-1].goto(position)
    
    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.turtles[-1].position())


    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            self.turtles[seg_num].goto(self.turtles[seg_num-1].pos())
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].seth(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].seth(270)
    
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].seth(180)
    
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].seth(0)