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
ERASECOLOR = "#fff"
COLOR = "#fff"
IMAGE = [] # codeBoot does not support list comprehension :D
for _ in range(WIDTH):
    lst = list()
    for _ in range(HEIGHT):
        lst.append(COLOR)
    IMAGE.append(lst)
SIZE = math.floor(HEIGHT / 10)
SPACING = math.floor(SIZE / 2)
COLORS = ["#fff", "#000", "#f00", "#ff0", "#0f0", "#00f", "#f0f", "#888"] # White, black, red, yellow, green, blue, fuschia, grey


def createBoutons(couleurs, taille, espace, couleurEffacer):
    y2 = 6 + taille
    effacer = struct(coin1=struct(x=6, y=6),
                     coin2=struct(x=6 + taille, y=y2),
                     couleur=couleurEffacer,
                     effacer=True)
    x1 = 6 + taille + espace
    boutons = [effacer]
    for c in couleurs:
        bouton = struct(coin1=struct(x=x1, y=6),
                        coin2=struct(x=x1 + taille, y=y2),
                        couleur=c,
                        effacer=False)
        boutons.append(bouton)
        x1 += taille + espace
    return boutons


def findBouton(boutons, position):
    for bouton in boutons:
        if position.x >= bouton.coin1.x and position.x <= bouton.coin2.x:
            if position.y >= bouton.coin1.y and position.y <= bouton.coin2.y:
                return bouton
    return None


def drawFloatingRectangle(imageOriginale, debut, couleur):
    xDebut = debut.x
    yDebut = debut.y
    xFinal = xDebut
    yFinal = yDebut
    x1 = xDebut
    x2 = xDebut
    y1 = yDebut
    y2 = yDebut
    while True:
        # Check if continue to draw floating rectangle
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        boutton = mouse.button
        if boutton == 0:
            break

        # Reset to original grid
        restoreImage(imageOriginale, struct(coin1=struct(
            x=x1, y=y1), coin2=struct(x=x2, y=y2)))

        # Get new floating rectangle
        x1 = min(x, debut.x)
        x2 = max(x, debut.x)
        y1 = min(y, debut.y)
        y2 = max(y, debut.y)

        # Color
        y1 = max(y1, math.ceil(HAUTEUR / 5))
        fillRectangle(x1, y1, x2 - x1, y2 - y1, couleur)

        # Update last coords
        xFinal = x
        yFinal = y

        # Sleep
        sleep(0.01)

    # Update the original image
    rectangle = struct(coin1=struct(x=min(xDebut, xFinal), y=min(
        yDebut, yFinal)), coin2=struct(x=max(xDebut, xFinal) + 1, y=max(yDebut, yFinal) + 1))
    addRectangle(imageOriginale, rectangle, couleur)
    return


def restoreImage(imageOriginale, rectangle):
    for i in range(rectangle.coin1.x, rectangle.coin2.x - 1):
        for j in range(max(math.ceil(HAUTEUR / 5), rectangle.coin1.y), rectangle.coin2.y - 1):
            setPixel(i, j, imageOriginale[i][j])
    return


def addRectangle(image, rectangle, couleur):
    for i in range(rectangle.coin1.x, rectangle.coin2.x):
        for j in range(max(math.ceil(HAUTEUR / 5), rectangle.coin1.y), rectangle.coin2.y):
            image[i][j] = couleur
    return


def treatNextClick(boutons):
    COULEUR = "#fff"
    while True:
        # Check if user clicked
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        boutton = mouse.button
        if boutton == 1:
            if y <= math.ceil(HAUTEUR / 5):
                b = findButton(boutons, struct(x=x, y=y))
                if b is not None:
                    if b.erase:
                        draw()
                    else:
                        COULEUR = b.color
            else:
                drawFloatingRectangle(IMAGE, struct(x=x, y=y), COLOR)
        sleep(0.01)


def addBorder(button):
    # Horizontal borders
    for i in range(button.coin1.x, button.coin1.x + SIZE + 1):
        setPixel(i, button.coin1.y, "#000")
        setPixel(i, button.coin1.y + SIZE, "#000")

    # Vertical borders
    for i in range(button.coin1.y, button.coin1.y + SIZE):
        setPixel(button.coin1.x, i, "#000")
        setPixel(button.coin1.x + SIZE, i, "#000")


def draw():
    # Initialize
    setScreenMode(WIDTH, HEIGHT)

    # Background
    fillRectangle(0, 0, LARGEUR, HAUTEUR, COULEUREFFACER)
    fillRectangle(0, 0, LARGEUR, math.ceil(HAUTEUR / 5), "#888")

    # Buttons
    buttons = createButtons(COULEURS, TAILLE, ESPACE, COULEUREFFACER)
    for button in buttons:
        fillRectangle(button.coin1.x,
                      button.coin1.y,
                      button.coin2.x - button.coin1.x,
                      button.coin2.y - button.coin1.y,
                      button.couleur)

    # Add "X" on erase
    for i in range(6, 6 + TAILLE):
        setPixel(i, i, "#f00")
    for i in range(0, TAILLE):
        setPixel(6 + TAILLE - i, i + 6, "#f00")

    # Add border for buttons
    for button in buttons:
        addBorder(button)

    # Reset IMAGE
    for i in range(LARGEUR):
        for j in range(HAUTEUR):
            IMAGE[i][j] = COULEUREFFACER

    # Start program
    # Infinite loop, does not terminate (PDF does not say to terminate)
    treatNextClick(buttons)
