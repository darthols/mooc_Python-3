#!/usr/bin/env python3
# coding: utf8

"""
On veut implémenter une classe pour manipuler une queue d'événements. La logique de cette classe est que :
    on la crée sans argument ;
    on peut toujours ajouter un élément avec la méthode incoming ;
    et tant que la queue contient des éléments on peut appeler la méthode outgoing, qui retourne et enlève un élément
    dans la queue.

Cette classe s'appelle Fifo pour First In, First Out, c'est-à-dire que les éléments retournés par outgoing le sont dans
le même ordre où ils ont été ajoutés.

La méthode outgoing retourne None lorsqu'on l'appelle sur une pile vide.
"""


a, b, c = 1, 1, 1


def g():
    b, c = 2, 4
    b = b + 10

    def h():
        c = 5
        print(a, b, c)
    h()


if __name__ == "__main__":
    g()
    print(a, b, c)
