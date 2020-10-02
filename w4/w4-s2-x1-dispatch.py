#!/usr/bin/env python3
# coding: utf8
"""
Dispatch
"""


def dispatch1(a, b):
    if a % 2:
        # a est impair
        result = a**2 - b**2 if b % 2 else (a - 1) * b
    else:
        # a est pair
        result = a * (b - 1) if b % 2 else a**2 + b**2
    return result


def dispatch2(a, b, A, B):
    if a in A:
        result = a**2 + b**2 if b in B else a * (b - 1)
    else:
        result = (a - 1) * b if b in B else a**2 + b**2
    return result


if __name__ == "__main__":
    assert dispatch1(3, 7) == -40
    assert dispatch2(3, 7, (2, 4, 6), {8, 10, 6}) == 58
    assert dispatch2(3, 8, (2, 4, 6), {8, 10, 6}) == 16
    assert dispatch2(3, 9, (2, 4, 6), {8, 10, 6}) == 90
    assert dispatch2(4, 7, [2, 4, 6], {8, 10, 6}) == 24
    assert dispatch2(4, 8, [2, 4, 6], {8, 10, 6}) == 80
    assert dispatch2(4, 9, [2, 4, 6], {8, 10, 6}) == 32
