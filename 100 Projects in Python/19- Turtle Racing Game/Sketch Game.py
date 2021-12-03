from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clearscreen, "c")


screen.exitonclick()