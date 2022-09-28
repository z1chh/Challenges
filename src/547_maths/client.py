from GCD import *
from eGCD import *
from inverse import *
from exponent import *
from jacobi import *


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
    print("Jacobi({a}, {b}) = {x}".format(a=a, b=b, x=jacobi(a, b)))


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

    getJacobi(572, 723)
