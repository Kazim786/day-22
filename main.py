from turtle import Turtle, Screen 
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")



paddle = Paddle((350, 0))

paddle_2 = Paddle((-350, 0))


screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")



game_is_on = True 

while game_is_on:
    screen.update()




screen.exitonclick()