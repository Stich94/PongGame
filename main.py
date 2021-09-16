from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # turn off the animation for moving from the center to the new pos

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
# first is the listen required on the screen after that is the onkey
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")




# required to call a update every single time when using .tracer()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball. ycor() > 280 or ball. ycor() < -280:
        # needs to bounce_y
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.bounce_x()
        
    # Detect right paddle miss
    if ball.xcor() > 380:
        print("out of screen")
        ball.reset_position()
        
    # Detect left paddle miss
    if ball.xcor() < -380:
        print("out of screen")
        ball.reset_position()


screen.exitonclick()