# Pong

from GameElement import *

import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)

# Necessary for fast updatespeed
win.tracer(0)

# Score
score_a = score_b = 0

paddle_a = GameElement(-350, 0, 5, 1)
paddle_b = GameElement(350, 0, 5, 1)
ball = GameElement(0, 0)
pen = GameElement(0, 260, 0, 0, hide_turtle=True)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

# Ball speed (moves by x)
ball.dx = ball.dy = .2


# TODO: It is not possible to parse an argument with Turtle onkeypress. Find another listener?
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Listeners
win.listen()

win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Reversing direction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)

        # Reverse direction
        ball.dx *= -1

        # A scores
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)

        # Reverse direction
        ball.dx *= -1

        # A scores
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
