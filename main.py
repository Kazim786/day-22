from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
# screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Paddle((350, 0))

left_pad = Paddle((-350, 0))

ball = Ball()
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(left_pad.up, "w")
screen.onkey(left_pad.down, "s")

game_is_on = True 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #To bounce the ball
    #this code is working
    if ball.distance(paddle) <= 10 or ball.distance(left_pad) <= 10:
        #probably going to have to change the ball's x and y coordinates
        print(ball.distance(paddle))

screen.exitonclick()