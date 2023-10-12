import turtle
from Paddle import Paddle
from Ball import Ball, BallState
from UI import UI
import math

t = turtle.Turtle()
screen = turtle.Screen()
screensize = (600, 800)
paddle_x = screensize[0] / 2 - 50
paused = True
screen.tracer(0)
# speed = 1

def toggle_pause(x, y):
    global paused
    paused = not paused

def init_game():
    global t
    screen.setup(screensize[0], screensize[1])
    screen.bgcolor('black')
    screen.onscreenclick(toggle_pause)
    
    render_tick()

    screen.onkeypress(paddle_left.move_up, 'w')
    screen.onkeypress(paddle_left.move_down, 's')
    screen.onkeypress(paddle_right.move_up, 'Up')
    screen.onkeypress(paddle_right.move_down, 'Down')
    
    t.pen(speed=0, shown=False)
    

def render_tick():
    global t, speed, paused

    if not paused:
        ball_state = ball.get_state()
        if ball_state == BallState.GOAL_LEFT:
            ui.give_score_left()
        elif ball_state == BallState.GOAL_RIGHT:
            ui.give_score_right()

        paddle_left.bounce_ball_by_intersection(ball)
        paddle_right.bounce_ball_by_intersection(ball)

        ball.move()

        ui.display()
        screen.update()

    turtle.ontimer(render_tick, 40)

paddle_left = Paddle(-paddle_x, screensize[1]/2)
paddle_right = Paddle(paddle_x, screensize[1]/2)
ball = Ball(screensize)
ui = UI(screensize)

init_game()

screen.listen()
screen.mainloop()
