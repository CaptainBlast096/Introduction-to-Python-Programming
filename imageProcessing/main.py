from images import *

"""
def clamp(x)
if x> 255:
    return 255
red = FACTOR * (right - center) + 128
blue = FACTOR * (down - center) + 128
color = (red , 0, blue)
image
"""
def main():
    image = Image("Height.gif")
    image.draw()
    #image.draw()
    # Create a tuple
    image.draw()
    """"
    (r, g, b) = image.getPixel(0, 0)
    r
    194
    g
    221
    b
    128
    image.setPixel(0, 0, (r + 10, g + 10, b + 10)
    """

if __name__ == '__main__':
    main()
