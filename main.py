#turtle race
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500 , height = 400)
userbet = screen.textinput( title = "Make your bet : " , prompt = "Which turtle will win the race? Choose a color : ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cor = [-100, 100, -60, 60, -20, 20]
total_turtles = []

for index in range(6):
    mr_turtle = Turtle(shape = "turtle")
    mr_turtle.penup()
    mr_turtle.color(color[index])
    mr_turtle.goto( x =  -230 , y = y_cor[index])
    total_turtles.append(mr_turtle)

race = False
if userbet:
    race = True

while race:
    for turtle in total_turtles:
        if turtle.xcor() > 230: 
            race = False
            winner = turtle.pencolor()
            if winner == userbet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        random_pace = random.randint(0,10)
        turtle.forward(random_pace)
 
screen.exitonclick()
