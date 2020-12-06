"""
utils.py
Fichier contenant des fonctions utilitaires pour l'exécution des tests. 
Ne surtout pas supprimer ce fichier.
Auteurs : Antoine Gaulin && Eya-Tom Augustin SANGAM & Hélène Jiang 
"""

import _thread
import threading
import unittest


## Timeout
def exitFunction():
    _thread.interrupt_main()


def timeout(s):
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, exitFunction)
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result

        return inner

    return outer


## Test basique
class TestBasique(unittest.TestCase):

    @timeout(1)  # Termine le programme quand l'execution dure plus d'une seconde
    def executerTest(self, fonction, nomFonctionTestee):
        try:
            fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nomFonctionTestee} ne se termine pas --> Vérifiez vos boucles')
        except AssertionError as e:
            raise e
        except:
            self.fail(
                f'Une exception a été levée lors de l\'appel fonction {nomFonctionTestee}. Revérifier votre code.')


## MauvaiseEntreeException
class MauvaiseEntreeException(Exception):
    """
    MauvaiseEntreeException
    """
    pass
