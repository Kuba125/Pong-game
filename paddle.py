from turtle import Turtle

HIGH_BORDER = 200
LOW_BORDER = -200
PADDLE_MOVEMENT = 30

class Paddle:
    def __init__(self,position):
        self.paddle = Turtle()
        self.paddle.lt(90)
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(1, 7)
        self.paddle.penup()
        if position == 'left':
            self.paddle.goto(-400, 0)
        elif position == 'right':
            self.paddle.goto(400, 0)

    def up(self):
        if self.paddle.pos()[1] > HIGH_BORDER:
            pass
        else:
            self.paddle.fd(PADDLE_MOVEMENT)

    def down(self):
        if self.paddle.pos()[1] < LOW_BORDER:
            pass
        else:
            self.paddle.bk(PADDLE_MOVEMENT)