from turtle import Turtle

# Write the Paddle Class and Create the Second Paddle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1) # because the default size is 20 by 20 so we have to stretch it by 5 in the wid
        

    # moving paddle up or down
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        