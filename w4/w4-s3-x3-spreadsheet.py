#!/usr/bin/env python3
# coding: utf8
"""
Spreadsheet

prend en entrée un entier et retourne le nom de la colonne correspondante dans un fichier Excel.
"""


def int_to_char(n):
    """
    Prend les entiers de 1 à 26 et retourne les lettres de A à Z.
    :param n: entier de 1 à 26
    :return: lettres de A à Z
    """
    return chr(ord('A') + (n - 1) % 26)


def spreadsheet(index):
    """
    Transforme un numéro de colonne en nom alphabétique dans l'ordre lexicographique
        1 -> A; 26 -> Z; 27 -> AA; 28 -> AB; etc..
    :param index:
    :return:
    """
    # index peut être supérieur à 26 en remarquant que la dernière lettre s'incrémente à chaque fois qu'index augmente,
    # et repasse à 'A' de manière cyclique, on voit qu'on peut utiliser notre version cyclique de `int_to_char`
    # pour calculer la lettre la plus à droite dans le résultat.
    # et pour les autres lettres, il suffit de recommencer sur le quotient
    result = int_to_char(index)
    while index > 26:
        index = (index - 1) // 26
        result = int_to_char(index) + result
    return result


if __name__ == "__main__":
    assert spreadsheet(1) == 'A'
    assert spreadsheet(15) == 'O'
    assert spreadsheet(26) == 'Z'
    assert spreadsheet(27) == 'AA'
    assert spreadsheet(701) == 'ZY'
    assert spreadsheet(702) == 'ZZ'
    assert spreadsheet(703) == 'AAA'
    assert spreadsheet(704) == 'AAB'
    assert spreadsheet(18277) == 'ZZY'
    assert spreadsheet(18278) == 'ZZZ'
    assert spreadsheet(18279) == 'AAAA'
    assert spreadsheet(18280) == 'AAAB'
    assert spreadsheet(675) == 'YY'
    assert spreadsheet(30000) == 'ARIV'
    assert spreadsheet(100000) == 'EQXD'
    assert spreadsheet(1000000) == 'BDWGN'
