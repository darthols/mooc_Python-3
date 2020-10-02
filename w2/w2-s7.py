# coding: utf-8

import math


a = [1, 4, 18, 29, 13]

b = []
for i in a:
    b.append(math.log(i))
print("Boucle for :", b)

# Par la compréhension de liste
b = [math.log(i) for i in a]
print("Compréhension de liste :", b)

# ajout d'un test pour éliminer les valeurs négatives
a.append(-1)
b = [math.log(i) for i in a if i > 0]
print("Compréhension de liste avec test :", b)

prenom = ['Alice', 'sonia', 'eVe', 'BOB']
prenom = [str.capitalize(p) for p in prenom]
print("Compréhension de liste avec des strings :", prenom)
