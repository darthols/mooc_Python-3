#!/usr/bin/env python3
# coding: utf8

"""
Ecrire une fonction qui lit un fichier texte, et construit (et retourne) un dictionnaire Python qui représente ce graphe.
cat data/graph1.txt
    s1 10 s2
    s2 12 s3
    s3 25 s1
    s1 14 s3
qui signifierait :
    un graphe à 3 sommets s1, s2 et s3;
    et 4 arêtes
    une entre s1 et s2 de longueur 10;
    une entre s2 et s3 de longueur 12;
    etc…

Dans cet exercice on choisit :

de modéliser le graphe comme un dictionnaire indexé sur les (noms de) sommets ;
et chaque valeur est une liste de tuples de la forme (suivant, longueur), dans l'ordre d'apparition dans le fichier d'entrée.
"""


def graph_dict(filename):
    graph = {}
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            tokens = line.split()
            if tokens[0] not in graph:
                graph[tokens[0]] = []
            graph[tokens[0]].append((tokens[2], int(tokens[1])))
    return graph


if __name__ == "__main__":
    # graph_dict('data/graph1.txt')
    assert graph_dict('data/graph1.txt') == {'s1': [('s2', 10), ('s3', 14)], 's2': [('s3', 12)], 's3': [('s1', 25)]}

    assert graph_dict('data/graph2.txt') == {'lyon': [('marseille', 300)],
                                             'marseille': [('nice', 200), ('bordeaux', 500)],
                                             'metz': [('lyon', 500)],
                                             'paris': [('metz', 300)]}

    assert graph_dict('data/graph3.txt') == {'inst': [('while', 1)],
                                             'start': [('while', 1)],
                                             'while': [('inst', 1), ('end', 1)]}
