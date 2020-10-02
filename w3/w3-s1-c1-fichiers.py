#!/usr/bin/env python3
# coding: utf8
"""
Les fichiers
"""


# f = open('C:\\tmp\\spam.txt')
# Utilisation de raw string
f = open(r'C:\tmp\spam.txt', 'w', encoding='utf8')
for i in range(100):
    f.write(f"ligne {i + 1}\n")
f.close()


f = open(r'C:\tmp\spam.txt', 'r', encoding='utf8')
f2 = open(r'C:\tmp\spam2.txt', 'w', encoding='utf8')
for line in f:
    line = line.split()
    line[0] = line[0].upper()
    f2.write(",".join(line) + "\n")
f.close()
f2.close()

# Utilisation du context manager pour fermer automatiquement le fichier lorsqu'il n'est plus utilisé (fin du bloc)
with open(r'C:\tmp\spam.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line, end="")

# on ouvre le fichier en mode 'a' comme append (= ajouter)
with open(r'C:\tmp\spam.txt', 'a', encoding='utf8') as f:
    for i in range(100, 102):
        f.write(f"{i}\n")


# Utilisation de fichiers en mode binaire
with open(r'C:\tmp\spam.bin', 'wb') as f:
    for i in range(100):
        f.write(b'\x3d')


# une autre façon de montrer tout le contenu du fichier
with open(r'C:\tmp\spam.txt', encoding='utf-8') as entree:
    full_contents = entree.read()
    print(f"Contenu complet\n{full_contents}", end="")

# lire dans le fichier deux blocs de quatre caractères
with open(r'C:\tmp\spam.txt', encoding='utf-8') as entree:
    for bloc in range(2):
        print(f"Bloc {bloc} >>{repr(entree.read(4))}<<")
