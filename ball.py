from turtle import Turtle
from constants import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.customize_ball()
        self.x_side = 1
        self.y_side = 1
        self.move_speed =0.1
    def customize_ball(self):
        self.color("white")
        self.penup()
        self.shape("circle")
        self.turtlesize(stretch_wid=BALL_S / 20, stretch_len=BALL_S / 20)

    def move(self):
        self.goto((self.xcor() + self.x_side * BALL_STEPS, self.ycor() + self.y_side * BALL_STEPS))

    def bounce_y(self):
        self.y_side *= -1

    def bounce_x(self):
        self.x_side *= -1
        self.move_speed *=0.9
    def reset(self):
        self.setposition((0, 0))
        self.x_side *= -1
        self.move_speed = 0.1
    # def move_down_right(self):
    #     self.goto((self.xcor()+10,self.ycor()-10))
    #
    # def move_up_left(self):
    #     self.goto((self.xcor()-10,self.ycor()+10))
    #
    # def move_down_left(self):
    #     self.goto((self.xcor()-10,self.ycor()-10))
