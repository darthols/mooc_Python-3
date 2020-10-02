#!/usr/bin/env python3
# coding: utf8
"""
La suite de Fibonacci
    u_0 = 0
    u_1 = 1
    forall n >= 2, u_n = u_{n-1} + u_{n-2}

Ce qui donne pour les premières valeurs :
    | n  | fibonacci(n) |
    |---:|-------------:|
    | 0  | 0            |
    | 1  | 1            |
    | 2  | 1            |
    | 3  | 2            |
    | 4  | 3            |
    | 5  | 5            |
    | 6  | 8            |
    | 7  | 13           |
"""


def fibonacci(n):
    """
    Retourne le nombre de fibonacci pour l'entier n
    :param n: entier
    :return: nombre de fibonacci
    """
    # pour les deux petites valeurs de n, on peut retourner n
    if n <= 1:
        return n
    # sinon on initialise f2 pour n-2 et f1 pour n-1
    f2, f1 = 0, 1
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
        # print(i, f2, f1)
    # le résultat est dans f1
    return f1


if __name__ == "__main__":
    entier = int(input("Entrer un entier :"))
    print(f"fibonacci({entier}) = {fibonacci(entier)}")
