#!/usr/bin/env python3
# coding: utf8
"""
Fichiers système
"""


"""Dans un ordinateur, le système d'exploitation (Windows, Linux, macOS, etc.) comprend un noyau (kernel) qui est un 
logiciel qui a l'exclusivité pour interagir physiquement avec le matériel (processeur(s), mémoire, disque(s), 
périphériques, etc.) ; il offre aux programmes utilisateur (userspace) des abstractions pour interagir avec ce 
matériel. 

La notion de fichier, telle qu'on l'a vue dans la vidéo, correspond à une de ces abstractions ; elle repose 
principalement sur les quatre opérations élémentaires suivantes : 
    open ;
    close ;
    read ;
    write.

Parmi les autres conventions d'interaction entre le système (pour être précis : le shell) et une application, 
il y a les notions de : 
    entrée standard (standard input, en abrégé stdin) ;
    sortie standard (standard output, en abrégé stdout) ;
    erreur standard (standard error, en abrégé stderr).

Ceci est principalement pertinent dans le contexte d'un terminal. L'idée c'est que l'on a envie de pouvoir rediriger 
les entrées-sorties d'un programme sans avoir à le modifier. De la sorte, on peut également chaîner des traitements à 
l'aide de pipes, sans avoir besoin de sauver les résultats intermédiaires sur disque. 

Ainsi par exemple lorsque l'on écrit :
    $ monprogramme < fichier_entree > fichier_sortie

Les deux fichiers en question sont ouverts par le shell, et passés à monprogramme - que celui-ci soit écrit en C, 
en Python ou en Java - sous la forme des fichiers stdin et stdout respectivement, et donc déjà ouverts.

"""

import sys


for channel in (sys.stdin, sys.stdout, sys.stderr):
    print(channel)

"""
On n'a pas extrêmement souvent besoin d'utiliser ces variables en règle générale, mais elles peuvent s'avérer 
utiles dans des contextes spécifiques. 

Par exemple, l'instruction print écrit dans sys.stdout (c'est-à-dire la sortie standard). Et comme sys.stdout est une 
variable (plus exactement stdout est un attribut dans le module référencé par la variable sys) et qu'elle référence 
un objet fichier, on peut lui faire référencer un autre objet fichier et ainsi rediriger depuis notre programme tous 
les sorties, qui sinon iraient sur le terminal, vers un fichier de notre choix : 
"""

# ici je fais exprès de ne pas utiliser un `with` car très souvent les deux redirections apparaissent dans
# des fonctions différentes

# on ouvre le fichier destination
autre_stdout = open('../data/ma_sortie.txt', 'w', encoding='utf-8')
# on garde un lien vers le fichier sortie standard pour le réinstaller plus tard si besoin.
tmp = sys.stdout
print('sur le terminal')

# première redirection
sys.stdout = autre_stdout
print('dans le fichier')

# on remet comme c'était au début
sys.stdout = tmp
# et alors pour être propre on n'oublie pas de fermer
autre_stdout.close()
print('de nouveau sur le terminal')
