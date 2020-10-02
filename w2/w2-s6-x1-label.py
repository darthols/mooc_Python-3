
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Formatage des chaines de caractères

# ## Exercice - niveau basique

# In[1]:


# charger l'exercice
from corrections.exo_label import exo_label


# Vous devez écrire une fonction qui prend deux arguments :
# 
# * une chaîne de caractères qui désigne le prénom d'un élève ;
# * un entier qui indique la note obtenue.
# 
# Elle devra retourner une chaîne de caractères selon que la note est
# 
# * $0  \leqslant note \lt 10$
# * $10 \leqslant note \lt 16$
# * $16 \leqslant note \leqslant 20$
# 
# comme on le voit sur les exemples :

# In[2]:


exo_label.example()


# In[5]:


# à vous de jouer
def label(prenom, note):
    if note < 10:
        return(f"{prenom} est recalé")
    else:
        if note < 16:
            return(f"{prenom} est reçu")
    return(f"félicitations à {prenom}")


# In[6]:


# pour corriger
exo_label.correction(label)

