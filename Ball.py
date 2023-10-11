import turtle
from enum import Enum

class BallState(Enum):
    MOVING = 1
    GOAL_LEFT = 2
    GOAL_RIGHT = 3

class Ball(turtle.Turtle):
    def __init__(self, screensize):
        super().__init__()
        self.up()
        self.size = 10
        self.speed = 40
        direction = (-.23, -.7)
        self.step_dir = (self.speed * direction[0], self.speed * direction[1])
        self.shape('circle')
        self.color('white')

        self.screensize = screensize
        self.state = BallState.MOVING

    def check_goal(self):
        max_x = self.screensize[0] / 2 - 15

        if self.state == BallState.GOAL_LEFT or self.state == BallState.GOAL_RIGHT:
            self.state = BallState.MOVING
            self.goto(0, 0)

        if self.xcor() >= max_x:
            self.state = BallState.GOAL_RIGHT
        elif self.xcor() <= -max_x:
            self.state = BallState.GOAL_LEFT

    def bounce_x(self):
        self.step_dir = (-self.step_dir[0], self.step_dir[1])

    def bounce_y(self):
        self.step_dir = (self.step_dir[0], -self.step_dir[1])

    def move(self):
        self.check_goal()
        
        max_y = self.screensize[1] / 2 - 25

        if self.ycor() >= max_y or self.ycor() <= -max_y:
            self.bounce_y()
 
        self.goto(self.pos() + self.step_dir)

    def get_pos(self):
        return self.pos()

    def get_state(self):
        return self.state

    def get_size(self):
        return self.size

    def set_state(self, in_state):
        self.state = in_state
