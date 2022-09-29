from exponent import *

def primitive(q, pf):
    for i in range(len(pf)):
        pf[i] = (q - 1) / pf[i]
    for g in range(q):
        if exponent(g, q - 1, q) != 1:
            continue
        valid = True
        for i in range(len(pf)):
            if exponent(g, pf[i], q) == 1:
                valid = False
                break
        if valid:
            return g
    return -1

if __name__ == "__main__":
    print(primitive(7, [2]))