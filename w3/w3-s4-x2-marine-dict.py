#!/usr/bin/env python3
# coding: utf8

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

    De manière plus imagée, si :
        extended = [ bateau1, bateau2, ... ]
    Et si :
        bateau1 = [ id1, latitude, ... ]
    On doit obtenir comme résultat de index un dictionnaire :
        {
            id1 -> [ id_bateau1, latitude, ... ],
            id2 ...
        }

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

    assert index([
        [227254910, 49.91799, -5.315172, '2013-10-08T22:59:00'],
        [255801560, 49.25383, -4.784833, '2013-10-08T22:59:00'],
        [992271012, 47.64748, -3.509307, '2013-10-08T22:56:00'],
        [227844000, 47.13057, -3.126982, '2013-10-08T22:58:00']
    ]) == {
               227254910: [227254910, 49.91799, -5.315172, '2013-10-08T22:59:00'],
               227844000: [227844000, 47.13057, -3.126982, '2013-10-08T22:58:00'],
               255801560: [255801560, 49.25383, -4.784833, '2013-10-08T22:59:00'],
               992271012: [992271012, 47.64748, -3.509307, '2013-10-08T22:56:00']
           }

    assert index([
        [992271012, 47.64744, -3.509282, '2013-10-08T21:50:00', 'PENMEN', 'FR', '', ''],
        [227254910, 49.94479, -5.137455, '2013-10-08T21:51:00', 'LAURELINE', 'FR', '', 'CHERBOURG'],
        [227844000, 47.23206, -2.913887, '2013-10-08T21:51:00', 'NEPTUNE III', 'FR', '', ''],
        [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE']
    ]) == {
               227254910: [227254910, 49.94479, -5.137455, '2013-10-08T21:51:00', 'LAURELINE', 'FR', '', 'CHERBOURG'],
               227844000: [227844000, 47.23206, -2.913887, '2013-10-08T21:51:00', 'NEPTUNE III', 'FR', '', ''],
               255801560: [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE'],
               992271012: [992271012, 47.64744, -3.509282, '2013-10-08T21:50:00', 'PENMEN', 'FR', '', '']
           }

    result_index = index([
        [992271012, 47.64744, -3.509282, '2013-10-08T21:50:00', 'PENMEN', 'FR', '', ''],
        [227254910, 49.94479, -5.137455, '2013-10-08T21:51:00', 'LAURELINE', 'FR', '', 'CHERBOURG'],
        [227844000, 47.23206, -2.913887, '2013-10-08T21:51:00', 'NEPTUNE III', 'FR', '', ''],
        [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE']
    ])

    for key, value in result_index.items():
        print("==== clé")
        pprint(key)
        print("==== valeur")
        pprint(value)
        break

    assert merge(
        [[992271012, 47.64744, -3.509282, '2013-10-08T21:50:00', 'PENMEN', 'FR', '', ''],
         [227254910, 49.94479, -5.137455, '2013-10-08T21:51:00', 'LAURELINE', 'FR', '', 'CHERBOURG'],
         [227844000, 47.23206, -2.913887, '2013-10-08T21:51:00', 'NEPTUNE III', 'FR', '', ''],
         [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE']],
        [[227254910, 49.91799, -5.315172, '2013-10-08T22:59:00'],
         [255801560, 49.25383, -4.784833, '2013-10-08T22:59:00'],
         [992271012, 47.64748, -3.509307, '2013-10-08T22:56:00'],
         [227844000, 47.13057, -3.126982, '2013-10-08T22:58:00']]
    ) == {
               227254910: ['LAURELINE', 'FR', (49.94479, -5.137455, '2013-10-08T21:51:00'),
                           (49.91799, -5.315172, '2013-10-08T22:59:00')],
               227844000: ['NEPTUNE III', 'FR', (47.23206, -2.913887, '2013-10-08T21:51:00'),
                           (47.13057, -3.126982, '2013-10-08T22:58:00')],
               255801560: ['AUTOPRIDE', 'PT', (49.3815, -4.412167, '2013-10-08T21:51:00'),
                           (49.25383, -4.784833, '2013-10-08T22:59:00')],
               992271012: ['PENMEN', 'FR', (47.64744, -3.509282, '2013-10-08T21:50:00'),
                           (47.64748, -3.509307, '2013-10-08T22:56:00')]
           }
