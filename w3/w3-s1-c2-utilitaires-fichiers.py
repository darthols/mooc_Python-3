#!/usr/bin/env python3
# coding: utf8
"""
Fichiers et utilitaires
"""

from pathlib import Path

"""
Le module pathlib

pathlib offre une interface orientée objet avec la classe Path.
"""

nom = r"C:\tmp\fichier-temoin.txt"

# Pour commencer, nous allons vérifier si le fichier en question existe.
# Pour ça nous créons un objet qui est une instance de la classe Path, comme ceci:
#     on crée un objet de la classe Path, associé au nom de fichier
path = Path(nom)

# on peut savoir si le fichier existe avec la méthode exists()
print("Fichier existant ? :", path.exists())

# si j'écris dedans je le crée
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n')

print("Fichier existant ? :", path.exists())

# Cette méthode retourne (en un seul appel système) les métadonnées agrégées
print(path.stat())

# L'objet retourné par cette méthode stat est un namedtuple

# On accède aux différentes informations comme ceci:

# la taille du fichier en octets est de 11
print("st_size", path.stat().st_size)

# La date de dernière modification, sous forme d'un nombre : c'est le nombre de secondes depuis le 1er Janvier 1970
mtime = path.stat().st_mtime
print("mtime :", mtime)

# Rendre la date lisible :
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime)
print("mtime_datetime :", mtime_datetime)

# Formatter la date pour n'obtenir que l'heure et la minute
print("hhmm : " + f"{mtime_datetime:%H:%M}")

# Détruire le fichier seulement dans le cas où il existe :
try:
    path.unlink()
except FileNotFoundError:
    print("no need to remove")


# ## Recherche de fichiers

# Maintenant je voudrais connaître la liste des fichiers de nom *.json dans le directory data.
# La méthode la plus naturelle consiste à créer une instance de Path associée au directory lui-même:
dirpath = Path('../data/')

# Sur cet objet la méthode glob nous retourne un itérable qui contient ce qu'on veut:
# tous les fichiers *.json dans le répertoire data/
for json in dirpath.glob("*.json"):
    print(json)


# ## Type de path

# Le type de l'objet path est un objet de type PosixPath sur Linux ou WindowsPath sur Windows qui est une
# sous-classe de la classe Path
print(type(path))
