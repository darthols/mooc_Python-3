#!/usr/bin/env python3
# coding: utf8
"""
isinstance
"""

"""
Avec la fonction prédéfinie isinstance - qui peut être par ailleurs utile dans d'autres contextes - vous pouvez 
facilement :
    - vérifier qu'un argument d'une fonction a bien le type attendu,
    - et traiter différemment les entrées selon leur type.
"""


def factoriel(argument):
    """
    Exemple simple montrant comment on pourrait définir une fonction qui travaille sur un entier, mais qui par commodité
    peut aussi accepter un entier passé comme une chaîne de caractères, ou même une liste d'entiers (auquel cas on
    renvoie la liste des factorielles)
    :param argument:
    :return:
    """
    # si on reçoit un entier
    if isinstance(argument, int):              # (*)
        return 1 if argument <= 1 else argument * factoriel(argument - 1)
    # convertir en entier si on reçoit une chaîne
    elif isinstance(argument, str):
        return factoriel(int(argument))
    # la liste des résultats si on reçoit un tuple ou une liste
    elif isinstance(argument, (tuple, list)):  # (**)
        return [factoriel(i) for i in argument]
    # sinon on lève une exception
    else:
        raise TypeError(argument)


"""
Le module types définit un certain nombre de constantes qui peuvent être utiles. 
(https://docs.python.org/3/library/types.html)

Il est recommandé d'utiliser isinstance par rapport à la fonction type. Tout d'abord, cela permet, on vient de le voir, 
de prendre en compte plusieurs types.
Mais aussi et surtout isinstance supporte la notion d'héritage qui est centrale dans le cadre de la programmation 
orientée objet.
Avec la programmation objet, vous pouvez définir vos propres types. On peut par exemple définir une classe Animal qui 
convient pour tous les animaux, puis définir une sous-classe Mammifere. On dit que la classe Mammifere hérite de la 
classe Animal, et on l'appelle sous-classe parce qu'elle représente une partie des animaux ; et donc tout ce qu'on peut 
faire sur les animaux peut être fait sur les mammifères.

En voici une implémentation très rudimentaire, uniquement pour illustrer le principe de l'héritage.
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Mammifere(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


if __name__ == "__main__":
    print("entier", factoriel(4))
    print("chaine", factoriel("8"))
    print("tuple", factoriel((4, 8)))
    print()

    # pour créer un objet de type `Animal` (méthode __init__)
    requin = Animal('requin')
    # idem pour un Mammifere
    baleine = Mammifere('baleine')

    # bien sûr ici la réponse est 'True'
    print("l'objet baleine est-il un mammifère ?", isinstance(baleine, Mammifere))

    # ici c'est moins évident, mais la réponse est 'True' aussi
    print("l'objet baleine est-il un animal ?", isinstance(baleine, Animal))
