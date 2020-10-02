# coding: utf-8
"""
Ecrire une fonction dans le même esprit que la fonction polynomiale du notebook précédent.
Cette fois, chaque ligne contient, séparés par des points-virgules, une liste d'entiers, et on veut obtenir
une nouvelle chaîne avec les carrés de ces entiers, séparés par des deux-points.

À nouveau les lignes peuvent être remplies de manière approximative, avec des espaces, des tabulations, ou même
des points-virgules en trop, que ce soit au début, à la fin, ou au milieu d'une ligne.
"""


def carre(line):
    # on enlève les espaces et les tabulations
    line = line.replace(' ', '').replace('\t','')
    # la ligne suivante fait le plus gros du travail
    # d'abord on appelle split() pour découper selon les ';'
    # dans le cas où on a des ';' en trop, on obtient dans le résultat du split un 'token' vide, que l'on ignore ici
    # avec la clause 'if token'
    # enfin on convertit tous les tokens restants en entiers avec int() en éliminant les entrées vides qui
    # correspondent à des point-virgules en trop
    entiers = [int(token) for token in line.split(";") if token]

    # il n'y a plus qu'à mettre au carré, retraduire en strings, et à recoudre le tout avec join et ':'
    return ":".join([str(entier**2) for entier in entiers])
