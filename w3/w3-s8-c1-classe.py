#!/usr/bin/env python3
# coding: utf8


class C:

    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        self.mots = [m.upper() for m in self.mots]

    def __str__(self):
        return "\n".join(self.mots)


if __name__ == "__main__":
    c = C("Je fais un MOOC sur Python")
    print(c.mots)
    c.upper()
    print(c.mots)
    print(c)
