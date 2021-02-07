from turtle import Turtle, Screen

screen = Screen()

class Scoreboard(Turtle):
    def init(self):

        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        
        self.penup()

        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", True, align= "center", font= ("Arial", 24, "normal"))

        self.goto(100, 200)
        self.write(f"{self.r_score}", True, align= "center", font= ("Arial", 24, "normal"))





    def left_point(self):
        
        # self.clear()
        self.l_score+=1
        self.update_scoreboard()
        # self.write(f"Score: {self.l_score}", True, font= ("Arial", 24, "normal"))

    def right_point(self):
        
        # self.clear()
        self.r_score+=1
        self.update_scoreboard()
        # self.write(f"Score: {self.r_score}", True, font= ("Arial", 24, "normal"))