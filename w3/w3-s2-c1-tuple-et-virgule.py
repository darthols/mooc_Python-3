#!/usr/bin/env python3
# coding: utf8
"""
La construction de tuples
"""


# On peut construire un tuple à deux éléments - un couple - de quatre façons :

# sans parenthèse ni virgule terminale
couple1 = 1, 2

# avec parenthèses
couple2 = (1, 2)

# avec virgule terminale
couple3 = 1, 2,

# avec parenthèses et virgule
couple4 = (1, 2,)

# toutes ces formes sont équivalentes ; par exemple

couple1 == couple4

"""
En réalité la parenthèse est parfois superflue ; mais il se trouve qu'elle est largement utilisée pour améliorer 
la lisibilité des programmes, sauf dans le cas du tuple unpacking ; nous verrons aussi plus bas qu'elle est parfois 
nécessaire selon l'endroit où le tuple apparaît dans le programme ; la dernière virgule est optionnelle aussi, 
c'est le cas pour les tuples à au moins 2 éléments - nous verrons plus bas le cas des tuples à un seul élément. 
"""

# Conseil pour la présentation sur plusieurs lignes

# En général d'ailleurs, la forme avec parenthèses et virgule terminale est plus pratique. Considérez par exemple
# l'initialisation suivante ; on veut créer un tuple qui contient des listes (naturellement un tuple peut contenir
# n'importe quel objet Python), et comme c'est assez long on préfère mettre un élément du tuple par ligne :

mon_tuple = ([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
            )

"""
L'avantage lorsqu'on choisit cette forme (avec parenthèses, et avec virgule terminale), c'est d'abord qu'il n'est 
pas nécessaire de mettre un backslash à la fin de chaque ligne ; parce que l'on est à l'intérieur d'une zone 
parenthésée, l'interpréteur Python "sait" que l'instruction n'est pas terminée et va se continuer sur la ligne 
suivante.

Deuxièmement, si on doit ultérieurement ajouter ou enlever un élément dans le tuple, il suffira d'enlever ou d'ajouter
toute une ligne, sans avoir à s'occuper des virgules ; si on avait choisi de ne pas faire figurer la virgule terminale, 
alors pour ajouter un élément dans le tuple après le dernier, il ne faut pas oublier d'ajouter une virgule à la ligne 
précédente. Cette simplicité se répercute au niveau du gestionnaire de code source, où les différences dans le code 
sont plus faciles à visualiser.

Signalons enfin que ceci n'est pas propre aux tuples. La virgule terminale est également optionnelle pour les listes, 
ainsi d'ailleurs que pour tous les types Python où cela fait du sens, comme les dictionnaires et les ensembles que 
nous verrons bientôt. Et dans tous les cas où on opte pour une présentation multi-lignes, il est conseillé de faire 
figurer une virgule terminale.
"""

# Addition de tuples

# Bien que le type tuple soit immuable, il est tout à fait légal d'additionner deux tuples, et l'addition va produire
# un nouveau tuple :
tuple1 = (1, 2,)
tuple2 = (3, 4,)
print('addition', tuple1 + tuple2)

# Ainsi on peut également utiliser l'opérateur += avec un tuple qui va créer, comme précédemment, un nouvel objet
# tuple :
tuple1 = (1, 2,)
tuple1 += (3, 4,)
print('apres ajout', tuple1)


# Construire des tuples élaborés

# Malgré la possibilité de procéder par additions successives, la construction d'un tuple peut s'avérer fastidieuse.
# Une astuce utile consiste à penser aux fonctions de conversion, pour construire un tuple à partir de - par exemple -
# une liste. Ainsi on peut faire par exemple ceci :

# on fabrique une liste pas à pas
liste = list(range(10))
liste[9] = 'Inconnu'
del liste [2:5]

# on convertit le résultat en tuple
mon_tuple = tuple(liste)
