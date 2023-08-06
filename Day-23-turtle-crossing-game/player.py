from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        
    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.go_to_start()
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def move_forward(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x,new_y)