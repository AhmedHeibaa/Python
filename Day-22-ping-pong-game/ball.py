from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        
    def create_ball(self,position):
        self.shape("circle")
        self.color("white")
        # self.shapesize(5,1)
        self.penup()
        self.setposition(position)
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        #Reverse the direction in y axis
        self.y_move *= -1
    def bounce_x(self):
        #Reverse the direction in x axis
        self.x_move *= -1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        
        
        
    
