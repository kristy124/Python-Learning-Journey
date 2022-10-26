from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# screen = Screen()
# screen.setup(width=600, height=600)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(305, random.randint(-250, 250))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT


# screen.exitonclick()