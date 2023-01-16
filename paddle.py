from turtle import Turtle
from constants import *


class Paddle(Turtle):
    def __init__(self, screen,pos=( WIDTH// 2 - 50, 0)):
        super().__init__()
        # self.pp_scr = pp_screen
        self.scr = screen
        self.post=pos
        self.customize_pad()

    def customize_pad(self):
        self.color(FG_COLOR)
        self.turtlesize(stretch_wid=PAD_H / 20, stretch_len=PAD_W / 20)
        self.penup()
        self.shape("square")
        self.setposition(self.post)

    def move_up(self):
        if self.ycor()+PAD_H//2<HEIGHT//2:
            self.goto((self.xcor(),self.ycor()+STEPS))

    def move_down(self):
        if self.ycor()-PAD_H//2 > -HEIGHT//2:
            self.goto((self.xcor(),self.ycor()-STEPS))

    def key_controls(self,player=1):
        """player argument takes 1 or 2"""
        keys={1:("Up","Down"), 2:("w","s")}
        self.scr.onkeypress(self.move_up, keys[player][0])
        self.scr.onkeypress(self.move_down, keys[player][1])
