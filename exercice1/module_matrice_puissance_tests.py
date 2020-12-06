import unittest

from arreter_programme import MauvaiseEntreeException
from module_matrice import puissance
from utils import TestBasique


class ModuleMatricePuissanceTest(TestBasique):

    def test_mauvaises_matrices(self):
        mauvaisesMatrices = [
            [[]],
            [[1, 2]],
            [[1, 2], [3, 4], [5, 6]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2], [1, float('nan')]],
            [[1, 2], [1, float('inf')]],
            [[1, 10], [1, float('-inf')]],
            [[1, 2, 3], [-1, -2, -3], [0, 0, 0], [0]]
        ]
        for matrice in mauvaisesMatrices:
            def fonction():
                try:
                    puissance(matrice, 2)
                    self.fail(
                        f'{matrice} n\'est pas une matrice carrée valide. La fonction puissance() devrait appeler la fonction arreter_programme() quand un tel cas survient')
                except MauvaiseEntreeException:
                    pass
            self.executerTest(fonction, f'puissance({matrice}, 2)')

    def test_puissance(self):
        casDeTests = [
            (([[1]], 0), [[1]]),
            (([[1]], 1), [[1]]),
            (([[1]], 2), [[1]]),
            (([[1]], 20), [[1]]),
            (([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 20),
             [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            (([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 0),
             [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            (([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 10), [[13732435440, 17713440288, 21694445136], [
             42154372512, 54374838624, 66595304736], [70576309584, 91036236960, 111496164336]]),
        ]
        for (matrice, exposant), matriceAttendue in casDeTests:
            def fonction():
                matriceObtenue = puissance(matrice, exposant)
                self.assertEqual(
                    matriceObtenue,
                    matriceAttendue,
                    f'La matrice retournée par l\'appel fonction puissance({matrice}, {exposant}) n\'est pas valide. La valeur attendue est {matriceAttendue}. La valeur obtenue est {matriceObtenue}.')
            self.executerTest(fonction, f'puissance({matrice}, {exposant})')


if __name__ == '__main__':
    unittest.main(verbosity=2)
