
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.colormode(255)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle is going to win the race ? Enter a color: \n")
screen.setup(width=500, height=400)


y_position =[-60, -30, 10, 40]
color_turtles = ["blue", "green", "yellow", "red"]
all_turtles = []

for turtle_index in range(4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_turtles[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()#pen color is the body of the turtle
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner")
            else:
                print(f"You Lost ! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()