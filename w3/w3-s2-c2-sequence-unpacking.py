#!/usr/bin/env python3
# coding: utf8
"""
Sequence unpacking
"""

couple = (100, 'spam')

# On souhaite à présent extraire les deux valeurs, et les affecter à deux variables distinctes.
# Une solution naïve consiste bien sûr à faire simplement :
gauche = couple[0]
droite = couple[1]
print('gauche', gauche, 'droite', droite)

# On préférera la formulation équivalente suivante :
(gauche, droite) = couple
print('gauche', gauche, 'droite', droite)

# Les parenthèses sont optionnelles :
gauche, droite = couple
print('gauche', gauche, 'droite', droite)

"""
Les seules contraintes fixées par Python sont que :
    le terme à droite du signe = soit un itérable (tuple, liste, string, etc.) ;
    le terme à gauche soit écrit comme un tuple ou une liste - notons tout de même que l'utilisation d'une liste à 
    gauche est rare et peu pythonique ;
    les deux termes aient la même longueur - en tout cas avec les concepts que l'on a vus jusqu'ici, mais voir aussi 
    plus bas l'utilisation de *arg avec le extended unpacking.
    
La plupart du temps le terme de gauche est écrit comme un tuple. C'est pour cette raison que les deux termes tuple 
unpacking et sequence unpacking sont en vigueur.
"""


# La façon pythonique d'échanger deux variables

# Une caractéristique intéressante de l'affectation par sequence unpacking est qu'elle est sûre ; on n'a pas à se
# préoccuper d'un éventuel ordre d'évaluation, les valeurs à droite de l'affectation sont toutes évaluées en premier,
# et ainsi on peut par exemple échanger deux variables comme ceci :
a = 1
b = 2
a, b = b, a
print('a', a, 'b', b)


# Extended unpacking

reference = [1, 2, 3, 4, 5]
a, *b, c = reference
print(f"a={a} b={b} c={c}")

# Comme vous le voyez, le mécanisme ici est une extension de sequence unpacking ; Python vous autorise à mentionner
# une seule fois, parmi les variables qui apparaissent à gauche de l'affectation, une variable précédée de *, ici *b

# Cette variable est interprétée comme une liste de longueur quelconque des éléments de reference. On aurait donc
# aussi bien pu écrire :
reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")

# Ce trait peut s'avérer pratique, lorsque par exemple on s'intéresse seulement aux premiers éléments d'une
# structure : # si on sait que data contient prenom, nom, et un nombre inconnu d'autres informations
data = ['Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ', ]

# on peut utiliser la variable _
# ce n'est pas une variable spéciale dans le langage,
# mais cela indique au lecteur que l'on ne va pas s'en servir
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")
