#!/usr/bin/env python3
# coding: utf8
"""
PGCD

L'algorithme d'Euclide sur deux nombres entiers positifs a et b avec a > b ≥ 0 procède comme suit :
    Si b = 0, l'algorithme termine et rend la valeur a ;
    Sinon, l'algorithme calcule le reste r de la division euclidienne de a par b, puis recommence avec a := b et b := r.
"""


def pgcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


if __name__ == "__main__":
    assert pgcd(1, 1) == 1
    assert pgcd(0, 0) == 0
    assert pgcd(0, 1) == 1
    assert pgcd(1, 0) == 1
    assert pgcd(15, 10) == 5
    assert pgcd(10, 15) == 5
    assert pgcd(3, 10) == 1
