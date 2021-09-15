from turtle import Turtle

# Write the Paddle Class and Create the Second Paddle

class Paddle():
    def __init__(self):
        self.createPaddle()


    # create paddle 
    def createPaddle(self):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.goto(x=350, y=0)
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1) # because the default size is 20 by 20 so we have to stretch it by 5 in the wid
    
    # moving paddle up or down
    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)
    
    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

        