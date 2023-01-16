# improvements
## change the angle ang speed when hit the paddle

from turtle import Turtle
from screen import PPScreen
from paddle import Paddle
from ball import Ball
from constants import *

pp_scr = PPScreen()
scr = pp_scr.scr

r_paddle = Paddle(scr, pos=(WIDTH // 2 - 50, 0))
l_paddle = Paddle(scr, pos=(-WIDTH // 2 + 50, 0))
ball = Ball()
scr.update()
scr.listen()
r_paddle.key_controls(1)
l_paddle.key_controls(2)

scr.update()


def is_collision_up_down(ball):
    if ball.ycor() > HEIGHT // 2 - 20 or ball.ycor() < -HEIGHT // 2 + 20:
        ball.bounce()

pp_scr.show_score()
ls=0; rs=0
pp_scr.score_update(ls=ls,rs=rs)
import time

while (1):
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > HEIGHT // 2 - 20 or ball.ycor() < -HEIGHT // 2 + 20:
        ball.bounce_y()
    if (ball.distance(l_paddle) < 55 and ball.xcor() < l_paddle.xcor() + 10) or (
            ball.distance(r_paddle) < 55 and ball.xcor() > r_paddle.xcor() - 10):

        ball.bounce_x()
    if ( ball.xcor() < l_paddle.xcor() ):
        rs+=1
        ball.reset()
    if (ball.xcor() > r_paddle.xcor()):
        ls+=1
        ball.reset()
    pp_scr.score_update(ls=ls,rs=rs)
    scr.update()

scr.exitonclick()
