from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import Score_board
RIGHT_PADDLE_POSITION = (350,0)
LEFT_PADDLE_POSITION = (-350,0)
GAME_BALL_POSITION = (0,0)
screen = Screen()
screen.setup(800,600,None,None)
screen.bgcolor("black")
screen.title("PING PONG")
# to remove animation
screen.tracer(0)
right_paddle = Paddle()
left_paddle = Paddle()
game_ball = Ball()
score_board = Score_board()
right_paddle.create_paddle(RIGHT_PADDLE_POSITION)
left_paddle.create_paddle(LEFT_PADDLE_POSITION)
game_ball.create_ball(GAME_BALL_POSITION)

screen.listen()
screen.onkey(right_paddle.go_paddle_up,"Up")
screen.onkey(right_paddle.go_paddle_down,"Down")
screen.onkey(left_paddle.go_paddle_up,"w")
screen.onkey(left_paddle.go_paddle_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    game_ball.move()
    
    #Detect collision with wall
    if game_ball.ycor() > 285 or  game_ball.ycor() < -285:
        game_ball.bounce_y()
    #Detect collision with right padel
    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()
    #Detect collision when right paddle missed the ball
    if game_ball.xcor() > 388:
        game_ball.reset_position()
        score_board.l_point()
    #Detect collision when left paddle missed the ball
    if game_ball.xcor() < -388:
        game_ball.reset_position()
        score_board.r_point()
screen.exitonclick()