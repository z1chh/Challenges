import struct


"""
Remove the following functions:
 - getMouse()
 - sleep()
 - fillRectangle(x, y, w, h, c)

These functions are simply declared so that the code compiles, but they are built-in functions from codeBoot
"""


def getMouse():
    return (0, 0, 0, 0, 0)


def sleep(x):
    return


def fillRectangle(x, y, w, h, c):
    return


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
        x, y, button, shift, ctrl = getMouse()
        if button == 0:
            break
        
        # Reset to original grid
        for i in range(180):
            for j in range(120):
                fillRectangle(i, j, 1, 1, imageOriginale[i][j])
        
        # Get new floating rectangle
        x1 = min(x, debut.x)
        x2 = max(x, debut.x)
        y1 = min(y, debut.y)
        y2 = max(y, debut.y)
        fillRectangle(x1, y1, x2 - x1, y2 - y1, couleur)
        
        # Update last coords
        xFinal = x
        yFinal = y
        
        # Sleep
        sleep(0.01)
    
    # Update the original image
    for i in range(min(xDebut, xFinal), max(xDebut, xFinal) + 1):
        for j in range(max(24, min(yDebut, yFinal)), max(yDebut, yFinal) + 1):
            imageOriginale[i][j] = couleur
    return
