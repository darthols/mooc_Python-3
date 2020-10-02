#!/usr/bin/env python3
# coding: utf8

# load data from files
import json
from pprint import pprint

"""
De manière à optimiser le volume de données à transférer, l'API de MarineTraffic offre deux modes pour obtenir
les données :
    mode étendu : chaque mesure (bateau x position x temps) est accompagnée de tous les détails du bateau (id, nom,
    pays de rattachement, etc.) ;
    mode abrégé : chaque mesure est uniquement attachée à l'id du bateau.
En effet, chaque bateau possède un identifiant unique qui est un entier, que l'on note id.

Format des données¶
Le format de ces données est relativement simple, il s'agit dans les deux cas d'une liste d'entrées - une par bateau.

Chaque entrée à son tour est une liste qui contient :
    mode étendu: [id, latitude, longitude, date_heure, nom_bateau, code_pays, ...]
    mode abrégé: [id, latitude, longitude, date_heure]

Une entrée étendue est une liste qui ressemble à ceci
    [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE']
Une entrée abrégée ressemble à ceci
    [227254910, 49.91799, -5.315172, '2013-10-08T22:59:00']

On précise également que les deux listes extended et abbreviated :
    possèdent exactement le même nombre d'entrées ;
    et correspondent aux mêmes bateaux ;
    mais naturellement à des moments différents ;
    et pas forcément dans le même ordre.
"""


def index(extended):
    """
    Ecrire une fonction index qui calcule, à partir de la liste des données étendues, un dictionnaire qui est :
        indexé par l'id de chaque bateau ;
        et qui a pour valeur la liste qui décrit le bateau correspondant.
    :param extended:
    :return:
    """
    return {bateau[0]: bateau for bateau in extended}


def merge(extended, abbreviated):
    """
    Ecrire une fonction merge qui fasse une consolidation des données, de façon à obtenir en sortie un dictionnaire :
        id -> [nom_bateau, code_pays, position_etendu, position_abrege]
    dans lequel les deux objets position sont tous les deux des tuples de la forme :
        (latitude, longitude, date_heure)
    :param extended:
    :param abbreviated:
    :return:
    """
    # mode étendu: [id, latitude, longitude, date_heure, nom_bateau, code_pays, ...]
    #                0    1           2        3            4           5
    result = {}
    # for id, latitude, longitude, date_heure, nom_bateau, code_pays, *_ in extended:
    #     result[id] = [nom_bateau, code_pays, (latitude, longitude, date_heure)]
    # for id, latitude, longitude, date_heure in abbreviated:
    #     result[id].append((latitude, longitude, date_heure))

    result = {ext[0]: [ext[4], ext[5], (ext[1], ext[2], ext[3])] for ext in extended}
    for id, latitude, longitude, date_heure in abbreviated:
        result[id].append((latitude, longitude, date_heure))
    return result


if __name__ == "__main__":

    with open("data/marine-e1-ext.json", encoding="utf-8") as feed:
        extended_full = json.load(feed)

    with open("data/marine-e1-abb.json", encoding="utf-8") as feed:
        abbreviated_full = json.load(feed)

    result_index = index(extended_full)

    for key, value in result_index.items():
        print("==== clé")
        pprint(key)
        print("==== valeur")
        pprint(value)
        break

    result_merge = merge(extended_full, abbreviated_full)

    for key, value in result_merge.items():
        print("==== clé")
        pprint(key)
        print("==== valeur")
        pprint(value)
        break

