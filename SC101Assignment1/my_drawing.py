"""
File: 
Name: Eden
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon ,GArc
from campy.graphics.gwindow import GWindow

window = GWindow(width=800, height=400)

def main():
    """
    Title : FUJI Mountain
    Favorite landscape
    """
    background = GRect(800, 400)
    background.filled = True
    background.fill_color = 'lightskyblue'
    background.color = 'lightskyblue'
    window.add(background)

    background2 = GRect(800, 250, x=0,y=250)
    background2.filled = True
    background2.fill_color ='navy'
    background2.color = 'navy'
    window.add(background2)

    mountain = GPolygon()
    mountain.add_vertex((100, 400))
    mountain.add_vertex((700, 150))
    mountain.add_vertex((1200, 480))
    mountain.filled = True
    mountain.fill_color = 'skyblue'
    mountain.color = 'skyblue'
    window.add(mountain)

    boat = GArc(270, 160, 180, 80)
    boat.filled = True
    boat.fill_color = 'navy'
    boat.color = 'navy'
    window.add(boat, x=100, y=195)

    boat1 = GRect(10, 45, x=140, y=195)
    boat1.filled = True
    boat1.fill_color = 'navy'
    boat1.color = 'navy'
    window.add(boat1)


    mountain_top = GPolygon()
    mountain_top.add_vertex((600, 150))
    mountain_top.add_vertex((550, 200))
    mountain_top.add_vertex((770, 200))
    mountain_top.filled = True
    mountain_top.fill_color = 'white'
    mountain_top.color = 'white'
    window.add(mountain_top)

    mountain_top3 = GPolygon()
    mountain_top3.add_vertex((600, 150))
    mountain_top3.add_vertex((720, 150))
    mountain_top3.add_vertex((770, 200))
    mountain_top3.filled = True
    mountain_top3.fill_color = 'white'
    mountain_top3.color = 'white'
    window.add(mountain_top3)

    cloud1 = GOval(50, 50, x=100, y=80)
    cloud1.filled = True
    cloud1.fill_color ='whitesmoke'
    cloud1.color = 'whitesmoke'
    window.add(cloud1)

    cloud2 = GOval(60, 60, x=55, y=60)
    cloud2.filled = True
    cloud2.fill_color ='whitesmoke'
    cloud2.color = 'whitesmoke'
    window.add(cloud2)

    cloud3 = GOval(60, 60, x=90, y=35)
    cloud3.filled = True
    cloud3.fill_color ='whitesmoke'
    cloud3.color = 'whitesmoke'
    window.add(cloud3)

    cloud4 = GOval(60, 60, x=110, y=50)
    cloud4.filled = True
    cloud4.fill_color = 'whitesmoke'
    cloud4.color = 'whitesmoke'
    window.add(cloud4)


if __name__ == '__main__':
    main()
