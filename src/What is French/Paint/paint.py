import struct


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
