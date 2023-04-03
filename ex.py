from turtle import Turtle, Screen

mr_turtle = Turtle()
screen = Screen()

def move_forward():
    mr_turtle.forward(100)

def move_backward():
    mr_turtle.backward(100)

def turn_left():
    mr_turtle.left(10)

def turn_right():
    mr_turtle.right(10)

def clear_screen():
    mr_turtle.clear()

def reset_screen():
    mr_turtle.reset()

screen.listen()
screen.onkey(key = "w" , fun = move_forward)
screen.onkey(key = "s" , fun = move_backward)
screen.onkey(key = "a" , fun = turn_left)
screen.onkey(key = "d" , fun = turn_right)
screen.onkey(key = "c" , fun = clear_screen)
screen.onkey(key = "r" , fun = reset_screen)

screen.exitonclick()
