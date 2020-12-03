#!/usr/bin/env python3
# coding: utf8

"""
La fonction reduce permet d'appliquer une opération associative à une liste d'entrées.
Pour faire simple, étant donné un opérateur binaire ⊗ on veut pouvoir calculer
    𝑥1 ⊗ 𝑥2 ... ⊗ 𝑥𝑛

De manière un peu moins abstraite, on suppose qu'on dispose d'une fonction binaire f qui implémente l'opérateur ⊗,
et alors :
    reduce (𝑓,[𝑥1,..𝑥𝑛])=𝑓(...𝑓(𝑓(𝑥1,𝑥2),𝑥3),..,𝑥𝑛)

En fait reduce accepte un troisième argument - qu'il faut comprendre comme l'élément neutre de l'opérateur/fonction
en question - et qui est retourné lorsque la liste en entrée est vide.
"""

from functools import reduce

# la multiplication mais sous forme d'opérateur
from operator import mul
from operator import add


def factoriel(n):
    return reduce(mul, range(1, n + 1), 1)


def somme(n):
    return reduce(add, range(1, n + 1), 0)


if __name__ == "__main__":
    for i in range(6):
        print(f"{i} -> {factoriel(i)}")
    for i in range(6):
        print(f"{i} -> {somme(i)}")
