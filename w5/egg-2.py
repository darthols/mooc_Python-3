import sys

# on récupère le répertoire où est installé le point d'entrée
from pathlib import Path

directory_installation = Path(__file__).parent

# et on l'ajoute au chemin de recherche des modules
sys.path.append(directory_installation)

# maintenant on peut importer spam de n'importe où
import spam


def f():
    print(x)


if __name__ == "__main__":
    x = 2

    f()
    spam.f()
    print(spam.x)
