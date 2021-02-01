from turtle import Turtle, Screen 
# import random *

screen = Screen()
screen.listen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        
        self.goto(0, 0)
        

    def move(self):
        
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

