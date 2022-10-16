from exponent import *

def quadratic_residues(p):
    qr = []
    qnr = []
    for i in range(1, p):
        n = exponent(i, 2, p)
        if n not in qr:
            qr.append(n)
    
    for i in range(1, p):
        if i not in qr:
            qnr.append(i)
    
    qr.sort()
    qnr.sort()
    return (qr, qnr)