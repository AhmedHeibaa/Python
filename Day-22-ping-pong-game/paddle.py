from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        
    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.setposition(position)
    
    def go_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def go_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)