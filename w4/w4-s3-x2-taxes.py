#!/usr/bin/env python3
# coding: utf8
"""
Taxes

On se propose d'écrire une fonction taxes qui calcule le montant de l'impôt sur le revenu au Royaume-Uni.

Le barème est publié ici par le gouvernement anglais, voici les données de 2020 qui sont utilisées pour l'exercice :

Tranche	Revenu imposable	                Taux
------------------------------------------  ----
Non imposable	jusque £12.500	            0%
Taux de base	£12.501 à £50.000           20%
Taux élevé	£50.001 à £150.000	            40%
Taux supplémentaire	au delà de £150.000     45%
"""

import numpy as np
import matplotlib.pyplot as plt


# les tranches en ordre décroissant
bareme = (
    (150_000, 45),
    (50_000, 40),
    (12_500, 20),
    (0, 0),
)


def taxes(revenu):
    """
    U.K. income taxes calculator
    https://www.gov.uk/income-tax-rates
    """
    montant = 0
    for seuil, taux in bareme:
        if revenu > seuil:
            montant += (revenu - seuil) * taux // 100
            revenu = seuil
    return montant


if __name__ == "__main__":
    assert taxes(0) == 0
    assert taxes(50000) == 7500
    assert taxes(12500) == 0

    # Représentation graphique

    plt.ion()

    X = np.linspace(0, 200_000)
    Y = [taxes(x) for x in X]
    plt.plot(X, Y)
    plt.show()
    # plt.waitforbuttonpress()
