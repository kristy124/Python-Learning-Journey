import time
from turtle import Screen
from turtle_crossing_player import Player
from turtle_crossing_car_manager import CarManager
from turtle_crossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars
    if loop_counter % 6 == 0:
        car_manager.create_car()
    loop_counter += 1
    car_manager.move()

    # Detect when turtle crosses finish line
    if turtle.ycor() > 280:
        turtle.reset_position()
        car_manager.next_level()
        scoreboard.level_up()

    # Detect when cars collide with turtle
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()