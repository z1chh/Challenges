from exponent import *

def quadratic_residues(p, N):
    qr = []
    qnr = []
    for i in range(p):
        n = exponent(i, 2, N)
        if n not in qr:
            qr.append(n)
    
    for i in range(p):
        if i not in qr:
            qnr.append(i)
    
    return (qr, qnr)