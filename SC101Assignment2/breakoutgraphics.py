"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.paddle_width = paddle_width
        self.ball_radius = ball_radius
        self.brick_count = brick_rows * brick_cols

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2, y=self.window_height -paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval (ball_radius*2, ball_radius*2, x = (self.window_width-ball_radius*2)//2 ,
                           y = (self.window_height-ball_radius*2)//2)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.__dx = 0
        self.__dy = 0
        self.is_moving = False
        onmouseclicked(self.clicked_ball)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                colors =['red', 'orange', 'yellow', 'green', 'blue']
                rows_color = brick_rows // len(colors)
                per_row_color = j // rows_color
                #avoid brick_rows % len(colors) =! 0
                if per_row_color >= len(colors):
                    per_row_color = len(colors)-1
                self.bricks.fill_color = colors[per_row_color]
                x = i * (brick_width + brick_spacing)
                y = brick_offset + j * (brick_height + brick_spacing)
                self.window.add(self.bricks, x = x, y= y )

    def move_paddle(self, mouse):
        new_x = mouse.x-self.paddle_width/2
        if new_x <= 0:
            new_x = 0
        if new_x >= self.window_width - self.paddle_width:
            new_x = self.window_width - self.paddle_width
        self.paddle.x = new_x

    def clicked_ball(self, mouse):
        if not self.is_moving:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random()>0.5 :
                self.__dx = -self.__dx
            self.is_moving = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    def reset_ball(self):
        self.ball.x=(self.window_width - self.ball_radius * 2) // 2
        self.ball.y=(self.window_height - self.ball_radius * 2) // 2
        self.__dx = 0
        self.__dy = 0
        self.is_moving = False

    def game_over(self):
            self.game_over = GLabel('GAME OVER')
            self.game_over.font='-40'
            self.window.add(self.game_over, x=(self.window_width - self.game_over.width) // 2,
                            y=(self.window_height - self.game_over.height) // 2)

    def win(self):
            self.game_over = GLabel('YOU WIN!!!')
            self.game_over.font='-40'
            self.window.add(self.game_over, x=(self.window_width - self.game_over.width) // 2,
                            y=(self.window_height - self.game_over.height) //2)


    # def set_ball_position(self):
    #     self.ball.x = random.randint(0, self.window.width-self.ball.width)
    #     self.ball.y = random.randint(0, self.window.height - self.ball.height)









