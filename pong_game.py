from turtle import Screen, Turtle
from pong_paddle import Paddle
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


midline = Turtle()
midline.penup()
midline.goto(0, 300)
midline.width(5)
midline.color("white")
midline.setheading(270)
midline.hideturtle()
for i in range(20):
    midline.pendown()
    midline.forward(20)
    midline.penup()
    midline.forward(15)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

def start_pong():
    screen.listen()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect ball collision with wall and bounce.
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles.
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect when R paddle misses.
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
        # Detect when L paddle misses.
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        if scoreboard.l_score == 5:
            game_is_on = False
            scoreboard.left_wins()

        if scoreboard.r_score == 5:
            game_is_on = False
            scoreboard.right_wins()

    play_again = screen.textinput(title="Rematch?", prompt="Type 'y' to play again, or 'n' to exit game: ").lower()
    if play_again == 'y':
        scoreboard.rematch()
        start_pong()


start_pong()

screen.exitonclick()