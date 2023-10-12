import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x_pos, y_size):
        super().__init__()
        self.len = 5
        self.height = self.len * 10
        self.width = 20
        self.speed = 50

        self.x_pos = x_pos
        self.max_y = y_size - self.height * 1.5

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

    def bounce_ball_by_intersection(self, ball):
        left_edge = self.xcor() - self.width 
        right_edge = self.xcor() + self.width
        top_edge = self.ycor() + self.height
        bottom_edge = self.ycor() - self.height

        ball_x, ball_y = ball.pos()
        ball_radius = ball.get_size() / 2

        if left_edge - ball_radius < ball_x < right_edge + ball_radius and \
            bottom_edge - ball_radius < ball_y < top_edge + ball_radius:
            # if intersection
            if ball.distance((self.xcor(), top_edge)) < ball_radius or \
                ball.distance((self.xcor(), bottom_edge)) < ball_radius:
                ball.bounce_y()
            else:   
                ball.bounce_x()
