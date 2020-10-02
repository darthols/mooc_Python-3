#!/usr/bin/env python3
# coding: utf8


def read_set(filename):
    """
    Construit un ensemble à partir du contenu d'un fichier.
    :param filename: fichier
    :return: set construit
    """
    # with open(filename, 'r', encoding='utf8') as f:
    #     result = set()
    #     for line in f:
    #         result.add(line.strip())
    # return result
    #
    with open(filename, 'r', encoding='utf8') as f:
        return {line.strip() for line in f}


def search_in_set(filename_reference, filename):
    """
    Retourne une liste, contenant pour chaque ligne du fichier filename un tuple avec :
        la ligne (sans les espaces de début et de fin, ni la fin de ligne);
        un booléen qui indique si ce mot est présent dans les références ou pas.
    :param filename_reference: nom d'un fichier contenant des mots de référence.
    :param filename: nom d'un fichier contenant des mots, dont on veut savoir s'ils sont ou non dans les références.
    :return: liste résultante
    """
    ref = read_set(filename_reference)
    # result = []
    # with open(filename, 'r', encoding='utf8') as f:
    #     for line in f:
    #         elt = line.strip()
    #         result.append((elt, elt in ref))
    # return result
    #
    with open(filename, 'r', encoding='utf8') as f:
        return [(line.strip(), line.strip() in ref) for line in f]


if __name__ == "__main__":
    assert read_set('data/setref1.txt') == {'12', '4615', '6158', '9228'}
    assert read_set('data/setref2.txt') == {'1560', '26', '4609', '5132', '523', '7694', '7697', '9731'}

    assert search_in_set('data/setref1.txt', 'data/setsample1.txt') == [
        ('2048', False),
        ('8192', False),
        ('9228', True),
        ('2049', False),
        ('3', False),
        ('4', False),
        ('2053', False),
        ('2054', False),
        ('6158', True),
        ('4099', False),
        ('8', False),
        ('12', True)
    ]
