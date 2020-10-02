#!/usr/bin/env python3
# coding: utf8
"""
Type hints
"""

from typing import List

"""
Depuis la version 3.5, python supporte un mécanisme totalement optionnel qui vous permet d'annoter les arguments des 
fonctions avec des informations de typage, ce mécanisme est connu sous le nom de type hints.

À ce stade, on peut entrevoir les usages suivants à ce type d'annotation :
    tout d'abord, et évidemment, cela peut permettre de mieux documenter le code ;
    les environnements de développement sont susceptibles de vous aider de manière plus effective ; si quelque part 
    vous écrivez z = fact(12), le fait de savoir que z est entier permet de fournir une complétion plus pertinente 
    lorsque vous commencez à écrire z.[TAB] ;
    on peut espérer trouver des erreurs dans les passages d'arguments à un stade plus précoce du développement.

Par contre ce qui est très très clairement annoncé également, c'est que ces informations de typage sont totalement 
facultatives, et que le langage les ignore totalement.
"""


# une fonction factorielle avec des type hints
def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n-1)


# L'ensemble des symboles que nous allons utiliser dans la suite de ce complément provient du module typing
# une fonction qui # attend un paramètre qui soit une liste d'entiers,
# et qui retourne une liste de chaînes
def foo(x: List[int]) -> List[str]:
    pass


if __name__ == "__main__":
    # pour typer une variable avec les type hints
    nb_items: int = 0
