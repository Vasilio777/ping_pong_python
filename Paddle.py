import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x_pos, y_size):
        super().__init__()
        self.len = 5
        self.size = self.len * 10
        self.speed = 50
        self.x_pos = x_pos
        self.max_y = y_size - self.size * 1.5

        self.shape('square')
        self.shapesize(self.len, 1, 0)
        self.shape()
        self.color('white')
        self.up()
        self.setpos(x_pos, 0)

    def move_up(self):
        new_y = min(self.max_y, self.pos()[1] + self.speed)
        self.goto(self.x_pos, new_y)

    def move_down(self):
        new_y = max(-self.max_y, self.pos()[1] - self.speed)
        self.goto(self.x_pos, new_y)

    def get_hight(self):
        return self.size