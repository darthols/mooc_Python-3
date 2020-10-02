#
"""
On se donne une fonction polynomiale :
𝑃(𝑥) = 2𝑥**2 − 3𝑥 − 2

Ecrire une fonction liste_P qui prend en argument une liste de nombres réels 𝑥 et qui retourne la liste des valeurs
𝑃(𝑥).
"""

import numpy as np
import matplotlib.pyplot as plt


def P(x):
    """
    Fonction polynomiale : 𝑃(𝑥) = 2𝑥**2 − 3𝑥 − 2
    :param x: argument
    :return: valeur de 𝑃(𝑥)
    """
    return(2 * x**2 - 3 * x - 2)


def liste_P(liste_x):
    return [P(x) for x in liste_x]


# validation de l'exercice
assert liste_P([0, 1, 2, 3, 4]) == [-2, -3, 0, 7, 18]


# Visualisation de la courbe
# un échantillon des X entre -10 et 10
X = np.linspace(-10, 10)

# et les Y correspondants
Y = liste_P(X)

# on n'a plus qu'à dessiner
plt.plot(X, Y)
plt.show()
