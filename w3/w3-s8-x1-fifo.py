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


class Fifo:

    def __init__(self):
        self.queue = []

    def incoming(self, value):
        self.queue.append(value)

    def outgoing(self):
        try:
            result = self.queue[0]
            self.queue = self.queue[1:]
            return result
        except IndexError:
            return None

    def __str__(self):
        return "\n".join([elt for elt in self.queue])


if __name__ == "__main__":

    f = Fifo()
    assert f.incoming(1) is None
    assert f.incoming(2) is None
    assert f.outgoing() == 1
    assert f.outgoing() == 2
    assert f.incoming(3) is None
    assert f.incoming(4) is None
    assert f.outgoing() == 3
    assert f.outgoing() == 4
