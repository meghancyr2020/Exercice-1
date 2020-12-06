"""
arreter_programme.py
Auteurs : Antoine Gaulin && Eya-Tom Augustin SANGAM & Hélène Jiang 
"""

from utils import MauvaiseEntreeException


def arreter_programme(raisonMauvaiseEntree=''):
    """
    Fonction arreter_programme
    
    Cette fonction se charge d'arrêter le programme à votre place. 
    Vous pouvez lui donner en paramètres une chaîne de caractères donnant la raison pour laquelle vous pensez que l'entrée est mauvaise
    """
    raise MauvaiseEntreeException(f'Erreur : {raisonMauvaiseEntree}\n')
