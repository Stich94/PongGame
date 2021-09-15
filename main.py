from turtle import Turtle, Screen
from paddle import Paddle

# screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # turn off the animation for moving from the center to the new pos

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
# first is the listen required on the screen after that is the onkey
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# required to call a update every single time when using .tracer()
game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()