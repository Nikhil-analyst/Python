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

# def random_walk():
#     direction = (90,270)
#     tim.right(random.choice(direction))
#     tim.forward(50)
# for _ in range(100):
#     random_walk()

for _ in range(10):
    shape(_,100)


screen.exitonclick()

