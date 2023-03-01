import time
from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
move_ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


is_game_on = True
while is_game_on:
    time.sleep(move_ball.move_speed)
    move_ball.move()

    if move_ball.ycor() > 280 or move_ball.ycor() < -280:
        move_ball.bounce_y()

    if move_ball.distance(l_paddle) <50 and move_ball.xcor() < -320 or \
            move_ball.distance(r_paddle) <50 and move_ball.xcor() > 320:
        move_ball.bounce_x()

    if move_ball.xcor()>380:
        move_ball.center()
        scoreboard.l_point()


    if move_ball.xcor() < -380:
        move_ball.center()
        scoreboard.r_point()





screen.exitonclick()