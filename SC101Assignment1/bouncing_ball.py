"""
File: 
Name: Eden
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count = 0
bouncing_ball = False


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    window.add(ball)
    onmouseclicked(bouncing)
    while True:
        if bouncing_ball:
            bounce()
        pause(DELAY)


def bouncing(mouse):
    global bouncing_ball, count
    if ball.x == START_X and ball.y == START_Y:
        if count < 3 and not bouncing_ball:
            bouncing_ball = True


def bounce():
    global bouncing_ball, ball, count
    vy = 0

    while True:
        vy += GRAVITY
        ball.move(VX, vy)
        pause(DELAY)
        if ball.y + SIZE >= window.height:
            if vy < 0:
                vy = vy * REDUCE
            else:
                vy = -vy * REDUCE

        if ball.x > window.width:
            count += 1
            bouncing_ball = False
            ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
            ball.filled = True
            window.add(ball)
            break




if __name__ == "__main__":
    main()
