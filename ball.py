from turtle import Turtle, Screen 
# import random *

screen = Screen()
screen.listen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)

