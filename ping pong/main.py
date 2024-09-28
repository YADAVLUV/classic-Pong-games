import time
from turtle import Screen
from paddle import paddle
from ball import ball
from scoreboard import Scoreboard
from line import CenterLine

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

center_line = CenterLine()

r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))

ball = ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        screen.tracer(0)
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.l_score == 10:
            scoreboard.display_winner("Left Player")
            game_is_on = False
        screen.tracer(1)

    if ball.xcor() < -380:
        screen.tracer(0)
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.r_score == 10:
            scoreboard.display_winner("Right Player")
            game_is_on = False
        screen.tracer(1)

screen.exitonclick()
