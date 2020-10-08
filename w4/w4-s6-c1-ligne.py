#!/usr/bin/env python3
# coding: utf8

# Interface pour dessiner une ligne
def ligne(x1, y1, x2, y2, couleur="noir"):
    """dessine la ligne (x1, y1) -> (x2, y2) dans la couleur spécifiée"""
    print(f"la ligne ({x1}, {y1}) -> ({x2}, {y2}) en {couleur}")


def ligne_rouge(*arguments, **keywords):
    keywords['couleur'] = 'rouge'
    return ligne(*arguments, **keywords)


if __name__ == "__main__":
    ligne_rouge(1, 2, 4, 5)
