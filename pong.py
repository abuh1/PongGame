import turtle
from turtle import Turtle

# Set up window of game
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor('#5d73e3')
win.setup(width=800, height=600)
win.tracer(0)
# Class for paddles
class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos_x, pos_y)#
        
# Class for ball
class Ball(Turtle):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(pos_x, pos_y)   
        
# Creating both paddles and ball 
paddle1 = Paddle(-375, 0)
paddle2 = Paddle(375, 0)
ball = Ball()
# Functions to move paddles up or down
def pad1_up():
    y = paddle1.ycor()
    y += 15
    paddle1.sety(y)
def pad1_down():
    y = paddle1.ycor()
    y -= 15
    paddle1.sety(y)
def pad2_up():
    y = paddle2.ycor()
    y += 15
    paddle2.sety(y)
def pad2_down():
    y = paddle2.ycor()
    y -= 15
    paddle2.sety(y)

# Keyboard controls
win.listen()
win.onkeypress(pad1_up, "w")
win.onkeypress(pad1_down, "s")
win.onkeypress(pad2_up, "Up")
win.onkeypress(pad2_down, "Down")
# Main function
def main():
    # Main game loop
    while True:
        win.update()



if __name__ == '__main__':
    main()