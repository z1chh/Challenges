import math

def primitive(q, pf):
    for i in range(len(pf)):
        pf[i] = (q - 1) / pf[i]
    for g in range(q):
        if math.pow(g, q - 1) != 1:
            continue
        valid = True
        for i in range(len(pf)):
            if math.pow(g, pf[i]) == 1:
                valid = False
                break
        if valid:
            return g
    return -1

if __name__ == "__main__":
    print(primitive(5, [2, 2]))