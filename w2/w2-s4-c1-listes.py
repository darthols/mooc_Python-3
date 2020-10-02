# coding: utf-8

# # Méthodes spécifiques aux listes

# ## Complément - niveau basique

# ### Trouver l'information

# Pour commencer, rappelons comment retrouver la liste des méthodes définies sur le type `list` :
help(list)


# Ignorez les méthodes dont le nom commence et termine par `__` (nous parlerons de ceci en semaine 6),  vous trouvez
# alors les méthodes utiles listées entre `append` et `sort`.
# 

# Donnons-nous pour commencer une liste témoin :
liste = [0, 1, 2, 3]
print('liste', liste)


# **Avertissements** :
# 
# * soyez bien attentifs au nombre de fois où vous exécutez les cellules de ce notebook ;
# * par exemple une liste renversée deux fois peut donner l'impression que `reverse` ne marche pas ;
# * n'hésitez pas à utiliser le menu *Cell -> Run All* pour réexécuter en une seule fois le notebook entier.

# ### `append`

# La méthode `append` permet d'ajouter **un élément** à la fin d'une liste :
liste.append('ap')
print('liste', liste)


# ### `extend`

# La méthode `extend` réalise la même opération, mais avec **tous les éléments** de la liste qu'on lui passe en
# argument :
liste2 = ['ex1', 'ex2']
liste.extend(liste2)
print('liste', liste)


# ### `append` *vs* `+`

# Ces deux méthodes `append` et `extend` sont donc assez voisines ; avant de voir d'autres méthodes de `list`,
# prenons un peu le temps de comparer leur comportement avec l'addition `+` de liste. L'élément clé ici, on l'a déjà
# vu dans la vidéo, est que la liste est un objet **mutable**. `append` et `extend` **modifient** la liste sur
# laquelle elles travaillent, alors que l'addition **crée un nouvel objet**.

# pour créer une liste avec les n premiers entiers, on utilise la fonction built-in range(), que l'on convertit en
# liste
a1 = list(range(3))
print(a1)

a2 = list(range(10, 13))
print(a2)

# le fait d'utiliser + crée une nouvelle liste
a3 = a1 + a2

# si bien que maintenant on a trois objets différents
print('a1', a1)
print('a2', a2)
print('a3', a3)


# Comme on le voit, après une addition, les deux termes de l'addition sont inchangés. Pour bien comprendre, voyons
# exactement le même scénario sous pythontutor :
t_ipython().run_line_magic('load_ext', 'ipythontutor')

# **Note** : une fois que vous avez évalué la cellule avec `%%ipythontutor`, vous devez cliquer sur le bouton
# `Forward` pour voir pas à pas le comportement du programme.
get_ipython().run_cell_magic('ipythontutor', 'height=230 ratio=0.7', 'a1 = list(range(3))\na2 = list(range(10, '
                                                                     '13))\na3 = a1 + a2')


# Alors que si on avait utilisé `extend`, on aurait obtenu ceci :
get_ipython().run_cell_magic('ipythontutor', 'height=200 ratio=0.75', 'e1 = list(range(3))\ne2 = list(range(10, '
                                                                      '13))\ne3 = e1.extend(e2)')


# Ici on tire profit du fait que la liste est un objet mutable : `extend` **modifie** l'objet sur lequel on l'appelle
# (ici `e1`). Dans ce scénario on ne crée en tout que deux objets, et du coup il est inutile pour extend de renvoyer
# quoi que ce soit, et c'est pourquoi `e3` ici vaut None.

# C'est pour cette raison que :
# 
# * l'addition est disponible sur tous les types séquences - on peut toujours réaliser l'addition puisqu'on crée un
# nouvel objet pour stocker le résultat de l'addition ; * mais `append` et `extend` ne sont par exemple **pas
# disponibles** sur les chaînes de caractères, qui sont **immuables** - si `e1` était une chaîne, on ne pourrait pas
# la modifier pour lui ajouter des éléments.

# ### `insert`

# Reprenons notre inventaire des méthodes de `list`, et pour cela rappelons nous le contenu de la variable `liste` :
liste

# La méthode `insert` permet, comme le nom le suggère, d'insérer un élément à une certaine position ; comme toujours
# les indices commencent à zéro et donc : insérer à l'index 2
liste.insert(2, '1 bis')
print('liste', liste)

# On peut remarquer qu'un résultat analogue peut être obtenu avec une affectation de slice ; par exemple pour insérer
# au rang 5 (i.e. avant `ap`), on pourrait aussi bien faire :
liste[5:5] = ['3 bis']
print('liste', liste)

# ### `remove`

# La méthode `remove` détruit la **première occurrence** d'un objet dans la liste :
liste.remove(3)
print('liste', liste)


# ### `pop`

# La méthode `pop` prend en argument un indice ; elle permet d'extraire l'élément à cet indice. En un seul appel on obtient la valeur de l'élément et on l'enlève de la liste :
popped = liste.pop(0)
print('popped', popped, 'liste', liste)

# Si l'indice n'est pas précisé, c'est le dernier élément de la liste qui est visé :
popped = liste.pop()
print('popped', popped, 'liste', liste)


# ### `reverse`

# Enfin `reverse` renverse la liste, le premier élément devient le dernier :
liste.reverse()
print('liste', liste)

# On peut remarquer ici que le résultat se rapproche de ce qu'on peut obtenir avec une opération de slicing comme ceci :
liste2 = liste[::-1]
print('liste2', liste2)


# **À la différence toutefois** qu'avec le slicing c'est une copie de la liste initiale qui est retournée,
# la liste de départ quant à elle n'est pas modifiée.

# ### Pour en savoir plus

# <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

# ### Note spécifique aux notebooks

# #### `help` avec `?`

# Je vous signale en passant que dans un notebook vous pouvez obtenir de l'aide avec un point d'interrogation `?`
# inséré avant ou après un symbole. Par exemple pour obtenir des précisions sur la méthode `list.pop`, on peut faire
# soit :
# fonctionne dans tous les environnements Python
help(list.pop)

# spécifique aux notebooks
# l'affichage obtenu est légèrement différent
# tapez la touche 'Esc' - ou cliquez la petite croix
# pour faire disparaitre le dialogue qui apparaît en bas
get_ipython().run_line_magic('pinfo', 'list.pop')


# #### Complétion avec `Tab`

# Dans un notebook vous avez aussi la complétion ; si vous tapez, dans une cellule de code, le début d'un mot connu
# dans l'environnement, vous voyez apparaître un dialogue avec les noms connus qui commencent par ce mot ici `li`;
# utilisez les flèches pour choisir, et 'Return' pour sélectionner.

# placez votre curseur à la fin de la ligne après 'li'
# et appuyez sur la touche 'Tab'
li
