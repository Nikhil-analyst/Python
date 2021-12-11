from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 10, stretch_len=2)
        self.penup()
        self.goto(x_pos, 0)
        self.color("white")



    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

