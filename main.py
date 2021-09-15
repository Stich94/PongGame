from turtle import Turtle, Screen
from paddle import Paddle

# screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # turn off the animation for moving from the center to the new pos

paddle = Paddle()
# first is the listen required on the screen after that is the onkey
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

# required to call a update every single time when using .tracer()
game_is_on = True
while game_is_on:
    screen.update()

# Write the Paddle Class and Create the Second Paddle

screen.exitonclick()