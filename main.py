from turtle import Turtle, Screen
import random
race_is_on = True
screen = Screen()
screen.setup(width=650, height=400)

colors = ["red", "green", "yellow", "blue"]
yposition=[20,40,60,80]
all_turtles=[]
user_bet=screen.textinput("turtle race", " please insert color you are betting on. ")
for x in range(len(colors)):
    rania = Turtle()
    rania.shape("turtle")
    rania.color(colors[x])
    rania.penup()
    rania.setposition(-300, yposition[x])
    all_turtles.append(rania)
while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("you won")
            else:
                print(f"you lost! the winner is {winner} turtle")

        random_move= random.randint(0, 30)
        turtle.forward(random_move)

screen.exitonclick()