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


LARGEUR = 180
HAUTEUR = 120
COULEUREFFACER = "#fff"
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
        restaurerImage(imageOriginale, struct(coin1=struct(
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
    ajouterRectangle(imageOriginale, rectangle, couleur)
    return


def restaurerImage(imageOriginale, rectangle):
    for i in range(rectangle.coin1.x, rectangle.coin2.x):
        for j in range(max(math.ceil(HAUTEUR / 5), rectangle.coin1.y), rectangle.coin2.y):
            setPixel(i, j, imageOriginale[i][j])
    return


def ajouterRectangle(image, rectangle, couleur):
    for i in range(rectangle.coin1.x, rectangle.coin2.x):
        for j in range(max(math.ceil(HAUTEUR / 5) + 1, rectangle.coin1.y), rectangle.coin2.y):
            image[i][j] = couleur
    return


def traiterProchainClic(boutons):
    COULEUR = "#fff"
    while True:
        # Check if user clicked
        mouse = getMouse()
        x = mouse.x
        y = mouse.y
        boutton = mouse.button
        if boutton == 1:
            if y <= math.ceil(HAUTEUR / 5):
                b = trouverBouton(boutons, struct(x=x, y=y))
                if b is not None:
                    if b.effacer:
                        dessiner()
                    else:
                        COULEUR = b.couleur
            else:
                dessinerRectangleFlottant(IMAGE, struct(x=x, y=y), COULEUR)
        sleep(0.01)


def dessiner():
    # Initialize
    setScreenMode(LARGEUR, HAUTEUR)

    # Background
    fillRectangle(0, 0, LARGEUR, HAUTEUR, COULEUREFFACER)
    fillRectangle(0, 0, LARGEUR, math.ceil(HAUTEUR / 5), "#888")

    # Buttons
    boutons = creerBoutons(COULEURS, TAILLE, ESPACE, COULEUREFFACER)
    for bouton in boutons:
        fillRectangle(bouton.coin1.x,
                      bouton.coin1.y,
                      bouton.coin2.x - bouton.coin1.x,
                      bouton.coin2.y - bouton.coin1.y,
                      bouton.couleur)

    # Add "X" on erase
    for i in range(6, 6 + TAILLE):
        setPixel(i, i, "#f00")
    for i in range(0, TAILLE):
        setPixel(5 + TAILLE - i, i + 6, "#f00")

    # Reset IMAGE
    for i in range(LARGEUR):
        for j in range(HAUTEUR):
            IMAGE[i][j] = COULEUREFFACER

    # Start program
    # Infinite loop, does not terminate (PDF does not say to terminate)
    traiterProchainClic(boutons)
