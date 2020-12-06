"""
matrice_module.py
Module Matrice du TP5 du cours INF1005D
Description : Module qui regroupe toutes les opérations communes à une matrice
Auteurs     : À remplir. Vous devez spécifier vos noms et matricules 
"""
import math
import random

from arreter_programme import arreter_programme
from utils import MauvaiseEntreeException

DEFAULT_MIN_FLOAT = -10**15
DEFAULT_MAX_FLOAT = 10**15


def est_un_entier(n):
    """
    Fonction est_un_entier

    Cette fonction permet de déterminer si un nombre est un entier ou non.
    Retourne True si le nombre est un entier, False si non.
    """
    try:
        return float(n).is_integer()
    except ValueError:
        pass
    return False


def est_un_nombre(n):
    """
    Fonction est_un_nombre

    Cette fonction permet de déterminer si 'n' est valide ou non.
    Retourne True si le nombre est un nombre, False si non.
    """
    try:
        return math.isfinite(n)
    except ValueError:
        pass
    return False


def init(m, n, valeur):
    """
    Fontion init

    Cette fonction permet de créer et initialiser une matrice de taille m ⨉ n contenant uniquement le nombre 'valeur'.
    """
    # Cette fonction doit s'arrêter si m ou n n'est pas un entier ou si nombre n'est pas un nombre valide.
    # Pour arrêter une fonction, appeler la fonction arreter_programme(). Vous pouvez lui donner en argument, la raison pour laquelle vous arrêtez le programme.
    if not est_un_entier(m) or m <= 0:
        arreter_programme(f'{m} n\'est pas un nombre de lignes valide')
    if not est_un_entier(n) or n <= 0:
        arreter_programme(f'{n} n\'est pas un nombre de colonnes valide')
    if not est_un_nombre(valeur):
        arreter_programme(f'{valeur} n\'est pas un nombre valide')
    return [[valeur for _ in range(n)] for _ in range(m)]


def zeros(m, n):
    """
    Fonction zeros

    Initialise et retourne une matrice de taille m ⨉ n de zéros.
    """
    # TODO
    # Cette fonction est un cas particulier de la fonction init(). Veuillez donc faire un appel fonction à init().
    return []


def ones(m, n):
    """
    Fonction ones

    Initialise et retourne une matrice de taille m ⨉ n de uns.
    """
    # TODO
    # Cette fonction est un cas particulier de la fonction init(). Veuillez donc faire un appel fonction à init().
    return []


def identite(m):
    """
    Fonction identite

    Initialise et retourne une matrice identité carrée de taille m ⨉ m.
    """
    # TODO
    # Cette fonction doit s'arrêter si m n'est pas un entier valide.
    # Pour en savoir plus sur les matrices identités : https://en.wikipedia.org/wiki/Identity_matrix
    return []


def aleatoire(m, n, min=DEFAULT_MIN_FLOAT, max=DEFAULT_MAX_FLOAT):
    """
    Fonction init

    Initialise et retourne une matrice de taille m ⨉ n de nombres aléatoires compris entre min et max.
    """
    # TODO
    # Cette fonction doit s'arrêter si :
    #     ‣ m n'est pas un entier positif ou
    #     ‣ n n'est pas un entier positif ou
    #     ‣ min n'est pas un nombre valide ou
    #     ‣ max n'est pas un nombre valide ou
    #     ‣ min > max.
    # Si les arguments min et max ne sont pas fournis, supposer qu'ils valent respectivement DEFAULT_MIN_FLOAT et DEFAULT_MAX_FLOAT
    return []


def taille(matrice):
    """
    Fonction taille

    Fonction qui permet de déterminer la taille d'une matrice.
    Cette fonction retourne un tuple (m, n) si la matrice de taille m ⨉ n, ou None si la matrice est invalide.
    """
    # TODO
    # Une matrice invalide est une matrice :
    #     ‣ qui n'a pas de lignes ou
    #     ‣ qui n'a pas de colones ou
    #     ‣ qui a des lignes ayant plus de colonnes que d'autres
    #     ‣ qui contient des valeurs qui ne sont pas des nombres finis. Pour vérifier cette condition, utiliser la fonction est_un_nombre()
    return None


def addition(matrice1, matrice2):
    """
    Fonction addition

    Fonction pour additionner deux matrices de même dimension.
    Cette fonction retourne la matrice résultante qui est le résultat de l'opération matrice1 + matrice2.
    """
    # TODO
    # Si les matrices ne sont pas de même dimension, ou si une des matrices est invalide, arrêter le programme.
    return []


def soustraction(matrice1, matrice2):
    """
    Fonction soustraction

    Fonction pour soustraire deux matrices de même dimension.
    Cette fonction retourne la matrice résultante qui est le résultat de l'opération matrice1 - matrice2.
    """
    # TODO
    # Si les matrices ne sont pas de même dimension, ou si une des matrices est invalide, arrêter le programme.
    return []


def multiplication(matrice1, matrice2):
    """
    Fonction multiplication

    Fonction pour multiplier deux matrices compatibles.
    Cette fonction retourne la matrice résultante qui est le résultat de l'opération matrice1 ⨉ matrice2.
    """
    if len(matrice1[0])!= len(matrice2):
        return arreter_programme(f'les matrices ne sont pas compatibles')
    

    if matrice1[0] and len(matrice1[0]) != len(matrice2):
        return -1
    multiplication = [[sum(a * b for a, b in zip(matrice1_row, matrice2_col)) for matrice2_col in zip(*matrice2)] for matrice1_row in matrice1]
    return multiplication


def transposition(matrice):
    """
    Fonction multiplication

    Fonction pour multiplier deux matrices compatibles.
    Cette fonction retourne la matrice résultante qui est le résultat de l'opération matrice1 ⨉ matrice2.
    """
    # TODO
    # Si la matrice est de taille invalide, ou contient des éléments invalides, arrêter le programme.
    if not est_un_nombre(matrice[i][j]):
        return arreter_programme(f'matrice invalide')
    
    transpo = [[0]*len(matrice) for i in range(len(matrice[0]))]
    
    for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                transpo[j][i]= matrice[i][j]
            
    return transpo


def puissance(matrice, exposant):
    """
    Fonction puissance

    Fonction pour élever une matrice à un exposant donné.
    Cette fonction retourne la matrice résultante qui est le résultat de l'opération matriceᵉˣᵖᵒˢᵃⁿᵗ.
    E.g. : matrice⁰ = Matrice identité ; matrice² = matrice ⨉ matrice ; matrice³ = matrice ⨉ matrice ⨉ matrice.
    """
    
    # TODO
    # Arrêter le programme si :
    # ‣ Si la matrice est de taille invalide ou
    # ‣ Si la matrice n'est pas carrée ou 
    # ‣ Si la matrice ou contient des éléments invalides ou
    # ‣ Si n n'est pas un nombre entier positif
    
    if len(matrice)!= len(matrice[0]):
        return arreter_programme(f"La matrice n'est pas carree")


    if exposant < 0:
        return arreter_programme(f"L'exposant n'est pas un entier positif")
    
    for i in range(1, exposant+1):
        if not est_un_nombre(matrice[i][j]):
             arreter_programme(f'matrice invalide')
             puissance=1
             puissance = puissance * matrice
        return puissance
    

    puissance = 1
    while exposant>0:
        if exposant%2!=0: # y impair
            puissance *= matrice
        matrice *= matrice    
        exposant //= 2 # division entière par 2
    return exposant

def main():
    # Faites tous vos tests ici
    pass


if __name__ == '__main__':
    try:
        main()
    except MauvaiseEntreeException as e:
        print(e)
