from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
