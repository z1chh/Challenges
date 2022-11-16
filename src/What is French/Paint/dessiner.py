import struct
import math


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


"""
Global Variables:
 - LARGEUR
 - HAUTEUR
 - COULEUR
 - IMAGE
 - TAILLE
 - ESPACE
 - COULEURS
"""
LARGEUR = 180
HAUTEUR = 120
COULEUR = "#fff"
IMAGE = []
for _ in range(LARGEUR):
    lst = list()
    for _ in range(HAUTEUR):
        lst.append(COULEUR)
    IMAGE.append(lst)
TAILLE = 12
ESPACE = 6
COULEURS = ["#fff", "#000", "#f00", "#ff0", "#0f0", "#00f", "#f0f", "#888"]


"""
Functions
"""


def creerBoutons(couleurs, taille, espace, couleurEffacer):
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


def trouverBouton(boutons, position):
    for bouton in boutons:
        if position.x >= bouton.coin1.x and position.x <= bouton.coin2.x:
            if position.y >= bouton.coin1.y and position.y <= bouton.coin2.y:
                return bouton
    return None


def dessinerRectangleFlottant(imageOriginale, debut, couleur):
    xDebut = debut.x
    yDebut = debut.y
    xFinal = xDebut
    yFinal = yDebut
    while True:
        # Check if continue to draw floating rectangle
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        button = mouse.button
        if button == 0:
            break

        # Get new floating rectangle
        x1 = min(x, debut.x)
        x2 = max(x, debut.x)
        y1 = min(y, debut.y)
        y2 = max(y, debut.y)
        fillRectangle(x1, y1, x2 - x1, y2 - y1, couleur)

        # Reset to original grid
        restaurerImage(IMAGE, struct(coin1=struct(
            x=x1, y=y1), coin2=struct(x=x2, y=y2)))

        # Update last coords
        xFinal = x
        yFinal = y

        # Sleep
        sleep(0.01)

    # Update the original image
    rectangle = struct(coin1=struct(x=min(xDebut, xFinal), y=min(
        yDebut, yFinal)), coin2=struct(x=max(xDebut, xFinal) + 1, y=max(yDebut, yFinal) + 1))
    restaurerImage(imageOriginale, rectangle)
    return


def restaurerImage(imageOriginale, rectangle):
    for i in range(rectangle.coin1.x, rectangle.coin2.x):
        for j in range(max(math.ceil(HAUTEUR / 5) + 1, rectangle.coin1.y), rectangle.coin2.y):
            setPixel(i, j, imageOriginale[i][j])
    return


def ajouterRectangle(image, rectangle, couleur):
    for i in range(rectangle.coin1.x, rectangle.coin2.x):
        for j in range(max(math.ceil(HAUTEUR / 5) + 1, rectangle.coin1.y), rectangle.coin2.y):
            image[i][j] = couleur
    return


def traiterProchainClic(boutons):
    while True:
        # Check if user clicked
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        button = mouse.button
        if button == 1:
            if y < math.ceil(HAUTEUR / 5):
                b = trouverBouton(boutons, struct(x=x, y=y))
                if b is not None:
                    if b.effacer:
                        COULEUR = "#fff"
                    else:
                        COULEUR = b.couleur
            else:
                dessinerRectangleFlottant(IMAGE, struct(x=x, y=y), COULEUR)
        sleep(0.01)


def dessiner():
    # Initialize
    setScreenMode(LARGEUR, HAUTEUR)

    # Background
    fillRectangle(0, 0, LARGEUR, HAUTEUR, COULEUR)
    fillRectangle(0, 0, LARGEUR, math.ceil(HAUTEUR / 5), "#888")

    # Buttons
    boutons = creerBoutons(COULEURS, TAILLE, ESPACE, "#fff")
    for bouton in boutons:
        fillRectangle(bouton.coin1.x,
                      bouton.coin1.y,
                      bouton.coin2.x - bouton.coin1.x,
                      bouton.coin2.y - bouton.coin1.y,
                      bouton.couleur)

    # Start program
    # Infinite loop, does not terminate (PDF does not say to terminate)
    traiterProchainClic(boutons)
