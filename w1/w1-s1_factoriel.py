#!/usr/bin/env python3
# coding: utf8
"""
Factoriel
"""


def factoriel(n):
    """factoriel"""
    if n <= 1:
        return 1
    else:
        return n * factoriel(n - 1)


print(factoriel(100))
