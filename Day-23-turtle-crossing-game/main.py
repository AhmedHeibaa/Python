import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()
player.create_player()
screen.listen()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #Detect collision with cars
    for car in car_manager.allCars:
        
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            
    #Detect collision with finish line
    if player.ycor() > player.finish_line:
        score.increment_score()
        player.go_to_start()
        car_manager.increase_speed()
screen.exitonclick()