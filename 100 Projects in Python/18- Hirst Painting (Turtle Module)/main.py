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
        tim.right(360/sides)

for i in range(3,10):
    shape(i, 100)


screen.exitonclick()