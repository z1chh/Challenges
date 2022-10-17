# Dumbest shit ever
def nombreFrancais9(n):
    if n == 1:
        return "un"
    elif n == 2:
        return "deux"
    elif n == 3:
        return "trois"
    elif n == 4:
        return "quatre"
    elif n == 5:
        return "cinq"
    elif n == 6:
        return "six"
    elif n == 7:
        return "sept"
    elif n == 8:
        return "huit"
    elif n == 9:
        return "neuf"
    else:
        raise ValueError("input must be between 1 and 9")


def nombreDizaineFrancais6(n):
    if n == 1:
        return "dix"
    elif n == 2:
        return "vingts"
    elif n == 3:
        return "trente"
    elif n == 4:
        return "quarante"
    elif n == 5:
        return "cinquante"
    elif n == 6:
        return "soixante"
    else:
        raise ValueError("input must be between 1 and 6")


def nombreFrancais19(n):
    if n <= 0:
        raise ValueError("input must be between 1 and 19")
    if n < 10:
        return nombreFrancais9(n)
    if n == 10:
        return nombreDizaineFrancais6(1)
    if n == 11:
        return "onze"
    if n == 12:
        return "douze"
    if n == 13:
        return "treize"
    if n == 14:
        return "quatorze"
    if n == 15:
        return "quinze"
    if n == 16:
        return "seize"
    if n >= 17 and n <= 19:
        return nombreDizaineFrancais6(1) + "-" + nombreFrancais9(n - 10)
    else:
        raise ValueError("input must be between 1 and 19")
