from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def move_up(self):
        new_y_cord = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_cord)

    def move_down(self):
        new_y_cord = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cord)
