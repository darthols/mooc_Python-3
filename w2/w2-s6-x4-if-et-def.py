
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Instruction `if` et fonction `def`

# ## Exercice - niveau basique

# ### Fonction de divisibilité

# In[1]:


# chargement de l'exercice
from corrections.exo_divisible import exo_divisible


# L'exercice consiste à écrire une fonction baptisée `divisible` qui retourne une valeur booléenne, qui indique si un des deux arguments est divisible par l'autre.
# 
# Vous pouvez supposer les entrées `a` et `b` entiers et non nuls, mais pas forcément positifs.

# In[3]:


def divisible(a, b):
    if a % b == 0 or b % a == 0:
        return True
    return False


# Vous pouvez à présent tester votre code en évaluant ceci, qui écrira un message d'erreur si un des jeux de test ne donne pas le résultat attendu.

# In[4]:


# tester votre code
exo_divisible.correction(divisible)


# ## Exercice - niveau basique

# ##### Fonction définie par morceaux

# In[5]:


# chargement de l'exercice
from corrections.exo_morceaux import exo_morceaux


# On veut définir en Python une fonction qui est définie par morceaux :

# $$
# f: x \longrightarrow \left\{
# \begin{array}{ll}
# -x - 5          & \mbox{si } x \leqslant -5 \\
# 0               & \mbox{si } x \in [-5, 5]  \\
# \frac{1}{5}x -1 & \mbox{si } x \geqslant 5  \\
# \end{array}
# \right.
# $$

# In[6]:


# donc par exemple
exo_morceaux.example()


# In[9]:


# à vous de jouer

def morceaux(x):
    if x <= -5:
        return (-x - 5)
    if x >= -5 and x <= 5:
        return 0
    return (x / 5) - 1


# In[10]:


# pour corriger votre code
exo_morceaux.correction(morceaux)


# ##### Représentation graphique

# L'exercice est terminé, mais nous allons maintenant voir ensemble comment vous pourriez visualiser votre fonction.
# 
# Voici ce qui est attendu comme courbe pour `morceaux` (image fixe) :
# ![graphe morceaux](media/morceaux.png)

# En partant de votre code, vous pouvez produire votre propre courbe en utilisant `numpy` et `matplotlib` comme ceci :

# In[11]:


# on importe les bibliothèques
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


# un échantillon des X entre -10 et 20
X = np.linspace(-10, 20)

# et les Y correspondants
Y = np.vectorize(morceaux)(X)


# In[13]:


# on n'a plus qu'à dessiner
plt.plot(X, Y)
plt.show()

