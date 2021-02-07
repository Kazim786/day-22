from turtle import Turtle, Screen

screen = Screen()

class Scoreboard(Turtle):
    def init(self):

        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()

        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", True, align= "center", font= ("Arial", 24, "normal"))
        