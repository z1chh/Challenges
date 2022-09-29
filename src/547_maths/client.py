from GCD import *
from eGCD import *
from inverse import *
from exponent import *
from Jacobi import *
from sqrt import *
from qr import *
from miller_rabin import *
from primitive import *


def geteGCD(a, b):
    print("eGCD({a}, {b}) = {x}".format(a=a, b=b, x=eGCD(a, b)))


def getGCD(a, b):
    print("GCD({a}, {b}) = {x}".format(a=a, b=b, x=GCD(a, b)))


def getInverse(a, N):
    print("[{a}^(-1) mod {N}] = {x}".format(a=a, N=N, x=inverse(a, N)))


def getExp(a, b, N):
    print("[{a}^{b} mod {N}] = {x}".format(
        a=a, b=b, N=N, x=exponent(a, b, N)))


def getJacobi(a, b):
    print("Jacobi({a}, {b}) = {x}".format(a=a, b=b, x=Jacobi(a, b)))


def getQuadraticResidues(p):
    qr, qnr = quadratic_residues(p)
    print("QR({p}) = {qr} & QnR({p}) = {qnr}".format(p=p, qr=qr, qnr=qnr))


def getSqrtModulo(p, a):
    print("Sqrt of {a} modulo {p} = {x}".format(
        a=a, p=p, x="+/-" + str(sqrt(p, a))))
    
def getMillerRabin(n, k=4):
    print("Miller-Rabin primality test for {n} returns {s}".format(n=n, s="prime." if isPrime(n, k) == True else "composite."))


def getPrimitive(q, pf):
    p = primitive(q, pf)
    if p == -1:
        print("There is no primitive element in F_{q}".format(q=q))
    else:
        print("{p} is a primitive element of F_{q}".format(p=p, q=q))


if __name__ == "__main__":
    geteGCD(2, 1)
    geteGCD(7, 19)
    geteGCD(19, 7)
    geteGCD(170, 25)

    getGCD(2, 1)
    getGCD(19, 7)
    getGCD(170, 25)

    getInverse(19, 7)
    getInverse(7, 19)

    getExp(5, 13, 7)
    getExp(2, 18, 37)

    getJacobi(572, 723)

    getQuadraticResidues(7)
    getQuadraticResidues(43)
    getQuadraticResidues(37)
    getQuadraticResidues(41)
    getQuadraticResidues(262915409)

    getSqrtModulo(43, 16)
    getSqrtModulo(37, 16)
    getSqrtModulo(41, 16)
    getSqrtModulo(41, 8)
    
    getMillerRabin(5)
    getMillerRabin(1591)
    getMillerRabin(1597)
    
    getPrimitive(3, [2])
    getPrimitive(5, [2])
    getPrimitive(7, [2, 3])
    getPrimitive(11, [2, 5])
