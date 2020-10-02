
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Comptage dans les chaines

# ## Exercice - niveau basique

# Nous remercions Benoit Izac pour cette contribution aux exercices.

# ## La commande UNIX wc(1)
# 
# ---
# 
# Sur les systèmes de type UNIX, la commande [wc](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/wc.html) permet de compter le nombre de lignes, de mots et d'octets (ou de caractères) présents sur l'entrée standard ou contenus dans un fichier.
# 
# L'exercice consiste à écrire une fonction nommée *wc* qui prendra en argument une chaîne de caractères et retournera une liste contenant trois éléments :
# 
# 1. le nombre de lignes (plus précisément le nombre de retours à la ligne) ;
# 2. le nombre de mots (un mot étant séparé par des espaces) ;
# 3. le nombre de caractères (on utilisera uniquement le jeu de caractères ASCII).

# In[1]:


# chargement de l'exercice
from corrections.exo_wc import exo_wc


# In[2]:


# exemple
exo_wc.example()


# **Indice** : nous avons vu rapidement la boucle `for`, sachez toutefois qu'on peut tout à fait résoudre l'exercice en utilisant uniquement la bibliothèque standard.
# 
# **Remarque** : usuellement, ce genre de fonctions retournerait plutôt un tuple qu'une liste, mais comme nous ne voyons les tuples que la semaine prochaine..
# 

# À vous de jouer :

# In[34]:


# la fonction à implémenter
def wc(string):
    return [string.count("\n"),             len(string.split()),             len(string)]


# In[35]:


# correction
exo_wc.correction(wc)

