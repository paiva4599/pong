from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

display = Screen()
display.setup(width=800, height=600)
display.tracer(0)
display.bgcolor("black")
display.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

display.listen()
display.onkeypress(r_paddle.move_up, key="Up")
display.onkeypress(r_paddle.move_down, key="Down")
display.onkeypress(l_paddle.move_up, key="w")
display.onkeypress(l_paddle.move_down, key="s")

game_is_on = True

while game_is_on:
    display.update()
    time.sleep(ball.move_speed)
    ball.movement()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #Detect collision with the paddle
    if ((ball.xcor() > 320 and ball.distance(r_paddle) < 50) or
            (ball.xcor() < -320 and ball.distance(l_paddle) < 50)):
        ball.paddle_bounce()

    #Detect if right paddle misses
    if ball.xcor() > 400:
        ball.goto(0,0)
        scoreboard.increase_l_score()
        scoreboard.clear()
        scoreboard.write_scoreboard()
        scoreboard.separator()
        ball.move_speed = 0.1

    # Detect if left paddle misses
    if ball.xcor() < -400:
        ball.goto(0, 0)
        scoreboard.increase_r_score()
        scoreboard.clear()
        scoreboard.write_scoreboard()
        scoreboard.separator()
        ball.move_speed = 0.1

    #Condition to win
    if scoreboard.l_score == 3:
        scoreboard.print_winner("Left Player Wins!")
        game_is_on = False
    elif scoreboard.r_score == 3:
        scoreboard.print_winner("Right Player Wins!")
        game_is_on = False

display.exitonclick()
