#!/usr/bin/env python3
# coding: utf8

# load data from files
import json

"""
De manière à optimiser le volume de données à transférer, l'API de MarineTraffic offre deux modes pour obtenir
les données :
    mode étendu : chaque mesure (bateau x position x temps) est accompagnée de tous les détails du bateau (id, nom,
    pays de rattachement, etc.) ;
    mode abrégé : chaque mesure est uniquement attachée à l'id du bateau.
En effet, chaque bateau possède un identifiant unique qui est un entier, que l'on note id.

Format des données
Le format de ces données est relativement simple, il s'agit dans les deux cas d'une liste d'entrées - une par bateau.

Chaque entrée à son tour est une liste qui contient :
    mode étendu: [id, latitude, longitude, date_heure, nom_bateau, code_pays, ...]
    mode abrégé: [id, latitude, longitude, date_heure]

Une entrée étendue est une liste qui ressemble à ceci
    [255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '', 'ZEEBRUGGE']
Une entrée abrégée ressemble à ceci
    [227254910, 49.91799, -5.315172, '2013-10-08T22:59:00']
"""


# mode étendu: [id, latitude, longitude, date_heure, nom_bateau, code_pays, ...]
#                0    1           2        3            4           5

def diff(extended, abbreviated):
    """
    Retourne un tuple à trois éléments :
        l'ensemble (set) des noms des bateaux présents dans extended mais pas dans abbreviated ;
        l'ensemble des noms des bateaux présents dans extended et dans abbreviated ;
        l'ensemble des id des bateaux présents dans abbreviated mais pas dans extended (par construction, les données
        ne nous permettent pas d'obtenir les noms de ces bateaux).
    :param extended:
    :param abbreviated:
    :return:
    """
    ext_id_set = set([bateau[0] for bateau in extended])
    abb_id_set = set([bateau[0] for bateau in abbreviated])

    # id des bateaux présents seulement dans extended
    ext_only = ext_id_set - abb_id_set

    # id des bateaux présents dans les deux listes
    intersection = abb_id_set & ext_id_set

    # Remplacement des ids par les noms des bateaux
    ext_only_name = set(bateau[4] for bateau in extended if bateau[0] in ext_only)
    intersection_name = set(bateau[4] for bateau in extended if bateau[0] in intersection)
    return ext_only_name, intersection_name, abb_id_set - ext_id_set


def show_result(extended, abbreviated, result):
    """
    Affiche divers décomptes sur les arguments en entrée et en sortie de diff
    """
    print(10 * '-', "Les entrées")
    print(f"Dans extended: {len(extended)} entrées")
    print(f"Dans abbreviated: {len(abbreviated)} entrées")
    print(10 * '-', "Le résultat du diff")
    extended_only, both, abbreviated_only = result
    print(f"Dans extended mais pas dans abbreviated {len(extended_only)}")
    print(f"Dans les deux {len(both)}")
    print(f"Dans abbreviated mais pas dans extended {len(abbreviated_only)}")


if __name__ == "__main__":
    with open("data/marine-e2-ext.json", encoding="utf-8") as feed:
        extended_full = json.load(feed)

    with open("data/marine-e2-abb.json", encoding="utf-8") as feed:
        abbreviated_full = json.load(feed)

    # le résultat de votre fonction sur des données plus vastes
    # attention, show_result fait des hypothèses sur le type de votre résultat
    # aussi si vous essayez d'exécuter ceci avec comme fonction diff
    # la version vide qui est dans le notebook original
    # cela peut provoquer une exception
    diff_full = diff(extended_full, abbreviated_full)
    show_result(extended_full, abbreviated_full, diff_full)

    assert diff(
        [[305686000, 49.19304, -5.034783, '2013-10-08T21:50:00', 'INDUSTRIAL '          'KELLY', 'AG', '', 'ESBJERG'],
         [248730000, 49.94616, -2.994563, '2013-10-08T21:51:00', 'SCALI REALI', 'MT', '', 'ROTTERDAM-MAASVLAKTE'],
         [248730000, 49.94616, -2.994563, '2013-10-08T21:51:00', 'SCALI REALI', 'MT', '', 'ROTTERDAM-MAASVLAKTE'],
         [248730000, 49.94616, -2.994563, '2013-10-08T21:51:00', 'SCALI REALI', 'MT', '', 'ROTTERDAM-MAASVLAKTE'],
         [248730000, 49.94616, -2.994563, '2013-10-08T21:51:00', 'SCALI REALI', 'MT', '', 'ROTTERDAM-MAASVLAKTE'],
         [245718000, 49.8989, -5.240509, '2013-10-08T21:51:00', 'AMAZONE', 'NL', '', 'DUNKERQUE'],
         [228240600, 47.22783, -2.850353, '2013-10-08T21:51:00', 'QUENTIN '          'GREGOIRE', 'FR', '',
          'LES SABLES D OLONNE']],
        [[245718000, 49.92569, -5.524793, '2013-10-08T22:59:00'],
         [228240600, 47.22262, -2.786693, '2013-10-08T22:58:00'],
         [227115520, 48.09115, -4.333058, '2013-10-08T22:55:00'],
         [228240900, 47.19841, -2.723277, '2013-10-08T22:55:00']]
    ) == (
               {'INDUSTRIAL KELLY', 'SCALI REALI'},
               {'AMAZONE', 'QUENTIN GREGOIRE'},
               {227115520, 228240900})
