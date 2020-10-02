#!/usr/bin/env python3
# coding: utf8
"""
Fibonacci
"""


def fibonacci(n):
    return 1 if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    entier = int(input("Entrer un entier :"))
    print(f"fibonacci({entier}) = {fibonacci(entier)}")
