import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your Bet", prompt= 'Which turtle will win the race? \n ["red", "orange", "yellow", "blue", "purple"] \n Enter the color: ')
colors = ["red", "orange", "yellow", "blue", "purple"]
all_turtle = []
x= -230
y= -100

if user_bet:
    race_is_on = True


for color in colors:
    name_of_turtle = color
    name_of_turtle = Turtle()
    name_of_turtle = Turtle(shape="turtle")
    name_of_turtle.penup()
    name_of_turtle.goto(x, y)
    name_of_turtle.color(f"{color}")
    y += 50
    all_turtle.append(name_of_turtle)


while race_is_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0,15))
        if (turtle.position()[0] > 220):
            if user_bet == turtle.pencolor():
                print(f"Your Bid : {user_bet}")
                print("User Won!!!!")
            else:
                print(f"Your Bid: {user_bet}")
                print("You Lose!!!!")
                print(f"{turtle.pencolor()} has won the race.")
            race_is_on = False


screen.exitonclick()