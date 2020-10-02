#!/usr/bin/env python3
# coding: utf8
"""
Plusieurs variables dans une boucle for
"""

# Il est possible de faire une boucle for qui itère sur une seule liste mais qui agit sur plusieurs variables,
# comme ceci :
entrees = [(1, 2), (3, 4), (5, 6)]
for a, b in entrees:
    print(f"a={a} b={b}")

# À chaque itération, on trouve dans entree un tuple (d'abord (1, 2), puis à l'itération suivante (3, 4), etc.) ;
# à ce stade les variables a et b vont être affectées à, respectivement, le premier et le deuxième élément du
# tuple, exactement comme dans le sequence unpacking. Cette mécanique est massivement utilisée en Python.


# La fonction zip

# Voici un exemple très simple qui utilise la technique que l'on vient de voir.
# Imaginons qu'on dispose de deux listes de longueurs égales, dont on sait que les entrées correspondent une à une,
# comme par exemple :
villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6]

# Afin d'écrire facilement un code qui "associe" les deux listes entre elles, Python fournit une fonction built-in
# baptisée zip ; voyons ce qu'elle peut nous apporter sur cet exemple :
list(zip(villes, populations))

# On le voit, on obtient en retour une liste composée de tuples. On peut à présent écrire une boucle for comme ceci
for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)

# Qui est, nous semble-t-il, beaucoup plus lisible que ce que l'on serait amené à écrire avec des langages plus
# traditionnels.

# Tout ceci se généralise naturellement à plus de deux variables :
for i, j, k in zip(range(3), range(100, 103), range(200, 203)):
    print(f"i={i} j={j} k={k}")

# Remarque : lorsqu'on passe à zip des listes de tailles différentes, le résultat est tronqué, c'est l'entrée de
# plus petite taille qui détermine la fin du parcours.

# on n'itère que deux fois
# car le premier argument de zip est de taille 2
for units, tens in zip([1, 2], [10, 20, 30, 40]):
    print(units, tens)


# La fonction enumerate

# Une autre fonction très utile permet d'itérer sur une liste avec l'indice dans la liste, il s'agit de enumerate :
for i, ville in enumerate(villes):
    print(i, ville)

# Cette forme est plus simple et plus lisible que les formes suivantes qui sont équivalentes, mais qui ne sont pas
# pythoniques :
for i in range(len(villes)):
    print(i, villes[i])

for i, ville in zip(range(len(villes)), villes):
    print(i, ville)
