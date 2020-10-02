#!/usr/bin/env python3
# coding: utf8
"""
if comme expression
"""


"""
Expression conditionnelle

Il existe en Python une expression qui fait un test ; c'est la forme dite d'expression conditionnelle, qui est une 
expression à part entière, avec la syntaxe :
    <résultat_si_vrai> if <condition> else <résultat_si_faux>
"""

if __name__ == "__main__":
    x = 1
    y = 12 if x else 35
    print(y)

    # Puisque cette forme est une expression, on peut l'utiliser dans une autre expression conditionnelle, comme ici :
    # on veut calculer en fonction d'une entrée x
    # une sortie qui vaudra
    # -1 si x < -10
    # 0 si -10 <= x <= 10
    # 1 si x > 10

    x = 5  # ou quoi que ce soit d'autre

    valeur = -1 if x < -10 else (0 if x <= 10 else 1)

    print(valeur)
