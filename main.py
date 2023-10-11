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

        ball_size = ball.get_size()
        p_width = 20
        p_hight = paddle_left.get_hight()
        range_y_left = range(int(paddle_left.ycor() - p_hight), int(paddle_left.ycor() + p_hight)) 
        range_y_right = range(int(paddle_right.ycor() - p_hight), int(paddle_right.ycor() + p_hight))

        ball.move()

        if ball.xcor() < paddle_left.xcor() + p_width:
            if ball.ycor() < paddle_left.ycor() and ball.ycor() + ball.get_size() > paddle_left.ycor() - p_hight or \
                ball.ycor() > paddle_left.ycor() and ball.ycor() - ball.get_size() < paddle_left.ycor() + p_hight:
                ball.bounce_y()

        elif ball.xcor() - ball.get_size()/2 < paddle_left.xcor() + p_width and ball.ycor() in range_y_left:
            ball.bounce_x()
        # elif ball.xcor() < paddle_left.xcor() + p_width and ball.ycor() in range_y_left:
        #     ball.bounce_x()
        
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
