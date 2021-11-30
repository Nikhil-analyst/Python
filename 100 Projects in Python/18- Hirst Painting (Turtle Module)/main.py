import random
import turtle
from turtle import Turtle, Screen
from random import Random
tim = Turtle()
screen = Screen()
screen.colormode(255)
turtle.pen(pensize= 100)
def shape(sides, length):
    red = (random.randint(0,255))
    green = (random.randint(0,255))
    blue = (random.randint(0,255))
    tim.color(red, green, blue)
    for _ in range(sides):
        tim.forward(length)
        tim.right(360 / sides)

def random_walk():
    red = (random.randint(0,255))
    green = (random.randint(0,255))
    blue = (random.randint(0,255))
    tim.color(red, green, blue)
    direction = (0,90,180,270)
    tim.setheading(random.choice(direction))
    tim.forward(20)

tim.pensize()
tim.speed("fastest")


def draw_circle(radius, rotate):
    red = (random.randint(0,255))
    green = (random.randint(0,255))
    blue = (random.randint(0,255))
    tim.color(red, green, blue)
    tim.setheading(rotate)
    tim.circle(radius)
angle =0
while angle <= 360:
    angle += 5
    draw_circle(radius= 100,rotate = angle )

screen.exitonclick()

