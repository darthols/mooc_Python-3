#!/usr/bin/env python3
# coding: utf8

def agenda(nom, prenom, tel='?'):
    return {'nom': nom, 'prenom': prenom, 'tel': tel}


def f(*t):
    print(t)


def g(**d):
    print(d)


def show(a, b):
    print(a, b)


if __name__ == "__main__":
    ag = agenda('idle', 'eric', '07070707')
    print(ag)
    ag = agenda(tel='070707707', nom='idle', prenom='eric')
    print(ag)
    ag = agenda('idle', 'eric')
    print(ag)

    f()
    f(1)
    f(1, 2, 3, 4, 5)

    g()
    g(nom='idle', prenom='eric')

    d = {'a': 1, 'b': 2}
    show(**d)

    print(1, 2, sep=';', end='FIN\n')
    pp = {'sep': ';', 'end': 'FIN\n'}
    print(1, 2, **pp)
