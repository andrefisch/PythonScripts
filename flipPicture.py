import sys
flip_horizontal(sys.argv[1])

def flip_vertical(picture):
    width = getWidth(picture)
    height = getHeight(picture)

    for y in range(0, height/2):
        for x in range(0, width):
            sourcePixel = getPixel(picture, x, y)
            targetPixel = getPixel(picture, x, height - y - 1)
            color = getColor(sourcePixel)
            setColor(sourcePixel, getColor(targetPixel))
            setColor(targetPixel, color)

    return picture 


def flip_horizontal(picture):
    width = getWidth(picture)
    height = getHeight(picture)

    for y in range(0, height):
        for x in range(0, width/2):
            sourcePixel = getPixel(picture, x, y)
            targetPixel = getPixel(picture, width - x - 1, y)
            color = getColor(sourcePixel)
            setColor(sourcePixel, getColor(targetPixel))
            setColor(targetPixel, color)

    return picture 
