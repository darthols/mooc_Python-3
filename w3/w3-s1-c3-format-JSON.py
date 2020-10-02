#!/usr/bin/env python3
# coding: utf8
"""
Format JSON
"""

import json

# En partant d'une donnée construite à partir de types de base
data = [
    # des types qui ne posent pas de problème
    [1, 2, 'a', [3.23, 4.32], {'eric': 32, 'jean': 43}],
    # un tuple
    (1, 2, 3),
]

# sauver ceci dans un fichier
with open("../data/s1.json", "w", encoding='utf-8') as json_output:
    json.dump(data, json_output)

# et relire le résultat
with open("../data/s1.json", encoding='utf-8') as json_input:
    data2 = json.load(json_input)


print("data  :", data)
print("data2 :", data2)

"""
Limitations de json

Certains types de base ne sont pas supportés par le format JSON (car ils ne sont pas natifs en JavaScript), 
c'est le cas notamment pour :
    tuple, qui se fait encoder comme une liste ;
    complex, set et frozenset, que l'on ne peut pas encoder du tout (sans étendre la bibliothèque).
"""

"""
Le format csv
-------------
Le format csv pour Comma Separated Values, originaire du monde des tableurs, peut rendre service à l'occasion, 
il est proposé dans le module csv (https://docs.python.org/3/library/csv.html).

Le format pickle
----------------
Le format pickle remplit une fonctionnalité très voisine de JSON, mais est spécifique à Python. C'est pourquoi, malgré 
des limites un peu moins sévères, son usage tend à rester plutôt marginal pour l'échange de données, on lui préfère 
en général le format JSON.
Par contre, pour la sauvegarde locale d'objets Python (pour, par exemple, faire des points de reprises d'un programme), 
il est très utile. Il est implémenté dans le module pickle (https://docs.python.org/3/library/pickle.html).

Le format XML
-------------
Cela dit, la puissance, et donc le coût, de XML et JSON ne sont pas du tout comparables, XML étant beaucoup plus 
flexible mais au prix d'une complexité de mise en oeuvre très supérieure.

Il existe plusieurs souches différentes de bibliothèques prenant en charge le format XML, qui sont introduites dans
le module xml (https://docs.python.org/3/library/xml.html).
"""