from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from bricks import Bricks

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("BreakOut Game by Miralem")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
bricks = Bricks()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

hits = []


def walls_collision():
    global ball, paddle, hits, scoreboard
    if ball.xcor() < -570 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > 250:
        ball.bounce(x_bounce=False, y_bounce=True)
        paddle.shapesize(stretch_wid=1, stretch_len=5)
        return

    if ball.ycor() < -260:
        ball.reset_ball()
        paddle.paddle_reset((0, -250))
        hits.clear()
        scoreboard.end_game()


def paddle_collision():
    global ball, paddle, hits
    paddle_cor = paddle.xcor()
    ball_cor = ball.xcor()
    touch = 0
    if ball.distance(paddle) < 120 and ball.ycor() < -225:
        touch += 1
        hits.append(touch)
        if paddle_cor > 0:
            if ball_cor > paddle_cor:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        if paddle_cor < 0:
            if ball_cor > paddle_cor:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)


def speed_up_ball():
    global hits, ball
    if len(hits) == 4:
        ball.move_speed = 0.08
    elif len(hits) == 12:
        ball.move_speed = 0.05
    elif ball.ycor() > 100:
        ball.move_speed = 0.03
    elif ball.ycor() > 180:
        ball.move_speed = 0.01


def brick_collision():
    global bricks, ball, scoreboard
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            if brick.color()[0] == "yellow":
                scoreboard.point()
                scoreboard.evaluate_high_score()
            elif brick.color()[0] == "green":
                scoreboard.points_3()
                scoreboard.evaluate_high_score()
            elif brick.color()[0] == "orange":
                scoreboard.points_5()
                scoreboard.evaluate_high_score()
            elif brick.color()[0] == "red":
                scoreboard.points_7()
                scoreboard.evaluate_high_score()
            brick.clear()
            brick.goto(2000, 2000)
            bricks.bricks.remove(brick)

            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    walls_collision()
    paddle_collision()
    speed_up_ball()
    brick_collision()
    if len(bricks.bricks) == 0:
        bricks.create_lanes()
    if scoreboard.lives == 0:
        scoreboard.gm_ovr()
        game_is_on = False
screen.exitonclick()
