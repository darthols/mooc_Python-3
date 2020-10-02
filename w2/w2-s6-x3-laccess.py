
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" style="display:inline" /></span>
# </div>

# # Listes

# ## Exercice - niveau basique

# In[1]:


from corrections.exo_laccess import exo_laccess


# Vous devez écrire une fonction `laccess` qui prend en argument une liste, et qui retourne :
# 
# * `None` si la liste est vide ;
# * sinon le dernier élément de la liste si elle est de taille paire ;
# * et sinon l'élément du milieu.

# In[2]:


exo_laccess.example()


# In[32]:


# écrivez votre code ici
def laccess(liste):
    if liste == [] or liste == '':
        return None
    if len(liste) % 2 == 0:
        return liste[len(liste) - 1]
    else:
        return liste[len(liste) // 2]


# In[33]:


# pour le corriger
exo_laccess.correction(laccess)


# Une fois que votre code fonctionne, vous pouvez regarder si par hasard il marcherait aussi avec des chaînes :

# In[34]:


from corrections.exo_laccess import exo_laccess_strings


# In[35]:


exo_laccess_strings.correction(laccess)

