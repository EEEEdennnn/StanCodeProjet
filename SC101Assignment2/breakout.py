"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    total = NUM_LIVES
    graphics = BreakoutGraphics()
    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        ball = graphics.ball
        window = graphics.window
        ball.move(dx, dy)
        # ball touch brick and paddle
        remove = remove_brick(graphics)
        if remove == 'win':
            break
        if ball.x <= 0 or ball.x+ball.width >= window.width:
            graphics.set_dx(-dx)
        if ball.y <= 0:
            graphics.set_dy(-dy)
        if ball.y + ball.height > window.height:
            total -= 1
            graphics.reset_ball()
            if total == 0:
                graphics.game_over()
                break
        pause(FRAME_RATE)


def remove_brick(graphics):
    ball = graphics.ball
    window = graphics.window
    dy = graphics.get_dy()
    x = ball.x
    y = ball.y
    r = ball.width//2
    point = [(x,y), (x+2*r,y), (x,y+2*r), (x+2*r, y+2*r)]

    if window.get_object_at(ball.x, ball.y+ r*2) or (ball.x +2 *r, ball.y+ r*2) == graphics.paddle:
        graphics.set_dy(-dy)

    for (x,y) in point:
        p = window.get_object_at(x,y)
        if p is not None:
            if p == graphics.paddle:
                graphics.set_dy(-dy)
                ball.y = graphics.paddle.y - ball.height
            else:
                window.remove(p)
                graphics.set_dy(-dy)
                graphics.brick_count -= 1
                if graphics.brick_count == 0:
                    graphics.win()
                    return 'win'
                return p
            return None







    # Add the animation loop here!



if __name__ == '__main__':
    main()
