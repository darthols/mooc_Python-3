#!/usr/bin/env python3
# coding: utf8

"""
Dans le chiffre de César, on se donne une clé constituée d'un seul caractère, disons par exemple C (la 3-ième lettre
de l'alphabet), et avec cette clé on chiffre l'alphabet par un décalage de 3, ce qui donne :
    clé     : C
    clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
    chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC

La méthode de Vigenère consiste à choisir cette fois pour clé un mot, qui est utilisé de manière répétitive.
Ainsi par exemple si je choisis la clé CLE, on va chiffrer un message en appliquant la méthode de César
    avec la clé 'C' sur le 1-er caractère,
    avec la clé 'L' sur le 2-ème caractère,
    avec la clé 'E' sur le 3-ème caractère,
    avec la clé 'C' sur le 4-ème caractère,
    avec la clé 'L' sur le 5-ème caractère,
    ...
"""

import string
from itertools import cycle


def cesar(clear, key, encode=True):
    """
    Fonction qui implémente le décalage de César et doit :
      * laisser le texte tel quel si ce n'est pas un caractère alphabétique ASCII,
      * accepter une clé qui peut être minuscule ou majuscule ; dit autrement, deux clés qui valent 'C' et 'c'
        produisent toutes les deux le même résultat,
      * retourner une majuscule si le texte clair est en majuscule et une minuscule si le texte en clair est une
        minuscule.
    :param clear: caractère
    :param key: clé de codage/décodage
    :param encode: True pour encoder, False pour décoder
    :return: caractère codé ou décodé
    """
    if clear not in string.ascii_letters:
        return clear

    decalage = ord(key.lower()) - ord('a'.lower()) + 1

    # si on encode, il faut ajouter l'offset, si on décode, il faut le retrancher
    if not encode:
        decalage = -decalage

    # reste à faire le modulo
    # sauf que les bornes ne sont pas les mêmes pour les majuscules ou pour les minuscules
    bottom = ord('A') if clear.isupper() else ord('a')

    return chr(bottom + (ord(clear) - bottom + decalage) % 26)


def vigenere(clear, key, encode=True):
    """
     Prend un mot dont on utilise les lettres successivement, et en boucle, comme clé pour la méthode de César.
    :param clear: message
    :param key: clé de codage/décodage
    :param encode: True pour encoder, False pour décoder
    :return: message codé ou décodé
    """
    return "".join(cesar(c, k, encode) for c, k in zip(clear, cycle(key)))


if __name__ == "__main__":
    assert cesar('=', 'C') == '='
    assert cesar('A', 'C') == 'D'
    assert cesar('a', 'C') == 'd'
    assert cesar('A', 'c') == 'D'
    assert cesar('D', 'C', encode=False) == 'A'
    assert cesar('A', 'L') == 'M'
    assert cesar('Z', 'L') == 'L'
    assert cesar('a', 'c') == 'd'
    assert cesar('N', 'L') == 'Z'
    assert cesar('O', 'L') == 'A'
    assert cesar('D', 'C', encode=False) == 'A'
    assert cesar('D', 'c', encode=False) == 'A'
    assert cesar('D', 'c', encode=False) == 'A'
    assert cesar('a', 'c', True) == 'd'
    assert cesar('a', 'c', False) == 'x'
    assert cesar('a', 'J', True) == 'k'
    assert cesar('a', 'J', False) == 'q'
    assert cesar('a', 'T', True) == 'u'
    assert cesar('a', 'T', False) == 'g'
    assert cesar('a', 'x', True) == 'y'
    assert cesar('a', 'x', False) == 'c'
    assert cesar('N', 'c', True) == 'Q'
    assert cesar('N', 'c', False) == 'K'
    assert cesar('N', 'J', True) == 'X'
    assert cesar('N', 'J', False) == 'D'
    assert cesar('N', 'T', True) == 'H'
    assert cesar('N', 'T', False) == 'T'
    assert cesar('N', 'x', True) == 'L'
    assert cesar('N', 'x', False) == 'P'
    assert cesar('z', 'c', True) == 'c'
    assert cesar('z', 'c', False) == 'w'
    assert cesar('z', 'J', True) == 'j'
    assert cesar('z', 'J', False) == 'p'
    assert cesar('z', 'T', True) == 't'
    assert cesar('z', 'T', False) == 'f'
    assert cesar('z', 'x', True) == 'x'
    assert cesar('z', 'x', False) == 'b'

    assert vigenere('ce message', 'cle') == 'fq pqxvmlh'
    assert vigenere('fq pqxvmlh', 'CLE', False) == 'ce message'
