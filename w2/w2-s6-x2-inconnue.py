
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Séquences

# ## Exercice - niveau basique

# ### Slicing

# Commençons par créer une chaîne de caractères. Ne vous inquiétez pas si vous ne comprenez pas encore le code d'initialisation utilisé ci-dessous.
# 
# Pour les plus curieux, l'instruction `import`  permet de charger dans votre programme une boîte à outils que l'on appelle un module. Python vient avec de nombreux modules qui forment la bibliothèque standard. Le plus difficile avec les modules de la bibliothèque standard est de savoir qu'ils existent. En effet, il y en a un grand nombre et bien souvent il existe un module pour faire ce que vous souhaitez.
# 
# Ici en particulier nous utilisons le module `string`.

# In[1]:


# nous allons tirer profit ici d'une 
# constante définie dans le module string
import string
chaine = string.ascii_lowercase

# et voici sa valeur
print(chaine)


# Pour chacune des sous-chaînes ci-dessous, écrire une expression de slicing sur `chaine` qui renvoie la sous-chaîne. La cellule de code doit retourner `True`.

# Par exemple, pour obtenir "def" :

# In[2]:


chaine[3:6] == "def"


# 1) Écrivez une slice pour obtenir "vwx" (n'hésitez pas à utiliser les indices négatifs) :

# In[5]:


chaine[:-4] == "vwx"


# 2) Une slice pour obtenir "wxyz" (avec une seule constante) :

# In[6]:


chaine[len(chaine) - 4:] == "wxyz"


# 3) Une slice pour obtenir "dfhjlnprtvxz" (avec deux constantes) :

# In[7]:


chaine[3::2] == "dfhjlnprtvxz"


# 4) Une slice pour obtenir "xurolifc" (avec deux constantes) :

# In[9]:


chaine[-3::-3] == "xurolifc"


# ## Exercice - niveau intermédiaire

# ### Longueur

# In[10]:


# il vous faut évaluer cette cellule magique
# pour charger l'exercice qui suit
# et autoévaluer votre réponse
from corrections.exo_inconnue import exo_inconnue


# On vous donne une chaîne `composite` dont on sait qu'elle a été calculée à partir de deux chaînes `inconnue` et `connue` comme ceci :
# ```python
# composite = connue + inconnue + connue
# ```

# On vous donne également la chaîne `connue`. Imaginez par exemple que vous avez (ce ne sont pas les vraies valeurs) :
# ```python
# connue = '0bf1'
# composite = '0bf1a9730e150bf1'
# ```
# alors, dans ce cas :
# ```python
# inconnue = 'a9730e15'
# ```

# L'exercice consiste à écrire une fonction qui retourne la valeur de `inconnue` à partir de celles de `composite` et `connue`. Vous pouvez admettre que `connue` n'est pas vide, c'est-à-dire qu'elle contient au moins un caractère.

# Vous pouvez utiliser du *slicing*, et la fonction `len()`, qui retourne la longueur d'une chaîne :

# In[11]:


len('abcd')


# In[13]:


# à vous de jouer
def inconnue(composite, connue):
    return composite[len(connue):-len(connue)]


# Une fois votre code évalué, vous pouvez évaluer la cellule suivante pour vérifier votre résultat.

# In[14]:


# correction
exo_inconnue.correction(inconnue)


# Lorsque vous évaluez cette cellule, la correction vous montre :
# 
# * dans la première colonne l'appel qui est fait à votre fonction ;
# * dans la seconde colonne la valeur attendue pour `inconnue` ;
# * dans la troisième colonne ce que votre code a réellement calculé.
# 
# Si toutes les lignes sont **en vert** c'est que vous avez réussi cet exercice.

# Vous pouvez essayer autant de fois que vous voulez, mais il vous faut alors à chaque itération :
# 
# * évaluer votre cellule-réponse (là où vous définissez la fonction `inconnue`) ;
# * et ensuite évaluer la cellule correction pour la mettre à jour.
