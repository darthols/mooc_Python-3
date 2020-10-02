#!/usr/bin/env python3
# coding: utf8
"""
Passage par référence
"""

"""
En Python, tous les passages de paramètres se font par référence.
"""


def ma_fonction(dans_fonction):
    print(dans_fonction)


def ma_fonction2(dans_fonction):
    """
    On peut le voir encore d'une autre façon en instrumentant le code comme ceci -- on rappelle que la fonction
    built-in id retourne l'adresse mémoire d'un objet :
    """
    print('dans ma_fonction', dans_fonction , id(dans_fonction))


"""
On voit donc que l'appel de fonction crée des références partagées, exactement comme l'affectation, et que tout ce que 
nous avons vu au sujet des références partagées s'applique exactement à l'identique :
"""


# on ne peut pas modifier un immuable dans une fonction
def increment(n):
    n += 1


# on peut par contre ajouter dans une liste
def insert(liste, valeur):
    liste.append(valeur)


if __name__ == "__main__":
    dans_appelant = ["texte"]
    print()

    # ma_fonction (dans_appelant)
    # → on entre dans la fonction
    dans_fonction = dans_appelant
    print(dans_fonction)
    print()

    dans_appelant = ["texte"]
    print('dans appelant   ', dans_appelant, id(dans_appelant))
    ma_fonction2(dans_appelant)
    print()

    compteur = 10
    increment(compteur)
    print(compteur)
    print()

    liste = ["un"]
    insert(liste, "texte")
    print(liste)
