from turtle import Screen, Turtle
from constants import HEIGHT, WIDTH,FG_COLOR


class PPScreen:
    def __init__(self):
        self.scr = Screen()
        self.customize_scr()
        self.x = self.scr.window_width() - 20
        self.y = self.scr.window_height() - 20
        self.score = Turtle()
        self.score.hideturtle()
    def customize_scr(self):
        self.scr.tracer(0)
        self.scr.bgcolor("black")
        self.scr.setup(width=WIDTH, height=HEIGHT)
        self.draw_net()

    def draw_net(self):
        net = Turtle()
        net.shape("turtle")
        net.color(FG_COLOR)
        net.hideturtle()
        net.penup()
        net.pensize(8)
        net.setposition((0, HEIGHT//2-5))
        net.setheading(270)
        net.pendown()
        net.forward(HEIGHT)



    def show_score(self):
        self.score.penup()
        self.score.setposition((0,HEIGHT//2 - 80))
        self.score.color(FG_COLOR)
        self.score.write(f"{0} {0}", True, align="center", font=('Arial', 50, 'bold'))
    def score_update(self, ls=0,rs=0):
        self.score.clear()
        self.score.setposition((0,HEIGHT//2 - 80))
        self.score.write(f"{ls} {rs}", True, align="center", font=('Arial', 50, 'bold'))

    def show_game_over(self):
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition((-30, 0))
        turtle.color("red")
        turtle.write(f"Game Over", True, align="center", font=('Arial', 20, 'bold'))


if __name__ == "__main__":
    scr = PPScreen()


    scr.scr.update()
    scr.scr.exitonclick()
