import turtle
from turtle import Turtle

# Set up window of game
def window_setup():
    wn = turtle.Screen()
    wn.title("Pong Game")
    wn.bgcolor('#5d73e3')
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn
# Class for paddles
class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos_x, pos_y)
        
# Class for ball
class Ball(Turtle):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(pos_x, pos_y)

# Main function
def main():
    window = window_setup()
    # Main game loop
    while True:
        window.update()
        # Initialise the paddles
        paddle_a = Paddle(-375, 0)
        paddle_b = Paddle(375, 0)
        ball = Ball()




if __name__ == '__main__':
    main()