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