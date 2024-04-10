from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


#create the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)


#create and move a paddle (width = 20, height=100, xpos = 350, y=0)


l_paddle = Paddle((-350,0))
l_score = Scoreboard((-100,250))

r_paddle = Paddle((350,0))
r_score = Scoreboard((100, 250))


paddles = [l_paddle, r_paddle]
ball = Ball()




screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    #Detect h wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collesion with v walls
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or \
            ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #Detect R paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) > 50:
        l_score.increase_score()
        ball.ball_reset()

    #Detect L paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) > 50:
        r_score.increase_score()
        ball.ball_reset()




screen.exitonclick()