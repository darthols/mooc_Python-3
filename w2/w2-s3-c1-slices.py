# coding: utf-8
# # Les slices en Python

chaine = "abcdefghijklmnopqrstuvwxyz"
print("chaine :", chaine)


# ### Slice sans pas

# On a vu en cours qu'une slice permet de désigner toute une plage d'éléments d'une séquence :
print("chaine[2:6] :", chaine[2:6])


# ### Conventions de début et fin

# Les débutants ont parfois du mal avec les bornes. Il faut se souvenir que :
# 
# * les indices **commencent** comme toujours **à zéro** ;
# * le premier indice `debut` est **inclus** ;
# * le second indice `fin` est **exclu** ;
# * on obtient en tout `fin-debut` items dans le résultat.
# 
# Ainsi, ci-dessus, le résultat contient `6 - 2 = 4` éléments.

# Pour vous aider à vous souvenir des conventions de début et de fin, souvenez-vous qu'on veut pouvoir facilement
# juxtaposer deux slices qui ont une borne commune.
# chaine[a:b] + chaine[b:c] == chaine[a:c]
chaine[0:3] + chaine[3:7] == chaine[0:7]
print("chaine[0:3] + chaine[3:7] :", chaine[0:3] + chaine[3:7])
print("chaine[0:7] :", chaine[0:7])


# #### Bornes omises

# On peut omettre une borne :
# si on omet la première borne, cela signifie que la slice commence au début de l'objet
print("chaine[:6]:", chaine[:6])

# et bien entendu c'est la même chose si on omet la deuxième borne
print("chaine[2:] :", chaine[2:])

# ou même omettre les deux bornes, auquel cas on fait une copie de l'objet - on y reviendra plus tard
print("chaine[:] :", chaine[:])


# #### Indices négatifs

# On peut utiliser des indices négatifs pour compter à partir de la fin :
print("chaine[3:-3] :", chaine[3:-3])

print("chaine[-3:] :", chaine[-3:])


# ### Slice avec pas

# Il est également possible de préciser un *pas*, de façon à ne choisir par exemple, dans la plage donnée, qu'un
# élément sur deux :

# le pas est précisé après un deuxième deux-points (:)
# ici on va choisir un caractère sur deux dans la plage [3:-3]
print("chaine[3:-3:2] :", chaine[3:-3:2])


# Comme on le devine, le troisième élément de la slice, ici `2`, détermine le pas. On ne retient donc, dans la
# chaîne `defghi...` que `d`, puis `f`, et ainsi de suite.
# 
# On peut préciser du coup la borne de fin (ici `-3`) avec un peu de liberté, puisqu'ici on obtiendrait un résultat
# identique avec `-4`.
print("chaine[3:-4:2] :", chaine[3:-4:2])


# ### Pas négatif

# Il est même possible de spécifier un pas négatif. Dans ce cas, de manière un peu contre-intuitive, il faut préciser
# un début (le premier indice de la slice) qui soit *plus à droite* que la fin (le second indice).
# 
# Pour prendre un exemple, comme l'élément d'indice `-3`, c'est-à-dire `x`, est plus à droite que l'élément d'indice
# `3`, c'est-à-dire `d`, évidemment si on ne précisait pas le pas (qui revient à choisir un pas égal à `1`), on
# obtiendrait une liste vide :
print("chaine[-3:3] :", chaine[-3:3])


# Si maintenant on précise un pas négatif, on obtient cette fois :
print("chaine[-3:3:-2] :", chaine[-3:3:-2])


# ### Conclusion

# À nouveau, souvenez-vous que tous ces mécanismes fonctionnent avec de nombreux autres types que les chaînes de
# caractères. En voici deux exemples qui anticipent tous les deux sur la suite, mais qui devraient illustrer les
# vastes possibilités qui sont offertes avec les slices.

# #### Listes

# Par exemple sur les listes :
liste = [0, 2, 4, 8, 16, 32, 64, 128]
print("liste :", liste)

print("liste[-1:1:-2] :", liste[-1:1:-2])


# Et même ceci, qui peut être déroutant. Nous reviendrons dessus.
liste[2:4] = [100, 200, 300, 400, 500]
print("liste :", liste)


# ## Complément - niveau avancé

# #### `numpy`
# La bibliothèque `numpy` permet de manipuler des tableaux ou des matrices. En anticipant sur son usage que nous
# reverrons bien entendu en détail, voici un aperçu de ce que l'on peut faire avec des slices sur des objets `numpy`

# ces deux premières cellules sont à admettre on construit un tableau ligne
import numpy as np

un_cinq = np.array([1, 2, 3, 4, 5])
print("un_cinq :", un_cinq)


# ces deux premières cellules sont à admettre
# on le combine avec lui-même - et en utilisant une slice un peu magique
# pour former un tableau carré 5x5

array = 10 * un_cinq[:, np.newaxis] + un_cinq
print("array :\n", array)


# Sur ce tableau de taille 5x5, nous pouvons aussi faire du slicing et extraire le sous-tableau 3x3 au centre :
centre = array[1:4, 1:4]
print("centre :\n", centre)


# On peut bien sûr également utiliser un pas :
coins = array[::4, ::4]
print("coins :", coins)


# Ou bien retourner complètement dans une direction :
tete_en_bas = array[::-1,:]
print("tete_en_bas :\n", tete_en_bas)
