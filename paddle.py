from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(350, 0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=15, stretch_wid=0.5)
        # self.goto(350, 0)
        


    def up(self):
        self.penup()
        self.setheading(0)
        self.forward(20)   



    def down(self):
        self.penup()
        self.setheading(0)
        self.backward(20)        