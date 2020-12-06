"""
main.py
Fichier qui permet d'avoir un aperçu global de tous les tests
Auteurs : Antoine Gaulin && Eya-Tom Augustin SANGAM & Hélène Jiang 
"""

import os
import unittest

if __name__ == '__main__':
    __location__ = os.path.realpath(
        os.path.join(
            os.getcwd(),
            os.path.dirname(__file__)
        )
    )

    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__))
    suite = loader.discover(start_dir, pattern="*_tests.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
