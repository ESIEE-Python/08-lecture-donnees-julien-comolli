"""
Exercice fichier, csv
"""

#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        # J'utilise CSV READER ici car plus simple pour avoir les nombres
        # déjà sépérés plutôt que d'utiliser plus tard split, replace pour
        # nettoyer la ligne
        l = list(csv.reader(f, delimiter=';'))

        # Conversion de toutes les chaînes en entier
        for i, li in enumerate(l):
            l[i] = list(map(int, li))

    return l

def get_list_k(data, k):
    """
    Retourne la k ième ligne si elle existe, sinon None.
    """
    if len(data) > k:
        return data[k]

    return None
    # >>> python retourne None par défaut mais pour pylint on le rajoute.

def get_first(l):
    """
    Retourne le premier element de la liste s'il existe.
    """
    if len(l) > 0:
        return l[0]

    return None


def get_last(l):
    """
    Retourne le dernier élement de la liste.
    """
    if len(l) > 0:
        return l[len(l) - 1]

    return None


def get_max(l):
    """
    Retourne le max de la liste d'entier.
    """

    if len(l) > 0:
        return max(l)

    return None


def get_min(l):
    """
    Retourne le min de la liste d'entier.
    """
    if len(l) > 0:
        return min(l)

    return None



def get_sum(l):
    """
    Retourne la somme de la liste d'entier.
    """

    if len(l) > 0:
        return sum(l)

    return None



#### Fonction principale


def main():
    """
    Fonction principale.
    """

    data = read_data(FILENAME)

    k = 37
    print("Ligne :", k)
    print(get_list_k(data, k))
    print("last", get_last(data[k]))
    print("max ", get_max(data[k]))
    print("min ", get_min(data[k]))
    print("sum ", get_sum(data[k]))

if __name__ == "__main__":
    main()
