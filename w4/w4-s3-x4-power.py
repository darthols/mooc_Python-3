#!/usr/bin/env python3
# coding: utf8
"""
Power

fonction qui met un objet x à la puissance entière n.

Le paramètre x doit pouvoir être multiplié par lui même, et le paramètre n est un entier >=1 (pas la peine de vérifier).
Naturellement on s'interdit d'utiliser l'opérateur prédéfini **; notamment notre algorithme doit pouvoir s'appliquer
à tous les types d'objet qui supportent la multiplication.

Pour optimiser les calculs, on va utiliser un algorithme qui permet d'effectuer un nombre de multiplications en 𝑂(𝑙𝑜𝑔2(𝑛)).
Pour cela remarquez par exemple que le fait de mettre un nombre au carré nécessite seulement une multiplication ;
Ce qui signifie que la décomposition de n en binaire donne une formule pour  𝑥𝑛  qui met en jeu de l'ordre de  2∗𝑙𝑜𝑔2𝑛
multiplications.

Ainsi par exemple :
si n = 21, c'est-à-dire en base 2 010101, alors
𝑛=2∗2∗(2∗2+1)+1

x**21=(((𝑥.𝑥)²∗𝑥)²)².𝑥  soit 6 multiplications

si n = 42, c'est-à-dire en base 2 101010, alors
𝑛=2∗(2∗2∗(2∗2+1)+1)

𝑥**42=((((𝑥.𝑥)²∗𝑥)²)².𝑥)²  soit 7 multiplications
"""


def power(x, n):
    """
    mise à la puissance en O(log2(n))
    """
    if n == 1:
        return x
    elif n % 2 == 0:
        # on met au carré power(x, n//2)
        root = power(x, n//2)
        return root * root
    else:
        return x * power(x, n-1)


if __name__ == "__main__":
    assert power(2, 1) == 2
    assert power(2, 10) == 1024
    assert power(1j, 4) == (1-0j)
    assert power(3, 2) == 9
    assert power(3, 3) == 27
    assert power(1j, 256) == (1-0j)
    assert power(1j, 340282366920938463463374607431768211457) == 1j
    assert power(1j, 255) == (-0-1j)
