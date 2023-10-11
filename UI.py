import turtle

class UI(turtle.Turtle):
    def __init__(self, screensize):
        super().__init__()
        self.up()
        self.ht()
        self.color('white')
        self.goto(0, screensize[1] / 2.5)

        self.score_left = 0
        self.score_right = 0

        self.display()

    def give_score_left(self):
        self.score_left += 1

    def give_score_right(self):
        self.score_right += 1

    def display(self):
        self.clear()
        self.write(f'{self.score_left}   {self.score_right}', align="center", font=('Arial', 40, 'normal'))
