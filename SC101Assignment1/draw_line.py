"""
File: 
Name:Eden
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20
window = GWindow()
x1 = None
y1 = None
pen = GOval(SIZE, SIZE)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(hole)


def hole(mouse):
    global x1, y1
    pen.x = mouse.x - SIZE / 2
    pen.y = mouse.y - SIZE / 2
    if x1 is None and y1 is None:
        x1 = mouse.x
        y1 = mouse.y
        window.add(pen, x=pen.x, y=pen.y)
    else:
        line = GLine(x1, y1, mouse.x, mouse.y)
        window.remove(pen)
        window.add(line)
        x1 = None
        y1 = None













if __name__ == "__main__":
    main()
