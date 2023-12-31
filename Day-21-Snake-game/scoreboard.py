from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        # self.write(f"score = {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        self.update_score()
        # self.game_over()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center",font=("Arial",22,"normal"))
    def update_score(self):
        self.clear()
        self.write(f"score = {self.score}",align="center",font=("Arial",22,"normal"))
        self.score += 1