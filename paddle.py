from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(350, 0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        # self.goto(350, 0)
        


    def up(self):
        self.penup()
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y) 



    def down(self):
        self.penup()
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)        