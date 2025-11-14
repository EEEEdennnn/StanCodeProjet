"""
File: blur.py
Name:Eden
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage

def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    blurred_img.show()

def blur(img):
    """
    :param img:smiley-face image
    :return: blurred image
    """
    old_img = img
    blurred_img = SimpleImage.blank(old_img.width,old_img.height)
    for y in range(old_img.height):
        for x in range(old_img.width):
            r_sum = g_sum = b_sum = count = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    pixel_y = y+i
                    pixel_x = x+j
                    if 0 <= pixel_y < old_img.height:
                        if 0 <=pixel_x < old_img.width:
                            pixel = old_img.get_pixel(pixel_x,pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            blurred_img.set_rgb(x, y, int(r_sum / count), int(g_sum / count), int(b_sum / count))
    return blurred_img





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
