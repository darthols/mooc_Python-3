#!/usr/bin/env python3
# coding: utf8

def distance(*args):
    """
    Prend un nombre quelconque d'arguments numériques non complexes, et qui retourne la racine carrée de la somme
    des carrés des arguments.
    Par convention on fixe que 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒()=0
    :param args: liste d'entiers
    :return: racine carrée de la somme des carrés des arguments
    """
    result = 0
    for i in range(len(args)):
        result += args[i]**2
    return result**.5


def numbers(*args):
    """
    Prend en argument un nombre quelconque d'entiers, et retourne un tuple contenant
        la somme
        le minimum
        le maximum de ses arguments.
    :param args: liste d'entiers
    :return: tupe avec (somme, minimum, maximum des arguments)
    """
    if len(args) == 0:
        result = (0, 0, 0)
    else:
        result = (sum(args), min(args), max(args))
    return result


if __name__ == "__main__":
    assert distance() == 0.0
    assert distance(1) == 1.0
    assert distance(1, 1) == 1.4142135623730951
    assert distance(1, 1, 1) == 1.7320508075688772
    assert distance(1, 1, 1, 1) == 2.0
    assert distance(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) == 16.881943016134134

    assert numbers() == (0, 0, 0)
    assert numbers(6) == (6, 6, 6)
    assert numbers(8, 8) == (16, 8, 8)
    assert numbers(11, 12, 15, 11, 12, 6) == (67, 6, 15)
    assert numbers(13, 13, 12, 11) == (49, 11, 13)
    assert numbers(8, 8, 5, 6, 5, 11) == (43, 5, 11)
