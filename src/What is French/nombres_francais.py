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


def nombreFrancais99(n):
    if n < 20:
        return nombreFrancais19(n)
    elif n >= 20 and n <= 59:
        if n % 10 == 1:
            return nombreDizaineFrancais6(n // 10) + "-et-" + nombreFrancais9(n % 10)
        elif n % 10 == 0:
            return nombreDizaineFrancais6(n // 10)
        else:
            return nombreDizaineFrancais6(n // 10) + "-" + nombreFrancais9(n % 10)
    elif n >= 60 and n <= 69:
        if n % 10 == 1:
            return nombreDizaineFrancais6(6) + "-et-" + nombreFrancais19(n % 10)
        elif n % 10 == 0:
            return nombreDizaineFrancais6(6)
        else:
            return nombreDizaineFrancais6(6) + "-" + nombreFrancais9(n % 10)
    elif n == 70:
        return nombreDizaineFrancais6(6) + "-" + nombreDizaineFrancais6(1)
    elif n > 70 and n <= 79:
        if n % 10 == 1:
            return nombreDizaineFrancais6(6) + "-et-" + nombreFrancais19(11)
        else:
            return nombreDizaineFrancais6(6) + "-" + nombreFrancais19(n - 60)
    elif n == 80:
        return nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2)
    elif n > 80 and n <= 89:
        if n % 10 == 1:
            return nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2) + "-et-" + nombreFrancais9(n - 80)
        else:
            return nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2) + "-" + nombreFrancais19(n - 80)
    elif n >= 90 and n <= 99:
        if n % 10 == 1:
            return nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2) + "-et-" + nombreFrancais19(11)
        else:
            return nombreFrancais9(4) + "-" + nombreDizaineFrancais6(2) + "-" + nombreFrancais19(n - 80)
    else:
        raise ValueError("input must be between 1 and 99")


if __name__ == "__main__":
    l = [1, 8, 12, 16, 19, 20, 21, 30, 37, 41, 56, 60, 61, 69,
         70, 71, 75, 79, 80, 81, 88, 90, 91, 95, 99]
    for i in l:
        print(nombreFrancais99(i))
