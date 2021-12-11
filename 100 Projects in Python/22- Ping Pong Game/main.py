from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor('black')
screen.title("Nick Raj Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    r_paddle.check_color()
    l_paddle.check_color()

    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.bounce_y()
    if ball.distance(r_paddle) < 80 and ball.xcor() > 310 or ball.distance(l_paddle) < 80 and ball.xcor() < -310:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.count_score_l_paddle()
        time.sleep(1)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.count_score_r_paddle()
        time.sleep(1)

screen.exitonclick()

