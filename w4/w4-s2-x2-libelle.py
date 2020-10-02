#!/usr/bin/env python3
# coding: utf8
"""
Libelle
"""


def libelle(ligne):
    x = ligne.split(",")
    if len(x) == 3:
        if x[2].strip() == '1':
            result = x[1].strip() + '.' + x[0].strip() + ' (' + x[2].strip() + 'er)'
        else:
            result = x[1].strip() + '.' + x[0].strip() + ' (' + x[2].strip() + '-ème)'
    else:
        result = None
    return result


if __name__ == "__main__":
    print(libelle('Joseph, Dupont, 4'))
    print(libelle('Jules , Durand, 1'))
    print(libelle(' Ted, Mosby, 2,'))

    assert libelle('Joseph, Dupont, 4') == 'Dupont.Joseph (4-ème)'
    assert libelle('Jean') is None
    assert libelle('Jules , Durand, 1') == 'Durand.Jules (1er)'
    assert libelle(' Ted, Mosby, 2,') is None
    assert libelle(' Jacques , Martin, 3 \t') == 'Martin.Jacques (3-ème)'
    assert libelle('Sheldon, Cooper ,5,  ') is None
    assert libelle('\t John, Doe\t, ') == 'Doe.John (-ème)'
    assert libelle('John, Smith, , , , 3') is None
