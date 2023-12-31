from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) :
        super().__init__()
        self.allCars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2 )
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-230,230)
            new_car.goto(300,rand_y)
            self.allCars.append(new_car)
    def move_cars(self):
        for car in self.allCars:
            car.backward(self.car_speed)
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT