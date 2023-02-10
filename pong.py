import turtle
from turtle import Turtle
# Globals
WIDTH, HEIGHT = 1100, 750
# Set up window of game
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor('#3e4f59')
win.setup(WIDTH, HEIGHT)
win.tracer(0)
# Class for paddles
class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("#778aed")
        self.penup()
        self.shapesize(stretch_wid=5.25, stretch_len=0.75)
        self.goto(pos_x, pos_y)
        
# Class for ball
class Ball(Turtle):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()
        self.speed('fastest')
        self.shape("circle")
        self.color("#a0ebde")
        self.penup()
        self.goto(pos_x, pos_y)   
        self.dx = 0.25
        self.dy = 0.25
# Creating both paddles and ball 
paddle1 = Paddle(-515, 0)
paddle2 = Paddle(515, 0)
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
# w and s for left paddle
win.onkeypress(pad1_up, "w")
win.onkeypress(pad1_down, "s")
# Up and Down arrow keys for right paddle
win.onkeypress(pad2_up, "Up")
win.onkeypress(pad2_down, "Down")
# Scores
p1_score = 0
p2_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write(f"{p1_score} - {p2_score}", align="center", font=("Arial", 18, "bold"))
# Main function
def main():
    # Main game loop
    while True:
        win.update()
        # Move ball initially
        ball.setx(ball.xcor() - ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Bounce off top and bottom border
        if ball.ycor() > 365:
            ball.sety(365)
            ball.dy *= -1
        elif ball.ycor() < -360:
            ball.sety(-360)
            ball.dy *= -1
        # Resets ball if goes off left or right
        if ball.xcor() > 600:
            ball.goto(0, 0)
            ball.dx *= -1
            global p1_score, p2_score
            p1_score += 1
            pen.clear()
            pen.write(f"{p1_score} - {p2_score}", align="center", font=("Arial", 18, "bold"))
        elif ball.xcor() < -600:
            ball.goto(0, 0)
            ball.dx *= -1
            p2_score += 1
            pen.clear()
            pen.write(f"{p1_score} - {p2_score}", align="center", font=("Arial", 18, "bold"))
        # Collision with paddles
        if (ball.xcor() < paddle1.xcor() + 20) and (ball.ycor() in range(paddle1.ycor() - 70, paddle1.ycor() + 70)):
            ball.setx(paddle1.xcor() + 20)
            ball.dx *= -1
        elif (ball.xcor() > paddle2.xcor() -20) and (ball.ycor() in range(paddle2.ycor() - 70, paddle2.ycor() + 70)):
            ball.setx(paddle2.xcor() - 20)
            ball.dx *= -1

if __name__ == '__main__':
    main()