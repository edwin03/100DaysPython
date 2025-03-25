from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
