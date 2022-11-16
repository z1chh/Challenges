"""
Author     : Zi Chen Hu
Program    : Paint.py
Description: Simulates a paint program in which you can draw rectangles
Notes      : Remove all imports and functions defined before global variables
             They are here simply to avoid squiggly lines, they are already implemented in codeBoot
Execution  : Copy and paste code in codeBoot (https://codeboot.org/py/#)
"""

# THESE IMPORTS ARE HERE TO AVOID SQUIGGLYS, REMOVE BEFORE USING CODE IN CODEBOOT
import struct
import math

# THESE FUNCTIONS ARE IMPLEMENTED IN CODEBOOT, REMOVE THEM BEFORE RUNNING (HERE JUST TO GET RID OF SQUIGGLYS)


def getMouse():
    return (0, 0, 0, 0, 0)


def sleep(x):
    return


def fillRectangle(x, y, w, h, c):
    return


def setScreenMode(x, y):
    return


def setPixel(x, y, c):
    return


WIDTH = 180
HEIGHT = 120
DEFAULTSTART = 6
ERASECOLOR = "#fff"
COLOR = "#fff"
IMAGE = []  # codeBoot does not support list comprehension :D
for _ in range(WIDTH):
    lst = list()
    for _ in range(HEIGHT):
        lst.append(COLOR)
    IMAGE.append(lst)
SIZE = math.floor(HEIGHT / 10)
SPACING = math.floor(SIZE / 2)
# White, black, red, yellow, green, blue, fuschia, grey
COLORS = ["#fff", "#000", "#f00", "#ff0", "#0f0", "#00f", "#f0f", "#888"]


def createButtons(colors, size, spacing, eraseColor):
    y2 = DEFAULTSTART + size
    eraseButton = struct(corner1=struct(x=DEFAULTSTART, y=DEFAULTSTART),
                         corner2=struct(x=DEFAULTSTART + size, y=y2),
                         color=eraseColor,
                         erase=True)
    x1 = DEFAULTSTART + size + spacing
    buttons = [eraseButton]
    for c in colors:
        button = struct(corner1=struct(x=x1, y=DEFAULTSTART),
                        corner2=struct(x=x1 + size, y=y2),
                        color=c,
                        erase=False)
        buttons.append(button)
        x1 += size + spacing
    return buttons


def findButton(buttons, position):
    for button in buttons:
        if position.x >= button.corner1.x and position.x <= button.corner2.x:
            if position.y >= button.corner1.y and position.y <= button.corner2.y:
                return button
    return None


def drawFloatingRectangle(originalImage, start, color):
    xStart = start.x
    yStart = start.y
    xFinal = xStart
    yFinal = yStart
    x1 = xStart
    x2 = xStart
    y1 = yStart
    y2 = yStart
    while True:
        # Check if continue to draw floating rectangle
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        button = mouse.button
        if button == 0:
            break

        # Reset to original grid
        restoreImage(originalImage,
                     struct(corner1=struct(x=x1, y=y1),
                            corner2=struct(x=x2, y=y2)))

        # Get new floating rectangle
        x1 = min(x, start.x)
        x2 = max(x, start.x)
        y1 = min(y, start.y)
        y2 = max(y, start.y)

        # Color
        y1 = max(y1, math.ceil(HEIGHT / 5))
        fillRectangle(x1, y1, x2 - x1, y2 - y1, color)

        # Update last coords
        xFinal = x
        yFinal = y

        # Sleep
        sleep(0.01)

    # Update the original image
    rectangle = struct(corner1=struct(x=min(xStart, xFinal), y=min(yStart, yFinal)),
                       corner2=struct(x=max(xStart, xFinal) + 1, y=max(yStart, yFinal) + 1))
    addRectangle(originalImage, rectangle, color)
    return


def restoreImage(originalImage, rectangle):
    for i in range(rectangle.corner1.x, rectangle.corner2.x):
        for j in range(max(math.ceil(HEIGHT / 5), rectangle.corner1.y), rectangle.corner2.y):
            setPixel(i, j, originalImage[i][j])
    return


def addRectangle(image, rectangle, color):
    for i in range(rectangle.corner1.x, rectangle.corner2.x):
        for j in range(max(math.ceil(HEIGHT / 5), rectangle.corner1.y), rectangle.corner2.y):
            image[i][j] = color
    return


def treatNextClick(buttons):
    COLOR = "#fff"
    while True:
        # Check if user clicked
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        button = mouse.button
        if button == 1:
            if y <= math.ceil(HEIGHT / 5):
                b = findButton(buttons, struct(x=x, y=y))
                if b is not None:
                    if b.erase:
                        draw()
                    else:
                        COLOR = b.color
            else:
                drawFloatingRectangle(IMAGE, struct(x=x, y=y), COLOR)
        sleep(0.01)


def addBorder(button):
    # Horizontal borders
    for i in range(button.corner1.x, button.corner1.x + SIZE + 1):
        setPixel(i, button.corner1.y, "#000")
        setPixel(i, button.corner1.y + SIZE, "#000")

    # Vertical borders
    for i in range(button.corner1.y, button.corner1.y + SIZE):
        setPixel(button.corner1.x, i, "#000")
        setPixel(button.corner1.x + SIZE, i, "#000")


def draw():
    # Initialize
    setScreenMode(WIDTH, HEIGHT)

    # Background
    fillRectangle(0, 0, WIDTH, HEIGHT, ERASECOLOR)
    fillRectangle(0, 0, WIDTH, math.ceil(HEIGHT / 5), "#888")

    # Buttons
    buttons = createButtons(COLORS, SIZE, SPACING, ERASECOLOR)
    for button in buttons:
        fillRectangle(button.corner1.x,
                      button.corner1.y,
                      button.corner2.x - button.corner1.x,
                      button.corner2.y - button.corner1.y,
                      button.color)

    # Add "X" on erase
    for i in range(6, 6 + SIZE):
        setPixel(i, i, "#f00")
    for i in range(0, SIZE):
        setPixel(6 + SIZE - i, i + 6, "#f00")

    # Add border for buttons
    for button in buttons:
        addBorder(button)

    # Reset IMAGE
    for i in range(WIDTH):
        for j in range(HEIGHT):
            IMAGE[i][j] = ERASECOLOR

    # Start program
    # Infinite loop, does not terminate (PDF does not say to terminate)
    treatNextClick(buttons)
