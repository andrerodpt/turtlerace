from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
all_turtles = []


new_y = -150
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.speed('fastest')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=new_y)
    all_turtles.append(new_turtle)
    new_y += 50

if user_bet:
    is_race_on = True

def check_winner(turtle):
    if turtle.xcor() > 230:
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner.")
        else:
            print(f"You've lost! The {winning_color} turtle is the winner.")
        return False
    return True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        is_race_on = check_winner(turtle)
        if not is_race_on:
            break

screen.exitonclick()